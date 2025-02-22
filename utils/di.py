from repos.csv import CSVUserRepository
from repos.memory import MemoryUserRepository

def get_user_repository(data_source):
    if data_source == 'csv':
        return CSVUserRepository()
    return MemoryUserRepository()