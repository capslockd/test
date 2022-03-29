from unit_test_2 import User
import unittest

class TestUser(unittest.TestCase):

    def test_user_activation(self):
        user1 = User()
        user1.activate()
        self.assertTrue(user1.is_active())

    def test_user_points_update(self):
        user1 = User()
        user1.add_points(25)
        self.assertEqual(user1.get_points(), 25)

    def test_user_level_change(self):
        user1 = User()
        user1.add_points(205)
        self.assertEqual(user1.get_level(), 2)
        
if __name__ == '__main__':
    unittest.main()