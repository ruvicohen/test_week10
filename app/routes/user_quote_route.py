from flask import Blueprint, request, jsonify
from app.repository.psql_repository.user_quote_repository import get_user_quote_with_all_by_email
from app.service.messages_service import get_most_common_word
from app.service.producers import handle_producers

email_blueprint = Blueprint("email", __name__)

@email_blueprint.route("/", methods=["POST"])
def add_email():
    message = request.json
    handle_producers(message)
    return jsonify("info for email received"), 200

@email_blueprint.route("/<string:email>", methods=["POST"])
def get_by_email(email):
    res = get_user_quote_with_all_by_email(email)
    return jsonify(res), 200

@email_blueprint.route("/common_word", methods=["GET"])
def get_common_word():
    common_word = get_most_common_word()
    return jsonify(common_word), 200