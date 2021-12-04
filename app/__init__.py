from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # TODO: will store this key safely later & change it!
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "development_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    # app.config[
    # "SQLALCHEMY_DATABASE_URI"
    # ] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    # user=os.getenv("POSTGRES_USER"),
    # passwd=os.getenv("POSTGRES_PASSWORD"),
    # host=os.getenv("POSTGRES_HOST"),
    # port=5432,
    # table=os.getenv("POSTGRES_DB"),
    # )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # migrate = Migrate(app, db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")

    from .models import User, Cert, Tag

    create_database(app)

    # take care of the authentication
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("app" + DB_NAME):
        db.create_all(app=app)
        print("Database initialized!")
