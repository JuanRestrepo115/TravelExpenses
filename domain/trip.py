import datetime


class trip:

    def __init__(self, trip_id: int, user_id: int, destination: str, start_date: datetime.date, end_date: datetime.date):
        self._trip_id = trip_id
        self._user_id = user_id
        self._destination = destination
        self._start_date = start_date
        self._end_date = end_date


    # Getters

    @property
    def trip_id(self) -> int:
        return self._trip_id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def start_date(self) -> datetime.date:
        return self._start_date

    @property
    def end_date(self) -> datetime.date:
        return self._end_date

    # Setters

    @destination.setter
    def destination(self, value: str):
        self._destination = value

    @start_date.setter
    def start_date(self, value: datetime.date):
        self._start_date = value

    @end_date.setter
    def end_date(self, value: datetime.date):
        self._end_date = value


    def __repr__(self):
        return f"Trip(trip_id={self._trip_id}, user_id={self._user_id}, destination='{self._destination}', start_date='{self._start_date}', end_date='{self._end_date}')"