""" API Endpoint to Run the Bot... """

# Python Packages
from flask import Blueprint, request, jsonify

# Services
from app.services.llama_service import get_query_engine

# Blueprint
query_bp = Blueprint("query", __name__)





@query_bp.route("/")
def hello():
    return "PersonalDocBot is running 🚀"


@query_bp.route("/api/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        question = data.get("question")

        if not question:
            return jsonify({"error": "Question is required"}), 400

        query_engine = get_query_engine()

        response = query_engine.query(question)

        return jsonify({"response": str(response)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
