from flask import Blueprint

blag = Blueprint('blag', __name__, template_folder='templates', static_folder='static', static_url_path='/static/blag')

@blag.route('/')
def root_index():
    return "welcome to my blag"


@blag.route('/posts/<int:post_id>')
def post_show(post_id):
	return "i am a post: %r" % post_id

