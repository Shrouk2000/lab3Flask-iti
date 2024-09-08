
from flask import Blueprint

posts_blueprint = Blueprint("posts", __name__, url_prefix="/posts")

# Import views to register routes with the blueprint
from app.posts import views
