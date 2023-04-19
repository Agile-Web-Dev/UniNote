from app.libs.tests.fixtures import app, client


def test_get_notes(client):
    response = client.get("/api/notes/CITS3403")
    assert response.status_code == 200
    notes = response.json
    assert isinstance(notes, list)
    assert len(notes) == 3

    # Asserting the contents of first note
    note = notes[0]
    assert note["note_id"] == "202"
    assert note["class_id"] == "CITS3403"
    assert note["title"] == "My Mom"
    assert note["content"] == "my mommy is cool and the best."
    assert note["created_by"] == "123"

    # Asserting the contents of second note
    note = notes[1]
    assert note["note_id"] == "203"
    assert note["class_id"] == "CITS3403"
    assert note["title"] == "Random thoughts"
    assert note["created_by"] == "123"
