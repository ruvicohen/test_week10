from flask import Blueprint, request, jsonify
from app.repository.psql_repository.user_quote_repository import  \
    get_user_data_by_email
from app.service.messages_service import get_most_common_word
from app.service.producers import handle_producers

email_blueprint = Blueprint("email", __name__)

@email_blueprint.route("/", methods=["POST"])
def add_email():
    message = request.json
    handle_producers(message)
    return jsonify("info for email received"), 200

@email_blueprint.route("/<string:email>", methods=["GET"])
def get_by_email(email):
    res = get_user_data_by_email(email)
    if res is None:
        return jsonify("not found user by email"), 400
    return jsonify(res), 200

@email_blueprint.route("/common_word", methods=["GET"])
def get_common_word():
    common_word = get_most_common_word()
    if common_word is None:
        return jsonify("No data in db"), 400
    return jsonify(f'the common word is:{common_word}'), 200