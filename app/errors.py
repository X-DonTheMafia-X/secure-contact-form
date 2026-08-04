from flask import render_template
from app.logging_config import logger

def register_general_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(error):
        logger.warning(
            "404 Page Not Found"
        )

        return (
            render_template("errors/404.html"),
            404
        )
    @app.errorhandler(500)
    def internal_server_error(error):
        logger.exception(
            "Unhandled application exception"
        )

        return (
            render_template("errors/500.html"),
            500
        )
