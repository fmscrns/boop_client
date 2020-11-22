from flask import Flask, render_template
from .config import config_by_name
from .util.decorator import no_session_required

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    @app.route("/", methods=["GET", "POST"])
    @app.route("/welcome", methods=["GET", "POST"])
    @no_session_required
    def welcome():
        
        return render_template("welcome.html", page_title="Welcome")

    return app