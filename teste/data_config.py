from itertools import product
from load import *

dados = load_all()

# Configuração básica
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
horas = [9, 11, 14, 16]
salas = [s['nome'] for s in dados['salas']]
turmas = [t['id'] for t in dados['turmas']]
ucs = [uc['id'] for uc in dados['unidades_curriculares']]
professores = [p['id'] for p in dados['professores']]

uc_to_turma = {}
uc_to_professor = {}

# Distribuir UCs pelas turmas
for i, uc in enumerate(dados['unidades_curriculares']):
    uc_id = uc['id']
    # Alternar entre turmas (0 → turma1, 1 → turma2, etc.)
    turma_index = i % len(turmas)
    uc_to_turma[uc_id] = turmas[turma_index]
    
    # Distribuir professores
    prof_index = i % len(professores)
    uc_to_professor[uc_id] = professores[prof_index]

# Disponibilidades do CSV
disponibilidades = dados['disponibilidades']

def horarios_disponiveis(prof_id):
    disponiveis = []
    for d, h in product(dias, horas):
        for disp in disponibilidades:
            if (disp['prof_id'] == prof_id and 
                disp['dia'] == d and 
                disp['hora_inicio'] <= h < disp['hora_fim']):
                disponiveis.append((d, h))
                break
    return disponiveis