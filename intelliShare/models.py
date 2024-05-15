from db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    image:Mapped[str] = mapped_column()



