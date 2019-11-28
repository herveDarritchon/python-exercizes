import unittest

from exercizes.exercize13.main import get_lines_from_file, split_in_two_parts, zip_lefts_and_rights_array, \
    create_char_dict, sum_lefts_and_rights, filter_26_value


class Exercize13TestCase(unittest.TestCase):

    def test_construction_of_lines_array(self):
        lines = get_lines_from_file()
        self.assertEqual(len(lines), 3)
        self.assertEqual(len(lines[0]), 8)
        self.assertEqual(len(lines[1]), 8)
        self.assertEqual(len(lines[2]), 8)
        self.assertEqual(lines[0], 'RPTRAWFH')
        self.assertEqual(lines[1], 'UZPGEGFK')
        self.assertEqual(lines[2], 'QHGCCIZW')

    def test_split_lines_in_two_parts(self):
        lines = get_lines_from_file()
        lefts, rights = split_in_two_parts(lines)
        self.assertEqual(len(lefts), 3)
        self.assertEqual(len(rights), 3)
        self.assertEqual(len(lefts[0]), 4)
        self.assertEqual(len(lefts[1]), 4)
        self.assertEqual(len(lefts[2]), 4)
        self.assertEqual(len(rights[0]), 4)
        self.assertEqual(len(rights[1]), 4)
        self.assertEqual(len(rights[2]), 4)
        self.assertEqual(lefts[0], ['R', 'P', 'T', 'R'])
        self.assertEqual(lefts[1], ['U', 'Z', 'P', 'G'])
        self.assertEqual(lefts[2], ['Q', 'H', 'G', 'C'])
        self.assertEqual(rights[0], ['A', 'W', 'F', 'H'])
        self.assertEqual(rights[1], ['E', 'G', 'F', 'K'])
        self.assertEqual(rights[2], ['C', 'I', 'Z', 'W'])

    def test_zip_lefts_and_rights_array(self):
        lines = get_lines_from_file()
        lefts, rights = split_in_two_parts(lines)
        zipped_array = zip_lefts_and_rights_array(lefts, rights)
        self.assertEqual(len(zipped_array), 3)
        self.assertEqual(len(zipped_array[0]), 4)
        self.assertEqual(len(zipped_array[1]), 4)
        self.assertEqual(len(zipped_array[2]), 4)
        self.assertEqual(zipped_array[0], [('R', 'A'), ('P', 'W'), ('T', 'F'), ('R', 'H')])
        self.assertEqual(zipped_array[1], [('U', 'E'), ('Z', 'G'), ('P', 'F'), ('G', 'K')])
        self.assertEqual(zipped_array[2], [('Q', 'C'), ('H', 'I'), ('G', 'Z'), ('C', 'W')])

    def test_create_char_dict(self):
        expected_dict = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                         'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                         'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        char_dict = create_char_dict()
        self.assertEqual(char_dict, expected_dict)

    def test_sum_lefts_and_rights(self):
        expexted_sum_array = [[(19, 'R'), (39, 'P'), (26, 'T'), (26, 'R')],
                              [(26, 'U'), (33, 'Z'), (22, 'P'), (18, 'G')],
                              [(20, 'Q'), (17, 'H'), (33, 'G'), (26, 'C')]]
        char_dict = create_char_dict()
        lines = get_lines_from_file()
        lefts, rights = split_in_two_parts(lines)
        zipped_array = zip_lefts_and_rights_array(lefts, rights)
        sum_array = sum_lefts_and_rights(zipped_array, char_dict)
        self.assertEqual(sum_array, expexted_sum_array)


if __name__ == '__main__':
    unittest.main()
