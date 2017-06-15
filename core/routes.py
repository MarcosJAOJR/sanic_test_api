from sanic import Blueprint, response
from movies.controllers import get_movies

movies_bp = Blueprint('movies', url_prefix='/movies')

@movies_bp.get('/<category>')
async def handle_get_movies(request, category):
    '''Return movies of an especific category'''
    movies = get_movies(category)
    return response.json(movies, 200)
