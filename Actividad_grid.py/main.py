from repositories.user_repository import UserRepository
from services.user_service import UserService
from views.app_window import AppWindow

if __name__ == "__main__":
    repository = UserRepository()
    service = UserService(repository)
    app_window = AppWindow(service)
    app_window.mainloop()