from app.models import Class, Link

from . import bp


# get class based on the classID
@bp.route("/<class_id>", methods=["GET"])
def get_class_info(class_id):
    """
    Get class information based on the classID
    endpoint: /api/class/<class_id>
    serializes the class object into json
    """
    res = Class.query.filter(Class.class_id == class_id).one().serialize()
    return res
