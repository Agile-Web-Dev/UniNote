from app import create_app, db
from app.models import Class, Link, Message, Note, Tag, User

app = create_app()

app.config.update(
    {
        "TESTING": True,
    }
)

with app.app_context():
    User.query.delete()
    Note.query.delete()
    Tag.query.delete()
    Class.query.delete()
    Link.query.delete()
    Message.query.delete()

    class_links = [
        Link(name="LMS", url="http://teaching.csse.uwa.edu.au/units/CITS3403/"),
        Link(name="CSSE Site", url="http://teaching.csse.uwa.edu.au/units/CITS3403/"),
    ]

    cits3403 = Class(
        class_id="CITS3403",
        name="Agile Web Dev",
        links=class_links,
    )
    cits2401 = Class(
        class_id="CITS2401",
        name="Python",
        links=class_links,
    )
    cits1001 = Class(
        class_id="CITS1001",
        name="Java",
        links=class_links,
    )
    cits2002 = Class(
        class_id="CITS2002",
        name="Systems",
        links=class_links,
    )
    classes = [cits3403, cits2401, cits1001, cits2002]
    db.session.add_all(class_links)
    db.session.add_all(classes)
    print("CLASSES", classes)

    user = User(email="a@a.com", user_id="23030303", name="Test", role="student")

    user2 = User(email="not@test.com", user_id="12312312", name="danny", role="student")
    user.set_password("123")
    user2.set_password("123")
    db.session.add_all([user, user2])
    db.session.commit()

    user.class_ids.append(cits3403)
    user.class_ids.append(cits2401)
    user.class_ids.append(cits1001)
    user.class_ids.append(cits2002)
    user2.class_ids.append(cits3403)
    user2.class_ids.append(cits2401)
    db.session.commit()

    print("users TEST", user.get_id(), user.class_ids, user2)

    notes = [
        Note(
            created_by=123,
            class_id="CITS3403",
            title="My Mom",
            content="my mommy is cool and the best.",
        ),
        Note(
            created_by=123,
            class_id="CITS3403",
            title="Random thoughts",
            content="Finished her are its honoured drawings nor. Pretty see mutual thrown all not edward ten. Particular an boisterous up he reasonably frequently. Several any had enjoyed shewing studied two. Up intention remainder sportsmen behaviour ye happiness. Few again any alone style added abode ask. Nay projecting unpleasing boisterous eat discovered solicitude. Own six moments produce elderly pasture far arrival. Hold our year they ten upon. Gentleman contained so intention sweetness in on resolving.",
        ),
        Note(
            created_by=123,
            class_id="CITS3403",
            title="Suicidal thoughts",
            content="吉安而來 玉，不題 父親回衙 汗流如雨 冒認收了. 後竊聽 在一處 己轉身. 玉，不題 矣 曰： 父親回衙 去 」 冒認收了 吉安而來 汗流如雨 關雎. 關雎 覽 事 耳 去 」 意 冒認收了 出 吉安而來 汗流如雨 父親回衙 玉，不題. 此是後話 也懊悔不了 出 饒爾去罷」 ，愈聽愈惱 去 矣 意 關雎. 第十一回 己轉身 在一處 分得意 樂而不淫. 意 事 ，可 耳 出 去 曰： 關雎. 覽 矣 父親回衙 誨 冒認收了 」 去 吉安而來 出 玉，不題 汗流如雨. 覽 去 曰： 意 事 誨 ，可. 」 意 誨 去 出. ﻿白圭志 第十一回 在一處 危德至. 玉，不題 關雎 父親回衙 ，可 汗流如雨 冒認收了 去 意 吉安而來. 關雎 」 去 矣. 事 曰： 去 誨 矣 關雎. 汗流如雨 覽 冒認收了 事 吉安而來 玉，不題 去 父親回衙 意. 在一處 第十一回 建章曰： ﻿白圭志 不稱讚. 貢院 第五回 第二回. ，愈聽愈惱 饒爾去罷」 也懊悔不了 此是後話. 誨 」 關雎 出. 事 去 覽 」 意 誨. 誨 覽 事 耳 ，可 去 」 意. 誨 關雎 意 事 覽 」 曰：. 事 誨 」 關雎 出 ，可 去. .",
        ),
    ]

    tags = [
        Tag(name="Javascript Lecture", class_id="CITS3403"),
        Tag(name="HTML Lecture", class_id="CITS3403"),
        Tag(name="API Lecture", class_id="CITS3403"),
    ]

    messages = [
        Message(created_by="Dan", class_id="CITS3403", content="hey wassup guys"),
        Message(created_by="Bob", class_id="CITS3403", content="Hai"),
        Message(created_by="John", class_id="CITS3403", content="Sup"),
    ]

    db.session.add_all(messages)
    db.session.add_all(notes)
    db.session.add_all(tags)
    db.session.commit()

    print("Db has been populated")
