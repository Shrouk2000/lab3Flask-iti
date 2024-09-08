# app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.config import config_options
from app.posts import posts_blueprint

def create_app(config_name="prd"):
    app = Flask(__name__)

    # Load configuration
    current_config = config_options.get(config_name, config_options["prd"])
    app.config.from_object(current_config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(posts_blueprint)

    return app
