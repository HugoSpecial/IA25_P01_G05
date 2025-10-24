# Uma UC deve ocupar o menor número de dias distintos possível (idealmente 2)
def check_distinct_day_classes(*aulas):
    uc_days = {}
    for aula in aulas:
        dia, _, _, _, _, uc = aula
        uc_days.setdefault(uc, set()).add(dia)
    # penaliza UC com mais de 2 dias distintos
    return sum(len(dias) - 2 for dias in uc_days.values() if len(dias) > 2) == 0


# Uma turma deve ter aulas em no máximo 4 dias por semana
def check_weekly_days(*aulas):
    turma_days = {}
    for aula in aulas:
        dia, _, _, _, turma, _ = aula
        turma_days.setdefault(turma, set()).add(dia)
    return all(len(dias) <= 4 for dias in turma_days.values())


# As aulas num mesmo dia devem ser consecutivas (sem buracos entre horas)
def check_consecutive_classes(*aulas):
    dia_to_horas_turma = {}
    for aula in aulas:
        dia, hora, _, _, turma, _ = aula
        dia_to_horas_turma.setdefault((turma, dia), []).append(hora)

    def hora_to_int(h):
        # aceita "09:00", "9:00" ou inteiro 9
        if isinstance(h, int):
            return h * 60  # assume blocos de 1h
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
        # verifica se são consecutivas (intervalo de 60 min)
        for i in range(1, len(horas_ordenadas)):
            if horas_ordenadas[i] - horas_ordenadas[i-1] != 60:
                return False
    return True



# Uma turma deve usar o menor número de salas diferentes
def check_different_classes(*aulas):
    turma_salas = {}
    for aula in aulas:
        _, _, sala, _, turma, _ = aula
        turma_salas.setdefault(turma, set()).add(sala)
    # idealmente cada turma teria poucas salas — aqui verificamos <= 3
    return all(len(salas) <= 3 for salas in turma_salas.values())
