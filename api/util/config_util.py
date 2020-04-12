import os

import cherrypy


def set_server_configs() -> None:
    """
    Set cherrypy server configurations
    :return: None
    """
    cherrypy.config.update(_get_conf_for_env('global'))


def _get_conf_for_env(env: str) -> str:
    """
    Locate config file for given env
    :param env: environment config to locate
    :return: config file path
    :raise FileNotFoundError: config file cannot be located
    """

    print('Loading configs for', env, 'profile')

    this_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.split(this_dir)[0]
    conf_file_path = parent_dir + '/config/' + env + '.conf'

    if not os.path.isfile(conf_file_path):
        raise FileNotFoundError('No valid config file found for given env ', env)

    return conf_file_path
