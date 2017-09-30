from flask import Flask

from yab.blueprints.blag import blag


def create_app(config_object=None):
    app = Flask('yab')

    app.config.from_object(config_object)
    app.url_map.strict_slashes = False

    app.register_blueprint(blag)

    return app
