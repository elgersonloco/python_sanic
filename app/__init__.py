import aiohttp
from sanic import Sanic
from app.notes.controllers import bp_notes
from app.wit_ai.controllers import bp_wit

app = Sanic()


@app.listener('before_server_start')
async def setup_blueprint(_app, _loop):
    _app.blueprint(bp_notes)
    _app.blueprint(bp_wit)


@app.listener('before_server_start')
async def setup_http_client(_app, _loop):
    _app.http_session = aiohttp.ClientSession(loop=_loop)


@app.listener('after_server_stop')
async def stop_http_client(_app, _loop):
    _app.http_session.close()
