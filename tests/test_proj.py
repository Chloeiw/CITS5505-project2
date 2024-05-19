import responses 
import json 

from intelliShare.models import User, Question, Answer

def test_home(client):
    response = client.get("/")
    assert b"<title>IntelliShare</title>" in response.data


def test_registration(client, app):
    data = {"username": "test@test.com", "password": "testpassword"}
    response = client.post("/submit_profile",  data=data)
    assert response.status_code == 200
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().username == "test@test.com"



def test_question(client, app):
    response = client.post("/addQuestion_v1", data={"title": "What is a bird", "subtitle": "what is a peacock?", "question":"give a description what is a bird"})
    assert response.status_code == 200
    with app.app_context():
        assert Question.query.count() == 1
        assert Question.query.first().title == "What is a bird"
    pass


def test_answer(client, app):
    response = client.post("/questionDetails_v1.html", data={"question_id": 1, "answer": "here is a answer to question"})
    assert response.status_code == 200
    with app.app_context():
        assert Answer.count() == 1
        assert Answer.first().comment == "here is a answer to question"
    pass


