import unittest

from domain.user.factory import UserFactory, InvalidUsername
from domain.user.user import User


class UserFactoryTestCase(unittest.TestCase):
    def test_it_creates_a_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-and-20"
        factory = UserFactory()

        actual_user = factory.make(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_below_6(self):
        username = "below"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make(username)

        self.assertEqual(
            "Username should have at least 6 characters.", str(context.exception)
        )

    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        username = "a" * 21
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make(username)

        self.assertEqual(
            "Username should have a maximum of 20 characters", str(context.exception)
        )

    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        username = "first-user12"
        factory = UserFactory()

        actual_username = factory.make(username)

        self.assertEqual(username, actual_username.username)

    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        username = "username_1"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make(username)

        self.assertEqual(
            "Username should contain only letters, numbers and '-'",
            str(context.exception),
        )


if __name__ == "__main__":
    unittest.main()
