from flask import (
    Flask,
    render_template
    )

# Import Logging Config
import app.logging_config

# Import Routes
from app.routes.main import main
from app.routes.auth import auth
from app.routes.admin import admin

# Import Error Handler
from app.errors import register_general_error_handlers
from app.routes.errors import register_rate_limit_error_handlers

# Import Config
from config import DevelopmentConfig

# Import Extentions
from app.extensions import (
    db,
    login_manager,
    migrate,
    csrf,
    mail,
    limiter
)
# Import Security Headers
from app.security.headers import add_security_headers

# Import Models
import app.models

# Import User Model
from app.models.user import User

def create_app():

    # Create app
    app = Flask(__name__)

    # Load configurations
    app.config.from_object(DevelopmentConfig)

    # Initialize Extentions
    db.init_app(app)
    login_manager.init_app(app)
    limiter.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    



    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    

    # Register error handler blueprints
    register_general_error_handlers(app)
    register_rate_limit_error_handlers(app)
    

    # Create User Loader for Authorization
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @app.after_request
    def apply_security_headers(response):

        return add_security_headers(response)


    return app