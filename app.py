
import cherrypy
from flask import Flask

from app.controller import health_controller


def run_server() -> Flask:

    app = Flask(__name__)

    app.register_blueprint(health_controller)

    cherrypy.tree.graft(app, '/')
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 5000,
                            'engine.autoreload.on': False,
                            })

    return cherrypy.server.start()


if __name__ == '__main__':
    run_server()
