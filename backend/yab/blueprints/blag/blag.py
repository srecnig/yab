from flask import abort, Blueprint

from yab.models import Post

blag = Blueprint('blag', __name__, template_folder='templates', static_folder='static', static_url_path='/static/blag')

@blag.route('/')
@blag.route('/posts')
def post_index():
    posts = Post.query.all()
    return 'welcome to my blag: %r' % [p.title for p in posts]


@blag.route('/posts/<int:post_id>')
def post_show(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        return 'i am the post: %r, here\'s my content: %r' % (post.title, post.body)
    else:
        abort(404)
