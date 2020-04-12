
from json import dumps

from flask import Blueprint, Response

from api.__version__ import __description__, __title__, __version__

health_controller = Blueprint('health_controller', __name__)


@health_controller.route('/')
def health_check() -> Response:
    """
    Check the current status of the api
    :return:
    """

    api_status = {
        'service': __title__,
        'description': __description__,
        'version': __version__,
        'status': 'healthy'
    }

    return Response(dumps(api_status), status=200, mimetype='application/json')
