from flask import Blueprint, request, jsonify
from app.repository.psql.user_quote_repository import get_user_quote_with_all_by_email
from app.service.producers import produce_user_quote, handle_producers

email_blueprint = Blueprint("email", __name__)


@email_blueprint.route("/", methods=["POST"])
def add_email():
    message = request.json
    handle_producers(message)
    return jsonify("info for email received"), 200

@email_blueprint.route("/<email>", methods=["POST"])
def get_by_email(email):
    res = get_user_quote_with_all_by_email(email)
    return jsonify(res), 200