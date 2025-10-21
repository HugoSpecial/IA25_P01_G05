# Conflitos de sala
def no_same_room_same_time(a1, a2):
    return not (a1[0]==a2[0] and a1[1]==a2[1] and a1[2]==a2[2])

# Máximo 3 aulas/dia por turma
def max_three_per_day_turma(*aulas):
    count_por_dia_turma = {}
    for aula in aulas:
        dia, _, _, _, turma, _ = aula
        key = f"{turma}_{dia}"
        count_por_dia_turma[key] = count_por_dia_turma.get(key,0)+1
        if count_por_dia_turma[key]>3: return False
    return True

# Aulas da mesma UC em dias diferentes
def same_uc_different_days(a1,a2):
    return a1[0] != a2[0] if a1[5]==a2[5] else True

# Cada UC → 2 aulas
def exactly_two_per_uc(*aulas, ucs=None):
    count = {uc:0 for uc in ucs}
    for aula in aulas:
        count[aula[5]] += 1
    return all(v==2 for v in count.values())

# Cada turma → 10 aulas
def exactly_ten_per_turma(*aulas, turmas=None):
    count = {t:0 for t in turmas}
    for aula in aulas:
        count[aula[4]] += 1
    return all(v==10 for v in count.values())
