from datetime import datetime
from uuid import uuid4

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


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


class User(db.Model, TimeMixin, UserMixin):
    __tablename__ = "user"

    email = db.Column(db.String, primary_key=True, nullable=False)
    user_id = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    class_ids = db.relationship(
        "Class", secondary=user_class, back_populates="user_ids"
    )
    role = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.user_id
    
    def serialize(self):
        print()
        return {"email": self.email, "user_id": self.user_id, "name": self.name, "Class_ids": [Class.serialize_for_user() for Class in self.class_ids]}
    
    def serialize_for_classes(self):
        print()
        return {"user_id": self.user_id}


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


class Class(db.Model, TimeMixin):
    __tablename__ = "class"

    class_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    user_ids = db.relationship("User", secondary=user_class, back_populates="class_ids")
    name = db.Column(db.String, nullable=False)
    links = db.Column(db.String)
    
    def serialize(self):
        return {"class_id": self.class_id,"user_ids":[User.serialize_for_classes() for User in self.user_ids] ,"name": self.name, "links": self.links}
    def serialize_for_user(self):
        return {"class_id": self.class_id, "name": self.name}



class Message(db.Model, TimeMixin):
    __tablename__ = "message"

    message_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    created_by = db.Column(db.ForeignKey("user.user_id"), nullable=False)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    content = db.Column(db.String)
    
    def serialize(self):
        return {"message_id": self.message_id, "created_by": self.created_by, "class_id": self.class_id, "content": self.content, "created_at": TimeMixin.created_at, "updated_at": TimeMixin.created_at}



class Note(db.Model, TimeMixin):
    __tablename__ = "note"

    note_id = db.Column(db.String, primary_key=True, nullable=False, default=uuid4)
    created_by = db.Column(db.ForeignKey("user.user_id"), nullable=False)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    tag_names = db.relationship("Tag", secondary=note_tag, back_populates="note_ids")

    def serialize(self):
        return {"note_id": self.note_id, "created_by": self.created_by, "class_id": self.class_id, "title": self.title, "content": self.content}


class Tag(db.Model, TimeMixin):
    __tablename__ = "tag"

    name = db.Column(db.String, nullable=False, primary_key=True)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    note_ids = db.relationship("Note", secondary=note_tag, back_populates="tag_names")

    def serialize(self):
        return {"name": self.name, "class_id": self.class_id, "note_ids": self.note_ids,"created_at": TimeMixin.created_at, "updated_at": TimeMixin.created_at}

