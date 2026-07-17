from flask import Flask
from .models import db, User
from flask_login import LoginManager

#erstellt die flask anwendung, verbindet datenbanken und loginsysteme
#und registriert blueprints damit flask weiß welche bereiche der webapp existieren


login_manager = LoginManager()

def create_app():
    app = Flask(__name__)


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travelmate.db"
    app.config["SECRET_KEY"] = "travelmate-secret-key"      #für flash messages, sessions, login sicherheit


    db.init_app(app)        #datenbank verbinden


    login_manager.init_app(app)               #verbindet login system mit flask
    login_manager.login_view = "auth.login"


    @login_manager.user_loader          #eingeloggten user in db finden
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from . import main
    from .auth import auth_bp
    from .trips import trips_bp             # blueprint aus trips.py importiert
    from .dashboard import dashboard_bp
    from .profile import profile_bp 
    from .application import applications_bp


    app.register_blueprint(main.bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(trips_bp)        #nach import registrieren damit flask sie erkennt und nutzen kann
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(applications_bp)

    return app