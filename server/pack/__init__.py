from flask import Flask
from main.routes import mod

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

app.register_blueprint(mod, url_prefix='/home')