from app import create_app, db
from app.models import User

app = create_app()

app.config.update(
    {
        "TESTING": True,
    }
)

with app.app_context():
    User.query.delete()

    user = User(email="testes@test.com", user_id="123", name="Test", role="student")

    user.set_password("123")

    db.session.add_all([user])
    db.session.commit()

    print("Created new user")
