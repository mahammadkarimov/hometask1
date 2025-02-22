from .base import UserRepository

class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def get_all_users(self):
        user_list = [user.to_dict() for user in self.users]
        return user_list

    def create_user(self, user):
        self.users.append(user)
        return user.to_dict()