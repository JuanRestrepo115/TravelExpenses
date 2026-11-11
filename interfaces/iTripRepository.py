from domain import trip

class iTripRepository:
    def create_trip(self, trip: trip):
        raise NotImplementedError

    def get_trip_by_id(self, trip_id: int):
        raise NotImplementedError

    def update_trip(self, trip: trip):
        raise NotImplementedError

    def delete_trip(self, trip_id: int):
        raise NotImplementedError