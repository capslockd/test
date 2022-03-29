from sorted_nested_list import Sorter
import unittest


class TestUser(unittest.TestCase):

    def test_sort(self):
        inputv = [['Harsh','20'],
        ['Beria','20'],
        ['Varun','19'],
        ['Kakunami','19'],
        ['Vikas','21']]

        self.x = Sorter(inputv)

        sorted_list = self.x.sort(1)
        self.assertEqual(sorted_list, [['Varun', '19'], ['Kakunami', '19'], ['Harsh', '20'], ['Beria', '20'], ['Vikas', '21']])

    def test_score_checker(self):
        inputv = [['Harsh','20'],
        ['Beria','20'],
        ['Varun','19'],
        ['Kakunami','19'],
        ['Vikas','21']]

        self.x = Sorter(inputv)

        sorted_list = self.x.sort(1)
        self.assertEqual(self.x.score_checker(sorted_list[0][1], sorted_list), "20")

    def test_check_students(self):
        inputv = [['Harsh','20'],
        ['Beria','20'],
        ['Varun','19'],
        ['Kakunami','19'],
        ['Vikas','21']]

        self.x = Sorter(inputv)

        sorted_list = self.x.sort(1)
        second_lowest_score = self.x.score_checker(sorted_list[0][1], sorted_list)
        self.assertEqual(self.x.check_students(second_lowest_score, sorted_list), ["Beria","Harsh"])

if __name__ == '__main__':
    unittest.main()