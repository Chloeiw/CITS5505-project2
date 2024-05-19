import responses 
import json 

from intelliShare.models import User

def test_home(client):
    response = client.get("/")
    assert b"<title>IntelliShare</title>" in response.data


def test_registration(client, app):
    data = {"username": "test@test.com", "password": "testpassword"}
    response = client.post("/submit_profile", 
                           data=json.dumps(data),
                           headers={"Content-Type": "application/json"})
    print(response.json)
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().username == "test@test.com"



# def test_question(client, app):
#     response = client.post("/question", data={"email": "test@test.com", "password": "testpassword"})

#     with app.app_context():
#         assert User.query.count() == 1
#         assert User.query.first().email == "test@test.com"
#     pass


# def test_answer(client, app):
#     response = client.post("/answer", data={"email": "test@test.com", "password": "testpassword"})

#     with app.app_context():
#         assert User.query.count() == 1
#         assert User.query.first().email == "test@test.com"
#     pass


# def test_search(client, app):
#     response = client.post("/search", data={"email": "test@test.com", "password": "testpassword"})

#     with app.app_context():
#         assert User.query.count() == 1
#         assert User.query.first().email == "test@test.com"
#     pass
