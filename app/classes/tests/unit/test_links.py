import pytest
from pytest_unordered import unordered

from app import db
from app.libs.tests.fixtures import app, client
from app.libs.tests.utils import ignored_keys, remove_keys
from app.models import Class, Link


@pytest.fixture
def setup(app):
    Class.query.delete()
    Link.query.delete()

    yield app

    Class.query.delete()
    Link.query.delete()
    db.session.commit()


class_id = "CIT3403"


def test_get_class_links(client, setup):
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
            links=[],
        ),
    ]

    db.session.add_all(class_links)
    db.session.add_all(_classes)
    db.session.commit()

    links = [_link.serialize() for _link in class_links]

    response = client.get(f"/api/classes/{class_id}/links")
    assert response.status_code == 200

    items = response.json

    assert len(items) == len(links)
    assert [remove_keys(item, ignored_keys) for item in items] == unordered(
        [remove_keys(link, ignored_keys) for link in links]
    )
