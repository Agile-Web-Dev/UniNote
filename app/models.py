from datetime import datetime
from uuid import uuid4

from app import db


class TimeMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


user_class = db.Table(
    "user_class",
    db.Column("user_id", db.ForeignKey("user.user_id"), primary_key=True),
    db.Column("class_id", db.ForeignKey("class.class_id"), primary_key=True),
)

note_tag = db.Table(
    "note_tag",
    db.Column("note_id", db.ForeignKey("note.note_id"), primary_key=True),
    db.Column("tag_name", db.ForeignKey("tag.name"), primary_key=True),
)


class User(db.Model, TimeMixin):
    __tablename__ = "user"

    email = db.Column(db.String, primary_key=True, nullable=False)
    user_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String, nullable=False)
    class_ids = db.relationship(
        "Class", secondary=user_class, back_populates="user_ids"
    )
    role = db.Column(db.String, nullable=False)


class Class(db.Model, TimeMixin):
    __tablename__ = "class"

    class_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    user_ids = db.relationship("User", secondary=user_class, back_populates="class_ids")
    name = db.Column(db.String, nullable=False)
    links = db.Column(db.String)


class Message(db.Model, TimeMixin):
    __tablename__ = "message"

    message_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    created_by = db.Column(db.ForeignKey("user.user_id"), nullable=False)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    content = db.Column(db.String)


class Note(db.Model, TimeMixin):
    __tablename__ = "note"

    note_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    created_by = db.Column(db.ForeignKey("user.user_id"), nullable=False)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    tag_ids = db.relationship("Tag", secondary=note_tag, back_populates="tag_nmes")


class Tag(db.Model, TimeMixin):
    __tablename__ = "tag"

    name = db.Column(db.String, nullable=False, primary_key=True)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    note_ids = db.relationship("Note", secondary=note_tag, back_populates="note_ids")
