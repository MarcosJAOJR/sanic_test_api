from sanic import Sanic
from .routes import movies_bp

app = Sanic()
app.blueprint(movies_bp)
