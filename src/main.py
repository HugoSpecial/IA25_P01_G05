from constraint import Problem
from data_config import *
from hard_constraints_def import *
from soft_constraints_def import *

# === Criar problema CSP ===
problem = Problem()
all_vars = []

# 2 aulas por UC
for uc in ucs:
    turma = uc_to_turma[uc]
    prof = uc_to_professor[uc]
    disp = check_professor_availability(prof)
    dominio = [(d, h, s, prof, turma, uc) for s in salas for d, h in disp]
    problem.addVariable(f"UC{uc}_A1", dominio)
    problem.addVariable(f"UC{uc}_A2", dominio)
    all_vars.extend([f"UC{uc}_A1", f"UC{uc}_A2"])

# === Restrições rígidas ===
for i in range(len(all_vars)):
    for j in range(i + 1, len(all_vars)):
        problem.addConstraint(no_same_room_same_time, (all_vars[i], all_vars[j]))

for t in turmas:
    vars_t = [v for v in all_vars if uc_to_turma[int(v[2:v.find('_')])] == t]
    problem.addConstraint(max_three_per_day_turma, vars_t)

for uc in ucs:
    problem.addConstraint(same_uc_different_days, (f"UC{uc}_A1", f"UC{uc}_A2"))

for var in all_vars:
    problem.addConstraint(check_duration, [var])

problem.addConstraint(lambda *a: exactly_two_per_uc(*a, ucs=ucs), all_vars)
problem.addConstraint(lambda *a: exactly_ten_per_turma(*a, turmas=turmas), all_vars)

# === Gerar até 200 soluções válidas ===
print("🧩 A gerar soluções válidas...")
solucoes = []
for sol in problem.getSolutionIter():
    solucoes.append(sol)
    if len(solucoes) >= 200:
        break

if not solucoes:
    print("❌ Nenhuma solução encontrada")
    exit()

print(f"✅ Encontradas {len(solucoes)} soluções válidas")

# === Avaliar cada solução com soft constraints ===
def pontuacao(sol):
    aulas = list(sol.values())
    score = 0
    if check_distinct_day_classes(*aulas): score += 1
    if check_weekly_days(*aulas): score += 1
    if check_consecutive_classes(*aulas): score += 1
    if check_different_classes(*aulas): score += 1
    return score

avaliadas = [(sol, pontuacao(sol)) for sol in solucoes]
avaliadas.sort(key=lambda x: x[1], reverse=True)

melhor_sol, melhor_score = avaliadas[0]
print(f"🏆 Melhor solução encontrada com pontuação: {melhor_score}/4\n")

# === Visualizar melhor solução ===
for t in turmas:
    print(f"📘 Turma {t}")
    tabela = {d: {h: "" for h in horas} for d in dias}
    for val in melhor_sol.values():
        d, h, sala, prof, turma, uc = val
        if int(turma) == int(t):
            tabela[d][h] = f"UC{uc} ({sala}, Prof {prof})"

    print(f"{'Hora':<6}" + ''.join(f"{d:<22}" for d in dias))
    for h in horas:
        print(f"{h:<6}" + ''.join(f"{tabela[d][h]:<22}" for d in dias))
    print()
