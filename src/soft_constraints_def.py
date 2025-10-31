# Cada UC não deve ter aulas em mais de 2 dias diferentes
def check_distinct_day_classes(*aulas):
    uc_days = {}
    for aula in aulas:
        dia, _, _, _, _, uc = aula  
        uc_days.setdefault(uc, set()).add(dia)
    return sum(len(dias) - 2 for dias in uc_days.values() if len(dias) > 2) == 0


# Cada turma não deve ter aulas em mais de 4 dias por semana
def check_weekly_days(*aulas):
    turma_days = {}
    for aula in aulas:
        dia, _, _, _, turma, _ = aula
        turma_days.setdefault(turma, set()).add(dia)
    return all(len(dias) <= 4 for dias in turma_days.values())


# Aulas de uma mesma turma num mesmo dia devem ser consecutivas (cada aula = 2h)
def check_consecutive_classes(*aulas):
    turma_dia_horas = {}
    for aula in aulas:
        dia, hora, _, _, turma, _ = aula
        turma_dia_horas.setdefault((turma, dia), []).append(hora)

    for horas in turma_dia_horas.values():
        horas_ordenadas = sorted(horas)
        for i in range(1, len(horas_ordenadas)):
            if horas_ordenadas[i] - horas_ordenadas[i-1] != 2:
                return False
    return True


# Cada turma deve usar no máximo 3 salas diferentes
def check_different_classes(*aulas):
    turma_salas = {}
    for aula in aulas:
        _, _, sala, _, turma, _ = aula
        turma_salas.setdefault(turma, set()).add(sala)
    return all(len(salas) <= 3 for salas in turma_salas.values())
