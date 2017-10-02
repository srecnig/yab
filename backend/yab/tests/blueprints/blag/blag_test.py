from faker import Faker

from yab.models import db, Post
from yab.tests import BlueprintTest
from yab.tests.factories import PostFactory


class PostTest(BlueprintTest):
    def test_get_root_index(self):
        self._create_posts()
        response = self.client.get("/")
        assert response.status_code == 200

    def test_get_index(self):
        self._create_posts()
        response = self.client.get("/posts")
        assert response.status_code == 200

    def test_get_show(self):
        self._create_posts()
        response = self.client.get("/posts/%s" % self.post_a.id)
        assert response.status_code == 200

    def test_get_show_returns_404(self):
        response = self.client.get("/posts/1")
        assert response.status_code == 404


    def _create_posts(self):
        self.post_a = PostFactory.build()
        self.post_b = PostFactory.build()

        db.session.add(self.post_a)
        db.session.add(self.post_b)
        db.session.commit()
