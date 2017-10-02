import datetime

import factory

import yab.models


class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = yab.models.Post

    title = factory.Faker('sentence', nb_words=4)
    body = factory.Faker('paragraphs', nb=4)
    published_at = datetime.datetime.utcnow()

