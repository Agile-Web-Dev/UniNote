import pytest
from pytest_unordered import unordered

from app import db
from app.libs.tests.fixtures import app, client
from app.models import Note
from app.utils.tests import ignored_keys, remove_keys


@pytest.fixture
def setup(app):
    Note.query.delete()

    yield app

    Note.query.delete()
    db.session.commit()


class_id = "CIT3403"


def test_get_notes(client, setup):
    _notes = [
        Note(
            created_by="100",
            class_id=class_id,
            title="Note 0",
            content="content0",
        ),
        Note(
            created_by="101",
            class_id=class_id,
            title="Note 1",
            content="content1",
        ),
        Note(
            created_by="102",
            class_id=class_id,
            title="Note 2",
            content="content2",
        ),
    ]

    db.session.add_all(_notes)
    db.session.commit()

    notes = [note.serialize() for note in _notes]

    response = client.get(f"/api/notes/{class_id}")
    assert response.status_code == 200

    items = response.json

    assert isinstance(items, list)
    assert len(items) == len(notes)
    assert [remove_keys(item, ignored_keys) for item in items] == unordered(
        [remove_keys(note, ignored_keys) for note in notes]
    )


def test_post_notes(client, setup):
    request_body = {
        "createdBy": "100",
        "classId": class_id,
        "title": "Test note",
        "content": "Test content",
    }

    response = client.post("/api/notes", json=request_body)
    assert response.status_code == 201

    data = response.json

    assert isinstance(data, dict)

    assert data["created_by"] == request_body["createdBy"]
    assert data["class_id"] == request_body["classId"]
    assert data["title"] == request_body["title"]
    assert data["content"] == request_body["content"]

    assert (
        db.session.query(Note).filter(Note.note_id == data["note_id"]).first()
        is not None
    )
