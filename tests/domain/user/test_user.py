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

    def test_it_gets_empty_list_if_we_do_not_specify_stock(self):
        user = User("random-username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)


if __name__ == "__main__":
    unittest.main()
