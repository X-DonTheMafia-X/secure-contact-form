from flask import (
    Flask,
    render_template
)
# Import Routes
from app.routes.main import main

# Import Config
from config import DevelopmentConfig

def create_app():

    app = Flask(__name__)

    # Setting app configurations
    app.config.from_object(DevelopmentConfig)

    # Register blueprints
    app.register_blueprint(main)

    return app