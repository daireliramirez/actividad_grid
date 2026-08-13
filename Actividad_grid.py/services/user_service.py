"""Contiene la lógica de negocio de mi aplicación."""
from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def find_all(self):
        return self.repository.find_all()

    def create_one(self, fname: str, lname: str, age: int, email: str) -> User:
        user = User(fname, lname, age, email)
        
        return self.repository.save(user)