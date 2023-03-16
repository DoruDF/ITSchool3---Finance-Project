import unittest
from domain.user.user import User
class UserMyTestCase(unittest.TestCase):

    def test_user_sets_the_right_username(self):
        #set up
        username = "random generated"
        user = User(username)
        actual_username= user.username
        self.assertEqual(username, actual_username)
    @unittest.skip("TODO: Homework")
    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        pass

    @unittest.skip("TODO: Homework")
    def test_it_sets_the_stocks_we_give(self):
        pass



if __name__ == '__main__':
    unittest.main()