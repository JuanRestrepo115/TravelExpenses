
class User:
    def __init__(self, user_id: int, username: str, email: str, password: str):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password

    # Getters
    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    # Setters
    @username.setter
    def username(self, value: str):
        self._username = value

    @email.setter
    def email(self, value: str):
        self._email = value

    @password.setter
    def password(self, value: str):
        self._password = value


    def __repr__(self):
        return f"User(user_id={self._user_id}, username='{self._username}', email='{self._email}', password='{self._password}')"