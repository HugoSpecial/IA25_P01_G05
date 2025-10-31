def load_data_txt(path='dados/data.txt'):
    data = {
        'classes': {},           # #cc — cursos atribuídos a turmas
        'one_lesson_week': [],   # #olw — cursos com apenas uma aula/semana
        'teachers': {},          # #dsd — professores e UCs atribuídas
        'time_restrictions': {}, # #tr — restrições de horários (NÃO disponíveis)
        'room_restrictions': {}, # #rr — restrições de salas
        'online_classes': {},    # #oc — aulas online
        'time_availabilities': {} # calculadas automaticamente (disponíveis)
    }

    current_section = None

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('—') or line.startswith('#head'):
                continue

            # Identificar secções
            if line.startswith('#'):
                if line.startswith('#cc'):
                    current_section = 'classes'
                elif line.startswith('#olw'):
                    current_section = 'one_lesson_week'
                elif line.startswith('#dsd'):
                    current_section = 'teachers'
                elif line.startswith('#tr'):
                    current_section = 'time_restrictions'
                elif line.startswith('#rr'):
                    current_section = 'room_restrictions'
                elif line.startswith('#oc'):
                    current_section = 'online_classes'
                else:
                    current_section = None
                continue

            parts = line.split()
            if not parts:
                continue

            if current_section == 'classes':
                turma = parts[0]
                ucs = parts[1:]
                data['classes'][turma] = ucs

            elif current_section == 'one_lesson_week':
                data['one_lesson_week'].append(parts[0])

            elif current_section == 'teachers':
                professor = parts[0]
                ucs = parts[1:]
                data['teachers'][professor] = ucs

            elif current_section == 'time_restrictions':
                professor = parts[0]
                not_available = [int(x) for x in parts[1:]]
                data['time_restrictions'][professor] = not_available

            elif current_section == 'room_restrictions':
                uc, sala = parts
                data['room_restrictions'][uc] = sala

            elif current_section == 'online_classes':
                uc, idx = parts
                data['online_classes'][uc] = int(idx)

    # Converter restrições em disponibilidades para todos os professores
    all_slots = set(range(1, 21))  # 20 blocos (5 dias × 4 blocos)
    for prof in data['teachers'].keys():  # garantir todos os professores
        unavailable = data['time_restrictions'].get(prof, [])  # se não tiver, assume []
        available = sorted(all_slots - set(unavailable))
        data['time_availabilities'][prof] = available

    return data


if __name__ == "__main__":
    dados = load_data_txt()

    print("=== Professores e UCs ===")
    for prof, ucs in dados['teachers'].items():
        print(f"{prof}: {ucs}")

    print("\n=== Slots indisponíveis ===")
    for prof, slots in dados['time_restrictions'].items():
        print(f"{prof}: {slots}")

    print("\n=== Slots disponíveis ===")
    for prof, slots in dados['time_availabilities'].items():
        print(f"{prof}: {slots}")
