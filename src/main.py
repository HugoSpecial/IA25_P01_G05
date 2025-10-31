from constraint import Problem
from load import load_data_txt
from hard_constraints_def import *
from soft_constraints_def import *

# === Carregar dados ===
dados = load_data_txt()

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
blocos = list(range(1, 21))
horas = [9, 11, 14, 16]

salas = ["Lab01", "Lab02", "Lab03"]

turmas = list(dados['classes'].keys())
ucs = [uc for ucs_list in dados['classes'].values() for uc in ucs_list]

# UC → Turma e UC → Professor
uc_to_turma = {}
uc_to_professor = {}
for turma, ucs_list in dados['classes'].items():
    for uc in ucs_list:
        uc_to_turma[uc] = turma
        for prof, prof_ucs in dados['teachers'].items():
            if uc in prof_ucs:
                uc_to_professor[uc] = prof
                break

# === Criar problema CSP ===
problem = Problem()
all_vars = []

for uc in ucs:
    turma = uc_to_turma[uc]
    prof = uc_to_professor.get(uc)
    if not prof:
        print(f"⚠️ UC {uc} sem professor. Ignorada.")
        continue

    disp_slots = dados['time_availabilities'].get(prof, list(range(1, 21)))
    if not disp_slots:
        print(f"⚠️ UC {uc} do prof {prof} sem slots. Ignorada.")
        continue

    salas_validas = [dados['room_restrictions'][uc]] if uc in dados['room_restrictions'] else salas
    dominio = [(slot, s, prof, turma, uc) for slot in disp_slots for s in salas_validas]

    if not dominio:
        print(f"⚠️ UC {uc} sem domínios válidos. Ignorada.")
        continue

    # Variáveis separadas para cada aula da UC
    var1, var2 = f"UC{uc}_A1", f"UC{uc}_A2"
    problem.addVariable(var1, dominio)
    problem.addVariable(var2, dominio)
    all_vars.extend([var1, var2])

for i in range(len(all_vars)):
    for j in range(i + 1, len(all_vars)):
        problem.addConstraint(no_same_room_same_time, (all_vars[i], all_vars[j]))
        problem.addConstraint(no_same_turma_same_time, (all_vars[i], all_vars[j]))
        problem.addConstraint(no_same_professor_same_time, (all_vars[i], all_vars[j]))

for t in turmas:
    vars_t = [v for v in all_vars if uc_to_turma[v.split('_')[0][2:]] == t]
    if vars_t:
        problem.addConstraint(max_three_per_day_turma, vars_t)

for uc in ucs:
    var1, var2 = f"UC{uc}_A1", f"UC{uc}_A2"
    if var1 in all_vars and var2 in all_vars:
        problem.addConstraint(same_uc_different_days, (var1, var2))

problem.addConstraint(lambda *a: exactly_two_per_uc(*a, ucs=ucs), all_vars)
problem.addConstraint(lambda *a: exactly_ten_per_turma(*a, turmas=turmas), all_vars)

# === Gerar soluções iterativamente ===
print("🧩 A gerar soluções válidas...")
MAX_SOLUTIONS = 200
solucoes = []

for sol in problem.getSolutionIter():
    solucoes.append(sol)
    if len(solucoes) >= MAX_SOLUTIONS:
        break

if not solucoes:
    print("❌ Nenhuma solução possível com os dados atuais")
    exit()

print(f"✅ Encontradas {len(solucoes)} soluções válidas (limitadas a {MAX_SOLUTIONS})")

# === Avaliar soft constraints ===
def pontuacao(sol):
    aulas = []
    for val in sol.values():
        slot, sala, prof, turma, uc = val
        slot = int(slot)
        dia_index = (slot - 1) // 4
        bloco_index = (slot - 1) % 4
        dia = dias[dia_index]
        hora = horas[bloco_index]
        aulas.append((dia, hora, sala, prof, turma, uc))
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
    tabela = {dia: [""]*4 for dia in dias}
    for val in melhor_sol.values():
        slot, sala, prof, turma, uc = val
        if turma == t:
            dia_index = (slot-1)//4
            bloco_index = (slot-1)%4
            tabela[dias[dia_index]][bloco_index] = f"{uc} ({sala}, {prof})"

    print(f"{'Bloco':<6}" + ''.join(f"{d:<22}" for d in dias))
    for i in range(4):
        print(f"{i+1:<6}" + ''.join(f"{tabela[d][i]:<22}" for d in dias))
    print()
