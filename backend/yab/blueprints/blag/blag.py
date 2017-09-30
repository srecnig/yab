from flask import Blueprint

from yab.model import Post

blag = Blueprint('blag', __name__, template_folder='templates', static_folder='static', static_url_path='/static/blag')

@blag.route('/')
@blag.route('/posts')
def root_index():
    posts = Post.query.all()
    return "welcome to my blag: %s" % posts


@blag.route('/posts/<int:post_id>')
def post_show(post_id):
    post = Post.query.filter_by(id='post_id').first()
    return "i am a post: %r" % post
