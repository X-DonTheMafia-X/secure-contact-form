from flask import(
    render_template
)

from werkzeug.exceptions import TooManyRequests

def register_rate_limit_error_handlers(app):

    @app.errorhandler(TooManyRequests)
    def too_many_requests(error):

        return (
            render_template("errors/429.html"),429
        )