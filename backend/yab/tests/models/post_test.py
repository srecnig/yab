import pytest

from sqlalchemy.exc import IntegrityError

from yab.models import db, Post
from yab.tests import ModelTest
from yab.tests.factories import PostFactory


class PostTest(ModelTest):

    # validations

    def test_title_must_exist(self):
        with pytest.raises(IntegrityError):
            post = PostFactory.build(title=None)
            db.session.add(post)
            db.session.commit()

    def test_body_must_exist(self):
        with pytest.raises(IntegrityError):
            post = PostFactory.build(body=None)
            db.session.add(post)
            db.session.commit()

    def test_published_at_default(self):
        post = PostFactory.build(published_at=None)
        db.session.add(post)
        db.session.commit()
        assert post.published_at is not None

    # other

    def test_public_dict_must_not_contain_meta(self):
        post = PostFactory.build()
        db.session.add(post)
        db.session.commit()

        post_dict = post.to_public_dict()
        assert post_dict.get("title") is not None
        assert post_dict.get("body") is not None
        assert post_dict.get("published_at") is not None
        assert post_dict.get("meta") is None

