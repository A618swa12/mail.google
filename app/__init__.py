from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret-key-for-dev'

    # import routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app