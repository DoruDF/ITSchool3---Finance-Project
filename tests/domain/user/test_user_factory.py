import unittest

from domain.user.Factory import UserFactory, InvalidUsername


class UserFactoryTestCase(unittest.TestCase):
    @unittest.skip("TODO")
    def test_it_creates_a_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6_and-20"
        factory = UserFactory()

        actual_user = factory.make(username)


        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    @unittest.skip("TODO")
    def test_it_raises_exception_if_the_username_is_below_6(self):
        username = "below"
        factory = UserFactory()
        with self.assertRaises(InvalidUsername) as context:
            factory.make(username)

        self.assertEqual("Username should have at leasst 6 characters"
                        str(context.exception))

    @unittest.skip("TODO")
    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        pass

    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        pass

    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        pass






if __name__ == '__main__':
    unittest.main()
