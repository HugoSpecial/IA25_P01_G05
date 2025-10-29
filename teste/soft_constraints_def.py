def check_distinct_day_classes(*aulas):
    uc_days = {}
    for aula in aulas:
        dia, _, _, _, _, uc = aula
        uc_days.setdefault(uc, set()).add(dia)
    return sum(len(dias) - 2 for dias in uc_days.values() if len(dias) > 2) == 0

def check_weekly_days(*aulas):
    turma_days = {}
    for aula in aulas:
        dia, _, _, _, turma, _ = aula
        turma_days.setdefault(turma, set()).add(dia)
    return all(len(dias) <= 4 for dias in turma_days.values())

def check_consecutive_classes(*aulas):
    dia_to_horas_turma = {}
    for aula in aulas:
        dia, hora, _, _, turma, _ = aula
        dia_to_horas_turma.setdefault((turma, dia), []).append(hora)

    def hora_to_int(h):
        if isinstance(h, int):
            return h * 60
        elif isinstance(h, str):
            partes = h.split(':')
            if len(partes) == 2:
                hh, mm = map(int, partes)
                return hh * 60 + mm
            else:
                return int(h) * 60
        else:
            raise ValueError(f"Formato de hora inesperado: {h}")

    for (turma, dia), horas in dia_to_horas_turma.items():
        horas_ordenadas = sorted(hora_to_int(h) for h in horas)
        for i in range(1, len(horas_ordenadas)):
            if horas_ordenadas[i] - horas_ordenadas[i-1] != 60:
                return False
    return True

def check_different_classes(*aulas):
    turma_salas = {}
    for aula in aulas:
        _, _, sala, _, turma, _ = aula
        turma_salas.setdefault(turma, set()).add(sala)
    return all(len(salas) <= 3 for salas in turma_salas.values())

