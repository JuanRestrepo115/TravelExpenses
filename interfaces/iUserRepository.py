class iUserRepository:
    def get_user_by_id(self, user_id: int):
        raise NotImplementedError

    def create_user(self, user):
        raise NotImplementedError

    def update_user(self, user):
        raise NotImplementedError

    def delete_user(self, user_id: int):
        raise NotImplementedError

    