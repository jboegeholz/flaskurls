from flask import Blueprint
bp1 = Blueprint('bp1', __name__)


@bp1.route('/bp1')
def index():
    return "Hello from bp1_index"
