from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from db.connection import base

class UserModel(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))


class ExpenseModel(base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer)
    description = Column(String(200))
    date = Column(DateTime, default=datetime.utcnow)