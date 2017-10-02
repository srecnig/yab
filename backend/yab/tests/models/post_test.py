import pytest

from sqlalchemy.exc import IntegrityError

from yab.tests import ModelTest
from yab.models import db, Post


class PostTest(ModelTest):

    # validations

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

    # other

    def test_public_dict_must_not_contain_meta(self):
        post = Post(title="Some title", body="Some body")
        db.session.add(post)
        db.session.commit()

        post_dict = post.to_public_dict()
        assert post_dict.get("title") == "Some title"
        assert post_dict.get("body") == "Some body"
        assert post_dict.get("published_at") is not None
        assert post_dict.get("meta") is None

