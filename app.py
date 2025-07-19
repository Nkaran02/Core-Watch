import os
import webbrowser
import threading
from flask import Flask
from extensions import db

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from auth import auth_routes
        from system import system_routes

        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(system_routes.system_bp)

    return app

app = create_app()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(0.5, open_browser).start()
    app.run(debug=False)
