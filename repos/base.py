from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def create_user(self, user_data):
        pass