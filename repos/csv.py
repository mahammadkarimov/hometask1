import csv
from os.path import exists
from .base import UserRepository

class CSVUserRepository(UserRepository):
    def __init__(self, file_path='users.csv'):
        self.file_path = file_path
        if not exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "first_name", "last_name", "email"])
                writer.writeheader()

    def get_all_users(self):
        with open(self.file_path, mode='r') as file:
            return list(csv.DictReader(file))

    def create_user(self, user):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "first_name", "last_name", "email"])
            writer.writerow(user.to_dict())
        return user.to_dict()