import unittest
from mycode import unittest_sample


class MyFirstTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = unittest_sample()

    def test_hello(self):
        output = self.x.hello_world()
        self.assertEqual(output, 'hello world')

    def test_custom_num_list(self):
        output = self.x.create_num_list(10)

        self.assertEqual(len(output), 10)

    def test_custom_func_x(self):
        output = self.x.custom_func_x(3,2,3)

        self.assertEqual(output, 54)

    def test_custom_non_lin_num_list(self):

        output1 = self.x.custom_non_lin_num_list(5,2,3)[2]
        output2 = self.x.custom_non_lin_num_list(5,3,2)[4]

        self.assertEqual(output1, 16)
        self.assertEqual(output2, 48)

if __name__ == '__main__':
    unittest.main()