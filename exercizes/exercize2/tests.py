import unittest

from exercizes.exercize2.main import popule_circle_for, suppress_an_elt


class Exercize2TestCase(unittest.TestCase):

    def test_construction_of_the_series_of_number(self):
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = popule_circle_for(9)
        self.assertEqual(result, expected_result)

    def test_suppress_an_element_for_one_turn(self):
        expected_result = [2, 3, 4, 5, 6, 7, 8, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        self.assertEqual(1, elt)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_two_turns(self):
        expected_result = [3, 4, 5, 6, 7, 8, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(2, elt)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_three_turns(self):
        expected_result = [3, 5, 6, 7, 8, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(elt, 4)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_fourth_turns(self):
        expected_result = [3, 5, 6, 7, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(8, elt)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_fifth_turns(self):
        expected_result = [3, 6, 7, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(5, elt)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_sixth_turns(self):
        expected_result = [3, 7, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(6, elt)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_seventh_turns(self):
        expected_result = [7, 9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(3, elt)
        self.assertEqual(expected_result, remaining_list)

    def test_suppress_an_element_for_heigth_turns(self):
        expected_result = [9]
        initial_list = popule_circle_for(9)
        start_elt_idx, elt, remaining_list = suppress_an_elt(0, 0, initial_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, remaining_list)
        self.assertEqual(7, elt)
        self.assertEqual(expected_result, remaining_list)


if __name__ == '__main__':
    unittest.main()

"""
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9
3 4 5 6 7 8 9
3 5 6 7 8 9
3 5 6 7 9
3 6 7 9
3 7 9
7 9
9

"""
