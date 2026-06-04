from flask import Flask
from .models import db, User
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travelmate.db"
    app.config["SECRET_KEY"] = "travelmate-secret-key"


    db.init_app(app)


    login_manager.init_app(app)
    login_manager.login_view = "auth.login"


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from . import main
    from .auth import auth_bp
    from .trips import trips_bp

    app.register_blueprint(main.bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(trips_bp)

    return app
