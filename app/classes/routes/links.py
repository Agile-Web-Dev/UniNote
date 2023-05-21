from app.models import Class, Link

from . import bp


# get class based on the classID
@bp.route("/<class_id>/links", methods=["GET"])
def get_class_links(class_id):
    """
    Get class information based on the classID
    endpoint: /api/class/<class_id>
    serializes the link into a json format when returned
    """
    res = [
        link.serialize()
        for link in Link.query.join(Class.links).filter(Class.class_id == class_id)
    ]
    return res
