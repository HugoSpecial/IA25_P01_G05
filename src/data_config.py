from itertools import product
from load import load_data_txt

# Carregar dados
dados = load_data_txt('dados/data.txt')

# Turmas e UCs
turmas = list(dados['classes'].keys())  # Ex.: ['t01', 't02', 't03']
ucs = [uc for ucs_list in dados['classes'].values() for uc in ucs_list]

# Professores
professores = list(dados['teachers'].keys())  # Ex.: ['jo', 'mike', 'rob', 'sue']

# Salas (podes adicionar mais se necessário)
salas = ['Lab01', 'Lab02', 'Lab03', 'Lab04']

# UC → Turma
uc_to_turma = {}
for t, ucs_list in dados['classes'].items():
    for uc in ucs_list:
        uc_to_turma[uc] = t

# UC → Professores (uma UC pode ter mais que um professor)
uc_to_professor = {}
for prof, ucs_list in dados['teachers'].items():
    for uc in ucs_list:
        uc_to_professor.setdefault(uc, []).append(prof)

# Disponibilidades dos professores (slots 1–20)
disponibilidades = dados['time_availabilities']

# Função para obter slots disponíveis de um professor
def horarios_disponiveis(prof):
    return disponibilidades.get(prof, [])

# Teste rápido
if __name__ == "__main__":
    print("=== TURMAS ===", turmas)
    print("=== UCs ===", ucs)
    print("=== PROFESSORES ===", professores)
    print("=== UC → TURMA ===", uc_to_turma)
    print("=== UC → PROFESSOR ===", uc_to_professor)
    print("=== DISPONIBILIDADES ===")
    for prof, slots in disponibilidades.items():
        print(f"{prof}: {slots}")
