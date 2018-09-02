#!/usr/bin/venv python
# **************************************************************************
#
# **************************************************************************

from flask import Flask
import config
from app.views import accountviews, adminviews, postviews
from flask import current_app
# from app.extension import db, cache, search
# from app.api.user.models import User

import click
import os
import sys

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(adminviews.bp)
app.register_blueprint(postviews.post_bp)
app.register_blueprint(accountviews.account_bp)


# cli = FlaskGroup(add_default_commands=False, create_app=lambda r: app)
# cli.add_command(run_command)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        app.run('0.0.0.0', 5000)
    else:
        pass
        # cli.main()
