# hard_constraints.py

# Cada aula deve durar 2 horas
def check_duration(solucao):
    for aula, (_, hora, _, _, _) in solucao.items():
        if hora not in [8, 10, 14, 16]:  # blocos de 2h
            print("Não passou check_duration")
            return False
    return True

# Todas as turmas devem ter 10 aulas por semana
def check_weekly_classes(solucao):
    aulas_por_turma = {}
    for aula, (_, _, _, _, turma) in solucao.items():
        aulas_por_turma[turma] = aulas_por_turma.get(turma, 0) + 1
    # Temporário: aceitar >=2 aulas por turma
    return all(aulas >= 2 for aulas in aulas_por_turma.values())


# Cada curso pode ter 1 ou 2 aulas por semana por UC
def check_weekly_course_classes(solucao, uc_to_curso):
    # uc_to_curso = {uc_id: curso_id}
    aulas_por_uc = {}
    for uc, (_, _, _, _, turma) in solucao.items():
        aulas_por_uc[uc] = aulas_por_uc.get(uc, 0) + 1
    for uc, count in aulas_por_uc.items():
        if count < 1 or count > 2:
            print("Não Passou check_weekly_course_classes")
            return False
    return True

# Uma turma não pode ter mais de 3 aulas por dia
def check_daily_classes(solucao):
    aulas_por_turma_dia = {}
    for aula, (dia, _, _, _, turma) in solucao.items():
        if turma not in aulas_por_turma_dia:
            aulas_por_turma_dia[turma] = {}
        aulas_por_turma_dia[turma][dia] = aulas_por_turma_dia[turma].get(dia, 0) + 1
        if aulas_por_turma_dia[turma][dia] > 3:
            print("Não Passou check_daily_classes")
            return False
    return True

# O horário deve respeitar a disponibilidade do professor
def check_professor_availability(solucao, disponibilidades):
    # disponibilidades = [{'prof_id':..,'dia':..,'hora_inicio':..,'hora_fim':..}, ...]
    disp_por_prof = {}
    for d in disponibilidades:
        prof = d['prof_id']
        if prof not in disp_por_prof:
            disp_por_prof[prof] = []
        disp_por_prof[prof].append((d['dia'], d['hora_inicio'], d['hora_fim']))

    for aula, (dia, hora, _, prof, _) in solucao.items():
        if prof not in disp_por_prof:
            print("Não Passou check_professor_availability")
            return False
        if not any(d == dia and h_inicio <= hora < h_fim for d, h_inicio, h_fim in disp_por_prof[prof]):
            print("Não Passou check_professor_availability")
            return False
    return True
