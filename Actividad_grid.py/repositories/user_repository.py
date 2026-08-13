"""Se encarga de gestionar el almacenamiento de los datos en memoria."""
from models.user import User

class UserRepository:
    def __init__(self) -> None:
        self._users: list[User] = []

    def save(self, user: User) -> User:
        self._users.append(user)
        return user

    def find_all(self) -> list[User]:
        return self._users