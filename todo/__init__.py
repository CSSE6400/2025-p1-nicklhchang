from flask import Flask

def create_app():
    # poetry run flask --app todo run -p 6400
    app = Flask(__name__)

    from .views.routes import api
    app.register_blueprint(api)

    return app
