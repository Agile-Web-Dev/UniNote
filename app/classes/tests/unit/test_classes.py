import pytest

from app import db
from app.libs.tests.fixtures import app, client
from app.models import Class, Link
from app.utils.tests import ignored_keys, remove_keys


@pytest.fixture
def setup(app):
    Class.query.delete()
    Link.query.delete()

    yield app

    Class.query.delete()
    Link.query.delete()
    db.session.commit()


class_id = "CIT3403"


def test_get_class_info(client, setup):
    class_links = [
        Link(name="LMS", url="http://teaching.csse.uwa.edu.au/units/CITS3403/"),
        Link(name="CSSE Site", url="http://teaching.csse.uwa.edu.au/units/CITS3403/"),
    ]
    _classes = [
        Class(
            class_id=class_id,
            name="Agile Web Dev",
            links=class_links,
        ),
        Class(
            class_id="CITS3404",
            name="Unagile Web Dev",
            links=class_links,
        ),
    ]

    db.session.add_all(class_links)
    db.session.add_all(_classes)
    db.session.commit()

    classes = [_class.serialize() for _class in _classes]

    response = client.get(f"/api/classes/{class_id}")
    assert response.status_code == 200

    res = response.json

    assert isinstance(res, dict)
    assert remove_keys(res, ignored_keys) == classes[0]
