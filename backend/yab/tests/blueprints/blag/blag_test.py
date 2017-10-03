import json

from faker import Faker

from yab.models import db, Post
from yab.tests import BlueprintTest
from yab.tests.factories import PostFactory


class PostTest(BlueprintTest):
    def test_get_index(self):
        self._create_posts()
        response = self.client.get("/posts")
        assert response.status_code == 200
        assert response.content_type == "application/json"

    def test_get_show(self):
        self._create_posts()
        response = self.client.get("/posts/%s" % self.post_a.id)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert response.content_type == "application/json"
        assert data["status"] is True


    def test_get_show_returns_false(self):
        response = self.client.get("/posts/1")
        data = json.loads(response.data)
        assert response.status_code == 200
        assert response.content_type == "application/json"
        assert data["status"] is False

    def _create_posts(self):
        self.post_a = PostFactory.build()
        self.post_b = PostFactory.build()

        db.session.add(self.post_a)
        db.session.add(self.post_b)
        db.session.commit()

