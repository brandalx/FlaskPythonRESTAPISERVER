import pytest
from website import create_app, db
from website.models import User
from werkzeug.security import generate_password_hash


@pytest.fixture
def test_client():
    app = create_app("testing")
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


def test_login_page(test_client):
    response = test_client.get("/login")
    assert b"Email" in response.data
    assert b"Password" in response.data
