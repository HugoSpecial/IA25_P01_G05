from constraint import Problem
from data_config import *
from hard_constraints_def import *
from soft_constraints_def import *

# Criar CSP
problem = Problem()
all_vars = []

# Adicionar variáveis: 2 aulas por UC
for uc in ucs:
    turma = uc_to_turma[uc]
    prof = uc_to_professor[uc]
    disp = horarios_disponiveis(prof)
    dominio = [(d,h,s,prof,turma,uc) for s in salas for d,h in disp]
    problem.addVariable(f"UC{uc}_A1", dominio)
    problem.addVariable(f"UC{uc}_A2", dominio)
    all_vars.extend([f"UC{uc}_A1", f"UC{uc}_A2"])

# Conflitos de sala
for i in range(len(all_vars)):
    for j in range(i+1,len(all_vars)):
        problem.addConstraint(no_same_room_same_time, (all_vars[i], all_vars[j]))

# Máx. 3 aulas/dia por turma
for t in turmas:
    vars_t = [v for v in all_vars if uc_to_turma[int(v[2:v.find('_')])]==t]
    problem.addConstraint(max_three_per_day_turma, vars_t)

# Mesma UC em dias diferentes
for uc in ucs:
    problem.addConstraint(same_uc_different_days, (f"UC{uc}_A1", f"UC{uc}_A2"))

# Cada UC → 2 aulas
problem.addConstraint(lambda *a: exactly_two_per_uc(*a, ucs=ucs), all_vars)

# Cada turma → 10 aulas
problem.addConstraint(lambda *a: exactly_ten_per_turma(*a, turmas=turmas), all_vars)


print("🧩 A procurar soluções válidas...")
# Gera soluções de forma iterativa e limita a quantidade
solucoes = []
max_solucoes = 500  # ← ajusta conforme o tamanho do problema

for sol in problem.getSolutionIter():
    solucoes.append(sol)
    if len(solucoes) >= max_solucoes:
        break

if not solucoes:
    print("❌ Nenhuma solução encontrada")
else:
    print(f"✅ Foram encontradas {len(solucoes)} soluções válidas\n")
    print("🔎 A avaliar qualidade das soluções...")

    def avaliar_solucao(sol):
        aulas = list(sol.values())
        score = 0
        if check_distinct_day_classes(*aulas): score += 1
        if check_weekly_days(*aulas): score += 1
        if check_consecutive_classes(*aulas): score += 1
        if check_different_classes(*aulas): score += 1
        return score

    avaliadas = [(sol, avaliar_solucao(sol)) for sol in solucoes]
    avaliadas.sort(key=lambda x: x[1], reverse=True)

    melhor_sol, melhor_score = avaliadas[0]
    print(f"🏆 Melhor solução com pontuação {melhor_score}/4\n")



# Resolver
print("🧩 A procurar solução...")
sol = problem.getSolution()

if sol:
    print("✅ Solução encontrada!\n")
    for t in turmas:
        print(f"📘 Turma {t}")
        tabela = {d:{h:"" for h in horas} for d in dias}
        for var,val in sol.items():
            d,h,_,_,turma,uc = val
            if turma==t:
                tabela[d][h]=f"UC{uc}"
        print(f"{'Hora':<6}"+''.join(f"{d:<15}" for d in dias))
        for h in horas:
            print(f"{h:<6}"+''.join(f"{tabela[d][h]:<15}" for d in dias))
        print()
else:
    print("❌ Nenhuma solução encontrada")