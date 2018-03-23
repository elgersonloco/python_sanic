from sanic import Blueprint
from sanic.exceptions import ServerError
from sanic.response import json

bp_wit = Blueprint('wit', url_prefix='/wit')


@bp_wit.get('/')
async def test(request):
    async with request.app.http_session.get('https://api.wit.ai/message',
                                            headers={"Authorization": "Bearer BHNZJKZBCDRCQ6KMGWSPAQXC4AR3IBRP"},
                                            params={"q": request.args["q"][0]}) as response:
        data = await response.json()

    return json(data)


@bp_wit.get('/perro')
async def test_excpetion(request):
    raise ServerError('Valio verga', status_code=500)
