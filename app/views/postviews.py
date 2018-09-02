from flask import Blueprint
import flask
from flask import redirect, url_for
from flask_login import login_required

post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route('/')
def index():
    return 'postviews'


@post_bp.route('/add_post/')
@login_required
def add_post():
    # 发帖
    pass


@post_bp.route('/add_comment/')
@login_required
def add_comment():
    pass


