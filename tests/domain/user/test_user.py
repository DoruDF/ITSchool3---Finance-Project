import unittest

from domain.user.user import User


class UserMyTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random_generate"
        user = User(username)
        # execution
        actual_username = user.username
        # asertion
        self.assertEqual(username, actual_username)


if __name__ == "__main__":
    unittest.main()
