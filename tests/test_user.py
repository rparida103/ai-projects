import pytest; from controllers.user_controller import UserController

class TestUserController:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.controller = UserController()

    def test_create_user(self):
        user = self.controller.create_user(1, 'testuser', 'test@example.com')
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'

    def test_get_users(self):
        self.controller.create_user(1, 'testuser', 'test@example.com')
        users = self.controller.get_users()
        assert len(users) == 1
        assert users[0].username == 'testuser'

    def test_multiple_users(self):
        self.controller.create_user(1, 'testuser1', 'test1@example.com')
        self.controller.create_user(2, 'testuser2', 'test2@example.com')
        users = self.controller.get_users()
        assert len(users) == 2
        assert users[0].username == 'testuser1'
        assert users[1].username == 'testuser2'