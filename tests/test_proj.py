import responses 

from intelliShare.models import User

def test_home(client):
    response = client.get("/")
    assert b"<title>IntelliShare</title>" in response.data


def test_registration(client, app):
    response = client.post("/register", data={"email": "test@test.com", "password": "testpassword"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"



def test_question(client, app):
    response = client.post("/question", data={"email": "test@test.com", "password": "testpassword"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"
    pass


def test_answer(client, app):
    response = client.post("/answer", data={"email": "test@test.com", "password": "testpassword"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"
    pass


def test_search(client, app):
    response = client.post("/search", data={"email": "test@test.com", "password": "testpassword"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"
    pass
