from app import db
from app.models import Class

from . import bp


# get notes based on the classID
@bp.route("/<class_id>", methods=["GET"])
def get_class_users(class_id):
    resArr = []
    res = db.session.query(Class).filter(Class.class_id == class_id)
    for entry in res:
        resArr.append(entry.serialize())
    return resArr
