from flask import make_response

from . import bp


@bp.route("/ping", methods=["GET"])
def ping():
    return make_response({"msg": "pong!"}, 200)
