from app import db
from app.models import Note

from . import bp


@bp.route("/", methods=["GET"])
def get_notes(class_id):
    """get notes based on the classID"""
    res = [
        note.serialize()
        for note in db.session.query(Note).filter(Note.class_id == class_id)
    ]
    return res


# when user saves their notes
@bp.route("/", methods=["POST"])
def post_notes(createdBy, classId, title, content):
    """upload notes based on the classID into database"""
    note = Note(created_by=createdBy, class_id=classId, title=title, content=content)
    db.session.add(note)
    db.session.commit()
    return note
