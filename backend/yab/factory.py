from flask import Flask

def create_app(config_object=None):
    app = Flask('yab')

    app.config.from_object(config_object)
    app.url_map.strict_slashes = False

    from yab.blueprints.blag import blag
    app.register_blueprint(blag)

    from yab.model import db
    db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate()
    migrate.init_app(app, db)

    return app
