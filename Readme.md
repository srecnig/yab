## yet another blag ##

### wat ###
this is yet another blag. well, not really actually – it's mostly a sample app to try out postgres, sqlalchemy, alembic and flask. it doesn't really a lot, but is a somewhat clean skeleton (i tried!) of how an actual app using this technologies could look.

### run ###
you need [Docker](https://www.docker.com) and [docker-compose](https://docs.docker.com/compose/) to run this (but thanks to docker, also nothing else). just go to `_` and run `docker-compose up`. developed and tested this on linux.

to enter the backend container, you'll have to call `./shell.sh` in `yab/backend`.

### migrations
we're using [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/), which utilizes [alembic](http://alembic.zzzcomputing.com/en/latest/) to do migrations. on first checking out the repository (or after changes have occured), enter the container and just call `flask db upgrade` - this will bring the database up to date.

when changing stuff in the models, call `flask db migrate`, alembic will create a migration file, you'll have to review it (e.g.: add indices you need, issue a rename of a column (alembic can't detect a rename – it will be shown as a drop and create) and then just call `flask db upgrade`, and you're done.


### tests
tests are run with [pytest](https://docs.pytest.org/en/latest/). just enter the container and run `pytest` in `/backend`. at the moment there's a few samples for model tests, but controller and lib tests should be somewhat similar.


### playground ###
postgresql allows storing arbitrary json data in its's tables (in this example, post has a `meta` field, and it can easily be queried again:

```
from yab.models import db
from yab.models import Post

# create a post with metadata
post = Post(title="with meta", body="such metadata, weeeeee", meta={"custom_1": "such value", "custom_2": "many wow" })
db.session.add(a)

# query for that
Post.query.filter(Post.meta["custom_1"].astext == 'such value').all()
```

### blag? ###
yeah, yeah, of course i can't come up with my own [jokes](https://xkcd.com/148/).
