import json

def get_movies(category):
    return json.dumps({"title": "A Lenda do Tesouro Perdido", "category": category}, ensure_ascii=False)