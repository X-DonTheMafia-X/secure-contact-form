from flask import (
    Flask,
    render_template
)
# Import Routes
from app.routes.main import main

# Import Config
from config import DevelopmentConfig

# Import Extentions
from app.extensions import (
    db,
    migrate,
    csrf
)

# Import app models for database
import app.models

def create_app():

    # Create app
    app = Flask(__name__)

    # Load configurations
    app.config.from_object(DevelopmentConfig)

    # Initialize Extentions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Register blueprints
    app.register_blueprint(main)

    

    return app