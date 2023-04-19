import pytest

from app import db
from app.libs.tests.fixtures import app, client
from app.models import Note


@pytest.fixture
def setup(app):
    Note.query.delete()
    db.session.commit()

    yield app

    Note.query.delete()
    db.session.commit()

    notes = [
        Note(
            note_id=202,
            created_by=123,
            class_id="CITS3403",
            title="My Mom",
            content="my mommy is cool and the best.",
        ),
        Note(
            note_id=203,
            created_by=123,
            class_id="CITS3403",
            title="Random thoughts",
            content="Finished her are its honoured drawings nor. Pretty see mutual thrown all not edward ten. Particular an boisterous up he reasonably frequently. Several any had enjoyed shewing studied two. Up intention remainder sportsmen behaviour ye happiness. Few again any alone style added abode ask. Nay projecting unpleasing boisterous eat discovered solicitude. Own six moments produce elderly pasture far arrival. Hold our year they ten upon. Gentleman contained so intention sweetness in on resolving.",
        ),
        Note(
            note_id=204,
            created_by=123,
            class_id="CITS3403",
            title="Suicidal thoughts",
            content="吉安而來 玉，不題 父親回衙 汗流如雨 冒認收了. 後竊聽 在一處 己轉身. 玉，不題 矣 曰： 父親回衙 去 」 冒認收了 吉安而來 汗流如雨 關雎. 關雎 覽 事 耳 去 」 意 冒認收了 出 吉安而來 汗流如雨 父親回衙 玉，不題. 此是後話 也懊悔不了 出 饒爾去罷」 ，愈聽愈惱 去 矣 意 關雎. 第十一回 己轉身 在一處 分得意 樂而不淫. 意 事 ，可 耳 出 去 曰： 關雎. 覽 矣 父親回衙 誨 冒認收了 」 去 吉安而來 出 玉，不題 汗流如雨. 覽 去 曰： 意 事 誨 ，可. 」 意 誨 去 出. ﻿白圭志 第十一回 在一處 危德至. 玉，不題 關雎 父親回衙 ，可 汗流如雨 冒認收了 去 意 吉安而來. 關雎 」 去 矣. 事 曰： 去 誨 矣 關雎. 汗流如雨 覽 冒認收了 事 吉安而來 玉，不題 去 父親回衙 意. 在一處 第十一回 建章曰： ﻿白圭志 不稱讚. 貢院 第五回 第二回. ，愈聽愈惱 饒爾去罷」 也懊悔不了 此是後話. 誨 」 關雎 出. 事 去 覽 」 意 誨. 誨 覽 事 耳 ，可 去 」 意. 誨 關雎 意 事 覽 」 曰：. 事 誨 」 關雎 出 ，可 去. .",
        ),
    ]

    db.session.add_all(notes)
    db.session.commit()


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
