import flask
from flask_login import login_required
from flask import Blueprint


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def index():
    return 'admin page'


