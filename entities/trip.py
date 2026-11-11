from datetime import date


class trip:

    def __init__(self, trip_id: int, user_id: int, destination: str, start_date: date, end_date: date):
        self._trip_id = trip_id
        self._user_id = user_id
        self._destination = destination
        self._start_date = start_date
        self._end_date = end_date


    # Getters and Setters
    def get_trip_id(self):
        return self._trip_id

    def get_user_id(self):
        return self._user_id

    def get_destination(self):
        return self._destination

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def set_trip_id(self, trip_id: int):
        self._trip_id = trip_id

    def set_user_id(self, user_id: int):
        self._user_id = user_id

    def set_destination(self, destination: str):
        self._destination = destination

    def set_start_date(self, start_date: date):
        self._start_date = start_date

    def set_end_date(self, end_date: date):
        self._end_date = end_date

    def __repr__(self):
        return f"Trip(trip_id={self._trip_id}, user_id={self._user_id}, destination='{self._destination}', start_date='{self._start_date}', end_date='{self._end_date}')"