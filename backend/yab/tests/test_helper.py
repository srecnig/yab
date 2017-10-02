from flask_testing import TestCase

from yab.factory import create_app
from yab.models import db

class BaseTest(TestCase):
    def create_app(self):
        return create_app("yab.config.test.Config")


    def setUp(self):
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


class ModelTest(BaseTest):
    pass

class BlueprintTest(BaseTest):
    def create_app(self):
        app = create_app("yab.config.test.Config")
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        return app
