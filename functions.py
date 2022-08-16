import json

def load_candidates_from_json():
    '''загрузит данные из файла и покажет всех кандидатов'''
    with open('candidates.json', 'r', encoding="utf-8") as f:
        return json.load(f)

def get_candidates_by_id(id):
    'вернет кандидата по id'
    for item in load_candidates_from_json():
        if item['id'] == id:
            return item


def get_candidates_by_name(name):
    'вернет кандидата по имени'
    candidates = []
    for item in load_candidates_from_json():
        if item['name'] == name:
            candidates.append(item)
    return candidates


def get_candidates_by_skill(skill_name):
    '''вернет кандидатов по навыку'''
    candidates =[]
    for item in load_candidates_from_json():
        if skill_name in item['skills']:
            candidates.append(item)
    return candidates