from . import bp
from app.models import Note
from app import db

#get notes based on the classID
@bp.route("/note", methods=["GET"])
def getNotes(classId):
    resArr = []
    res = db.session.query(Note).filter(Note.class_id == classId)
    for entry in res:
        resArr.append((entry.note_id,entry.created_by, entry.class_id, entry.title, entry.content, entry.tag_names))
    return  resArr

#when user saves their notes
@bp.route("/note", methods=["POST"])
def postNotes( createdBy, classId, title, contents):
    note = Note(created_by = createdBy, class_id = classId ,title = title,content = contents)
    db.session.add(note)
    db.session.commit()
    return note
