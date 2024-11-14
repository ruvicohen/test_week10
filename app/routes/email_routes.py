from flask import Blueprint, request, jsonify

from app.service.producers import produce_new_email

email_blueprint = Blueprint("email", __name__)


@email_blueprint.route("/", methods=["POST"])
def add_email():
    email = request.json
    produce_new_email(email)
    return jsonify("info for email received"), 200