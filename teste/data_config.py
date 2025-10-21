from itertools import product
from load import *
dados = load_all()
# Dias, horas, salas, turmas, UCs e professores
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
horas = [9, 11, 14, 16]
salas = [s['nome'] for s in dados['salas']] # Mostra apenas o nome das salas
turmas = [s['id'] for s in dados['turmas']] # Só está a funcionar com id
# ucs = [s['id'] for s in dados['unidades_curriculares']]
ucs = list(range(1,11))
professores = [1, 2, 3, 4, 5]

# UC → Turma
uc_to_turma = {1:1,2:1,3:1,4:1,5:1,6:2,7:2,8:2,9:2,10:2}

# UC → Professor
uc_to_professor = {1:1,2:2,3:3,4:4,5:5,6:1,7:2,8:3,9:4,10:5}

# Disponibilidade de professores
disponibilidades = [
    # Prof 1
    {"prof_id": 1, "dia": "Segunda", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 1, "dia": "Terça", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 1, "dia": "Quarta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 1, "dia": "Quinta", "hora_inicio": 8, "hora_fim": 18},
    # Prof 2
    {"prof_id": 2, "dia": "Segunda", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 2, "dia": "Terça", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 2, "dia": "Quarta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 2, "dia": "Sexta", "hora_inicio": 8, "hora_fim": 18},
    # Prof 3
    {"prof_id": 3, "dia": "Segunda", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 3, "dia": "Terça", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 3, "dia": "Quarta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 3, "dia": "Quinta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 3, "dia": "Sexta", "hora_inicio": 8, "hora_fim": 18},
    # Prof 4
    {"prof_id": 4, "dia": "Segunda", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 4, "dia": "Quarta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 4, "dia": "Quinta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 4, "dia": "Sexta", "hora_inicio": 8, "hora_fim": 18},
    # Prof 5
    {"prof_id": 5, "dia": "Segunda", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 5, "dia": "Terça", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 5, "dia": "Quarta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 5, "dia": "Quinta", "hora_inicio": 8, "hora_fim": 18},
    {"prof_id": 5, "dia": "Sexta", "hora_inicio": 8, "hora_fim": 18},
]

# Horários disponíveis por professor
def horarios_disponiveis(prof_id):
    disponiveis = []
    for d, h in product(dias, horas):
        for disp in disponibilidades:
            if disp['prof_id']==prof_id and disp['dia']==d and disp['hora_inicio']<=h<disp['hora_fim']:
                disponiveis.append((d,h))
                break
    return disponiveis
