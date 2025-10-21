import csv

def load_csv(path):
    """
    Carrega um ficheiro CSV e devolve uma lista de dicionários.
    """
    data = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def load_courses(path='dados/cursos.csv'):
    cursos = load_csv(path)
    for c in cursos:
        c['id'] = int(c['id'])
        c['n_turmas'] = int(c['n_turmas'])
    return cursos

def load_teachers(path='dados/professores.csv'):
    professores = load_csv(path)
    for p in professores:
        p['id'] = int(p['id'])
    return professores

def load_rooms(path='dados/salas.csv'):
    salas = load_csv(path)
    for s in salas:
        s['id'] = int(s['id'])
    return salas

def load_curricular_units(path='dados/unidades_curriculares.csv'):
    ucs = load_csv(path)
    seen = set()
    ucs_unique = []
    for u in ucs:
        if u['id'] not in seen:
            u['id'] = int(u['id'])
            u['curso_id'] = int(u['curso_id'])
            u['n_aulas_semana'] = int(u['n_aulas_semana'])
            ucs_unique.append(u)
            seen.add(u['id'])
    return ucs_unique

def load_availabilities(path='dados/disponibilidades.csv'):
    disp = load_csv(path)
    for d in disp:
        d['prof_id'] = int(d['prof_id'])
        d['hora_inicio'] = int(d['hora_inicio'])
        d['hora_fim'] = int(d['hora_fim'])
    return disp

def load_classes(path='dados/turmas.csv'):
    turmas = load_csv(path)
    seen = set()
    turmas_unique = []
    for t in turmas:
        if t['id'] not in seen:
            t['id'] = int(t['id'])
            t['curso_id'] = int(t['curso_id'])
            turmas_unique.append(t)
            seen.add(t['id'])
    return turmas_unique

def load_all():
    """
    Carrega todos os dados e devolve num único dicionário.
    """
    return {
        'cursos': load_courses(),
        'professores': load_teachers(),
        'salas': load_rooms(),
        'unidades_curriculares': load_curricular_units(),
        'turmas': load_classes(),
        'disponibilidades': load_availabilities()
    }

# Teste rápido
if __name__ == "__main__":
    dados = load_all()
    print("=== Cursos ===")
    for c in dados['cursos']:
        print(c)

    print("\n=== Professores ===")
    for p in dados['professores']:
        print(p)

    print("\n=== Salas ===")
    for s in [s['nome'] for s in dados['salas']]:
        print(s)

    print("\n=== Turmas ===")
    for t in dados['turmas']:
        print(t)

    print("\n=== Unidades Curriculares ===")
    for u in dados['unidades_curriculares']:
        print(u)

    print("\n=== Disponibilidades ===")
    for d in dados['disponibilidades']:
        print(d)
