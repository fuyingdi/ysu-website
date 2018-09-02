from flask import Blueprint, views
import flask
from flask_login import login_required

account_bp = Blueprint('account', __name__, url_prefix='/account')


@account_bp.route('/')
def index():
    return 'account index'


@account_bp.route('/settings/')
@login_required
def settings():
    pass


@account_bp.route('/settings/mail_captcha')
def mail_captcha():
    # 用于发送验证码
    pass


@account_bp.route('profile/<user_id>')
@login_required
def profile_posts():
    # 资料详情页
    pass


@account_bp.route('/graph_captcha/')
def graph_captcha():
    # 生成图形验证码
    pass


@account_bp.route('/logout/')
@login_required
def logout():
    # 登出
    return flask.redirect(flask.url_for('post.index'))

