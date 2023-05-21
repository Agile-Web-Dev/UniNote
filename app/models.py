from datetime import datetime
from uuid import uuid4

from flask_login import UserMixin, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


def generate_uuid():
    return str(uuid4())


class TimeMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)


user_class = db.Table(
    "user_class",
    db.Column("user_id", db.ForeignKey("user.user_id"), primary_key=True),
    db.Column("class_id", db.ForeignKey("class.class_id"), primary_key=True),
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
        return {
            "email": self.email,
            "user_id": self.user_id,
            "name": self.name,
            "class_ids": [_class.serialize_for_user() for _class in self.class_ids],
        }

    def serialize_for_classes(self):
        return {"user_id": self.user_id}


@login.user_loader
def load_user(user_id=None):
    if user_id is None:
        if not current_user.is_authenticated:
            return None
        user_id = current_user.user_id
    return User.query.filter_by(user_id=user_id).first()


class Class(db.Model, TimeMixin):
    __tablename__ = "class"

    class_id = db.Column(
        db.String, primary_key=True, nullable=False, default=generate_uuid
    )
    user_ids = db.relationship("User", secondary=user_class, back_populates="class_ids")
    name = db.Column(db.String, nullable=False)
    links = db.relationship("Link")

    def serialize(self):
        return {
            "class_id": self.class_id,
            "user_ids": [User.serialize_for_classes() for User in self.user_ids],
            "name": self.name,
            "links": [Link.serialize() for Link in self.links],
        }

    def serialize_for_user(self):
        return {"class_id": self.class_id, "name": self.name}


class Message(db.Model, TimeMixin):
    __tablename__ = "message"

    message_id = db.Column(
        db.String, primary_key=True, nullable=False, default=generate_uuid
    )
    created_by = db.Column(db.ForeignKey("user.user_id"), nullable=False)
    is_bot = db.Column(db.Boolean, default=False)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    content = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            "message_id": self.message_id,
            "created_by": self.created_by,
            "is_bot": self.is_bot,
            "content": self.content,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        }


class Note(db.Model, TimeMixin):
    __tablename__ = "note"

    note_id = db.Column(
        db.String, primary_key=True, nullable=False, default=generate_uuid
    )
    created_by = db.Column(db.ForeignKey("user.user_id"), nullable=False)
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            "note_id": self.note_id,
            "created_by": self.created_by,
            "class_id": self.class_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        }


class Link(db.Model, TimeMixin):
    __tablename__ = "link"

    link_id = db.Column(
        db.String, primary_key=True, nullable=False, default=generate_uuid
    )
    class_id = db.Column(db.ForeignKey("class.class_id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)

    def serialize(self):
        return {"link_id": self.link_id, "name": self.name, "url": self.url}
