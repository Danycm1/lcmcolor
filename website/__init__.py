from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.ProductionConfig")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from website.routes.views import views

    app.register_blueprint(views, url_prefix="/")

    login_manager = LoginManager()
    login_manager.login_view = "views.login"
    login_manager.init_app(app)

    from website.database.models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
