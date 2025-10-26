from models.user import User

class UserController:
    def __init__(self):
        self.users = []

    def create_user(self, user_id, username, email):
        user = User(user_id, username, email)
        self.users.append(user)
        return user

    def get_users(self):
        return self.users