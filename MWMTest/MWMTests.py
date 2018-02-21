import unittest
import config
import MWMFlask.Main as Main
import MWMFlask.utils.database.connection as database
import MWMFlask.utils.database.users as user
from MWMFlask.models.users import User

# class TestMapsAPI(unittest.TestCase):
#
#     Main.config_object = config.TestingConfig
#
#     def test_always_passes(self):
#         self.assertTrue(True)
#
#     def test_always_fails(self):
#         self.assertTrue(False)
#
#
# class TestVenuesAPI(unittest.TestCase):
#
#     Main.config_object = config.TestingConfig
#
#     def test_always_passes(self):
#         self.assertTrue(True)
#
#     def test_always_fails(self):
#         self.assertTrue(False)
#
#
# class TestWeatherAPI(unittest.TestCase):
#
#     Main.config_object = config.TestingConfig
#
#     def test_always_passes(self):
#         self.assertTrue(True)
#
#     def test_always_fails(self):
#         self.assertTrue(False)
#
#
# class TestWWW(unittest.TestCase):
#
#     Main.config_object = config.TestingConfig
#
#     def test_always_passes(self):
#         self.assertTrue(True)
#
#     def test_always_fails(self):
#         self.assertTrue(False)


class TestUsers(unittest.TestCase):

    Main.config_object = config.TestingConfig

    def setUp(self):
        database.init_db()
        database.load_db()

    def test_validate_admin_one_good_password(self):
        self.assertTrue(user.valid_password("admin_one@email.com", "admin_test_password"))

    def test_validate_admin_one_bad_password(self):
        self.assertFalse(user.valid_password("admin_one@email.com", "wrong_admin_password"))

    def test_validate_user_one_good_password(self):
        self.assertTrue(user.valid_password("user_one@email.com", "user_one_test_password"))

    def test_validate_user_one_bad_password(self):
        self.assertFalse(user.valid_password("user_one@email.com", "wrong_user_one_password"))

    def test_validate_user_two_good_password(self):
        self.assertTrue(user.valid_password("user_two@email.com", "user_two_test_password"))

    def test_validate_user_two_bad_password(self):
        self.assertFalse(user.valid_password("user_two@email.com", "wrong_user_two_password"))

    def test_get_correct_user_from_credentials(self):
        db_user = user.get_user("user_two@email.com")
        test_user = User(email="user_two@email.com", confirmed=1, admin=0,
                         first_name="Second", last_name="User", user_id=3)
        self.assertEqual(db_user, test_user)


if __name__ == '__main__':
    unittest.main()
