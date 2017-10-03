from flask import jsonify
from flask import abort, Blueprint

from yab.models import Post

blag = Blueprint('blag', __name__, template_folder='templates', static_folder='static', static_url_path='/static/blag')

@blag.route('/posts')
def post_index():
    posts = Post.query.all()
    return jsonify({"status": True, "posts": [post.to_public_dict() for post in posts]})


@blag.route('/posts/<int:post_id>')
def post_show(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        return jsonify({"status": True, "post": post.to_public_dict()})
    else:
        return jsonify({"status": False})

