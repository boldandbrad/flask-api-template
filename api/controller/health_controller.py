
from json import dumps

from flask import Blueprint, Response

health_controller = Blueprint('health_controller', __name__)


@health_controller.route('/')
def health_check() -> Response:
    return Response(dumps({'status': 'healthy'}), status=200, mimetype='application/json')
