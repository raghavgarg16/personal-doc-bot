"""
Application factory
"""

# Python Packages
from flask import Flask
from flask_cors import CORS

# Routes
from app.routes.query_routes import query_bp

# Services
from app.services.llama_service import init_llama





def create_app():
    """
    Application Factory
    """

    app = Flask(__name__)
    app.config["DEBUG"] = True

    # Enable CORS
    CORS(app)

    # Initialize Llama Index (load documents + create index)
    init_llama()

    # Register Blueprints
    app.register_blueprint(query_bp)

    return app
