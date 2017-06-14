from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def hello(req):
    return json({"hello": "world"})

@app.websocket('/feed')
async def feed(req, ws):
    while True:
        data = 'hello!'
        print('Sending: %s'%data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: %s'%data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
