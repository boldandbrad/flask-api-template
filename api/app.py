import os

import cherrypy
from flask import Flask

from api.controller import health_controller
from api.util import set_server_configs


def run_server():

    app = Flask(__name__)

    app.register_blueprint(health_controller)

    cherrypy.tree.graft(app, '/')
    # set_server_configs()

    config = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': int(os.environ.get('PORT', 5000)),
        }
    }

    cherrypy.config.update(config)

    cherrypy.server.start()


if __name__ == '__main__':
    run_server()
