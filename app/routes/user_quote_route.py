from flask import Blueprint, request, jsonify

from app.service.producers import produce_user_quote, handle_producers

email_blueprint = Blueprint("email", __name__)


@email_blueprint.route("/", methods=["POST"])
def add_email():
    message = request.json
    handle_producers(message)
    return jsonify("info for email received"), 200