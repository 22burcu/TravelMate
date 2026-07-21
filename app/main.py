from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

''' quellen
youtube run flask app run render template       https://www.youtube.com/watch?v=-5JocHM6QY0
youtube understanding routes in flask           https://www.youtube.com/watch?v=jF3wxBzP6H0
blueprint erstellen                             https://flask.palletsprojects.com/en/3.0.x/blueprints/
route definieren                                https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.route
GET methode                                     https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET
render_template html anzeigen                   https://flask.palletsprojects.com/en/3.0.x/api/#flask.render_template
'''