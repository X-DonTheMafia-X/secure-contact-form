from flask import (
    Flask,
    render_template
    )

# Import Logging Config
import app.logging_config

# Import Routes
from app.routes.main import main

# Import Error Handler
from app.errors import register_error_handlers

# Import Config
from config import DevelopmentConfig


# Import Extentions
from app.extensions import (
    db,
    migrate,
    csrf,
    mail,
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
    mail.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)


    # Register blueprints
    app.register_blueprint(main)

    # Register error handler blueprints
    register_error_handlers(app)

    

    return app