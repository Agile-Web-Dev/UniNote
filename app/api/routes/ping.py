from flask import make_response

from . import bp


@bp.route("/ping", methods=["GET"])
def index():
    return make_response({"msg": "pong!"}, 200)
