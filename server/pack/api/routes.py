from flask import Blueprint

mod = Blueprint('api', __name__)


@mod.route('/turnmotor')
def turnmotor():
    return "{'result': 'Hello world' }"
