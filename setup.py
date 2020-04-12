
import os

from setuptools import setup

from api import __description__, __title__, __version__


def get_file_contents(file_path: str) -> str:
    """
    Return contents of a file
    :param file_path:
    :return: contents of file
    """

    with open(os.path.join(HERE, file_path), encoding='utf-8') as f:
        contents = f.read()

    return contents


HERE = os.path.abspath(os.path.dirname(__file__))
REQUIRES = [
    'cherrypy',
    'flask',
    'marshmallow'
]

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=get_file_contents('README.md'),
    author='Bradley Wojcik',
    install_requires=REQUIRES,
    include_package_data=True,
    license=get_file_contents('LICENSE'),
    python_requires='>=3.0'
)
