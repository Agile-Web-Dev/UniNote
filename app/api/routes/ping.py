from flask import make_response

from . import bp


@bp.route("/ping", methods=["GET"])
def ping():
    """
    Ping the server to check if it is alive
    """
    return make_response({"msg": "pong!"}, 200)
