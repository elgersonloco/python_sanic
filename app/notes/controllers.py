from sanic import Blueprint
from sanic.response import json

bp_notes = Blueprint('notes', url_prefix='/notes')


@bp_notes.get('/')
async def test(request):
    return json({"hello": "world"})
