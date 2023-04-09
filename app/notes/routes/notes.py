from app import db
from app.models import Note

from . import bp


@bp.route("/<class_id>", methods=["GET"])
def get_notes(class_id):
    '''get notes based on the classID'''
    resArr = []
    res = db.session.query(Note).filter(Note.class_id == class_id)
    for entry in res:
        resArr.append(entry.serialize())
    return  resArr

#when user saves their notes
@bp.route("/", methods=["POST"])
def post_notes( createdBy, classId, title, contents):
    '''upload notes based on the classID into database'''
    note = Note(created_by = createdBy, class_id = classId ,title = title,content = contents)
    db.session.add(note)
    db.session.commit()
    return note
