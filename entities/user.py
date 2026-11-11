from entities import expense
from entities import trip
from datetime import date

class User:
    def __init__(self, user_id: int, username: str, email: str, password: str):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password

    def makeExpense():
        pass

    def makeTrip(trip: trip):
        pass   


    def __repr__(self):
        return f"User(user_id={self._user_id}, username='{self._username}', email='{self._email}', password='{self._password}')"