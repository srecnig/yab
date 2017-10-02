import pytest

from sqlalchemy.exc import IntegrityError

from yab.tests import ModelTest
from yab.models import db, Post


class PostTest(ModelTest):

    def test_title_must_exist(self):
        with pytest.raises(IntegrityError):
            post = Post(title=None, body="Some body")
            db.session.add(post)
            db.session.commit()

    def test_body_must_exist(self):
        with pytest.raises(IntegrityError):
            post = Post(title="Some title", body=None)
            db.session.add(post)
            db.session.commit()


    def test_published_at_default(self):
        post = Post(title="Some title", body="Some body", published_at=None)
        db.session.add(post)
        db.session.commit()
        assert post.published_at is not None
