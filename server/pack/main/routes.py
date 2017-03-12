from flask import Blueprint

mod = Blueprint('main', __name__)

@mod.route('/')
def homepage():
    return "<h1>Welcome to Flask</h1>"
