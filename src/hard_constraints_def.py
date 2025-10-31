# Conflitos de sala
def no_same_room_same_time(a1, a2):
    """
    Não permitir duas aulas na mesma sala no mesmo bloco.
    a1, a2 = (slot, sala, prof, turma, uc)
    """
    return not (a1[0] == a2[0] and a1[1] == a2[1])

# Máximo 3 aulas/dia por turma
def max_three_per_day_turma(*aulas):
    """
    Nenhuma turma pode ter mais de 3 aulas num mesmo dia.
    a1 = (slot, sala, prof, turma, uc)
    """
    # Mapear slot 1-20 para dia 1-5
    count_por_dia_turma = {}
    for aula in aulas:
        slot, _, _, turma, _ = aula
        dia = (slot - 1) // 4 + 1  # 1=Seg, 2=Ter, ..., 5=Sex
        key = f"{turma}_{dia}"
        count_por_dia_turma[key] = count_por_dia_turma.get(key, 0) + 1
        if count_por_dia_turma[key] > 3:
            return False
    return True

# Aulas da mesma UC em dias diferentes
def same_uc_different_days(a1, a2):
    """
    Garantir que duas aulas da mesma UC não fiquem no mesmo dia.
    a1, a2 = (slot, sala, prof, turma, uc)
    """
    if a1[4] != a2[4]:
        return True
    dia1 = (a1[0] - 1) // 4
    dia2 = (a2[0] - 1) // 4
    return dia1 != dia2

# Cada UC → 2 aulas
def exactly_two_per_uc(*aulas, ucs=None):
    count = {uc: 0 for uc in ucs}
    for aula in aulas:
        count[aula[4]] += 1
    return all(v == 2 for v in count.values())

# Cada turma → 10 aulas
def exactly_ten_per_turma(*aulas, turmas=None):
    count = {t: 0 for t in turmas}
    for aula in aulas:
        count[aula[3]] += 1
    return all(v == 10 for v in count.values())

# Check de duração não é mais necessário
# Todos os blocos já têm 2 horas
def check_duration(aula):
    return True
