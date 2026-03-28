from flask import Flask
from flask_wtf import CSRFProtect

from .extensions import db, login_manager

csrf = CSRFProtect()  # just create it here


def create_app():
    app = Flask(
        __name__,
        static_folder='../static',  # make sure path points to your project static/
        template_folder='../templates'
    )
    app.config.from_object("config.Config")

    csrf.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)  # <-- here
    # TODO replace this with auth.login
    login_manager.login_view = "home.index"  # redirect if not logged in
    login_manager.login_message_category = "info"

    from app.routes.home import home_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(home_bp)

    return app
