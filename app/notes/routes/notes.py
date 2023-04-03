from app import db
from app.models import Note

from . import bp

#get notes based on the classID
@bp.route("/<class_id>", methods=["GET"])
def getNotes(class_id):
    resArr = []
    res = db.session.query(Note).filter(Note.class_id == class_id)
    for entry in res:
        resArr.append(entry.serialize())
    return  resArr

#when user saves their notes
@bp.route("/", methods=["POST"])
def postNotes( createdBy, classId, title, contents):
    note = Note(created_by = createdBy, class_id = classId ,title = title,content = contents)
    db.session.add(note)
    db.session.commit()
    return note
