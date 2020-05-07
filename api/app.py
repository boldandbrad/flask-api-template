import cherrypy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.controller import health_controller
from api.util import set_server_configs


def run_server() -> Flask:

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://localhost/postgres'
    db = SQLAlchemy(app)

    app.register_blueprint(health_controller)

    cherrypy.tree.graft(app, '/')
    set_server_configs()

    return cherrypy.server.start()


if __name__ == '__main__':
    run_server()
