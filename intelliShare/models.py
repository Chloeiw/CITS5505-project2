from .db import db
from flask_login import UserMixin
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import relationship

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    image:Mapped[str] = mapped_column()

class Question(db.Model):
    __tablename__ = "question"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String, nullable=False)
    subtitle = mapped_column(String, nullable=False)
    content = mapped_column(String, nullable=False)
    cover = mapped_column(String, nullable=False)
    post_time = mapped_column(String, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'content': self.content,
            'cover': self.cover,
            'post_time': self.post_time,
            'user_id': self.user_id,
        }

class Answer(db.Model):
    __tablename__ = "answer"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    comment = mapped_column(String, nullable=False)
    answer_time = mapped_column(String, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    question_id = mapped_column(Integer, ForeignKey('question.id'), nullable=False)
    image = mapped_column(String)