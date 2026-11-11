from interfaces import iUserRepository
from domain import user

class UserService:
    def __init__(self, user_repository: iUserRepository):
        self.user_repository = user_repository

    def create_user(self, user: user):
        if not user.name:
            raise ValueError("User name cannot be empty.")
        
        self.user_repository.create_user(user)

    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)

    def update_user(self, user: user):
        if not user.name:
            raise ValueError("User name cannot be empty.")
        
        self.user_repository.update_user(user)

    def delete_user(self, user_id: int):
        self.user_repository.delete_user(user_id)