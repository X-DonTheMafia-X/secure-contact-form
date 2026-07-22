from flask import (
    Flask,
    render_template
)
from app.routes.main import main

def create_app():

    app = Flask(__name__)
    
    app.register_blueprint(main)

    return app