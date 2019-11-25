import unittest

from exercizes.exercize1.main import construct_initial_basket, number_max_of_apples, build_apple_label, \
    is_poisonous, split_in_5_stacks


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_initial_basket_size_is_48(self):
        expected_basket = [{'label': 'Apple n°1', 'poisonous': True}, {'label': 'Apple n°2', 'poisonous': True},
                           {'label': 'Apple n°3', 'poisonous': True}, {'label': 'Apple n°4', 'poisonous': True},
                           {'label': 'Apple n°5', 'poisonous': True}, {'label': 'Apple n°6', 'poisonous': True},
                           {'label': 'Apple n°7', 'poisonous': True}, {'label': 'Apple n°8', 'poisonous': True},
                           {'label': 'Apple n°9', 'poisonous': True}, {'label': 'Apple n°10', 'poisonous': True},
                           {'label': 'Apple n°11', 'poisonous': True}, {'label': 'Apple n°12', 'poisonous': True},
                           {'label': 'Apple n°13', 'poisonous': True}, {'label': 'Apple n°14', 'poisonous': True},
                           {'label': 'Apple n°15', 'poisonous': True}, {'label': 'Apple n°16', 'poisonous': True},
                           {'label': 'Apple n°17', 'poisonous': True}, {'label': 'Apple n°18', 'poisonous': True},
                           {'label': 'Apple n°19', 'poisonous': True}, {'label': 'Apple n°20', 'poisonous': True},
                           {'label': 'Apple n°21', 'poisonous': True}, {'label': 'Apple n°22', 'poisonous': True},
                           {'label': 'Apple n°23', 'poisonous': True}, {'label': 'Apple n°24', 'poisonous': True},
                           {'label': 'Apple n°25', 'poisonous': True}, {'label': 'Apple n°26', 'poisonous': True},
                           {'label': 'Apple n°27', 'poisonous': True}, {'label': 'Apple n°28', 'poisonous': True},
                           {'label': 'Apple n°29', 'poisonous': True}, {'label': 'Apple n°30', 'poisonous': True},
                           {'label': 'Apple n°31', 'poisonous': True}, {'label': 'Apple n°32', 'poisonous': True},
                           {'label': 'Apple n°33', 'poisonous': True}, {'label': 'Apple n°34', 'poisonous': True},
                           {'label': 'Apple n°35', 'poisonous': True}, {'label': 'Apple n°36', 'poisonous': True},
                           {'label': 'Apple n°37', 'poisonous': True}, {'label': 'Apple n°38', 'poisonous': True},
                           {'label': 'Apple n°39', 'poisonous': True}, {'label': 'Apple n°40', 'poisonous': True},
                           {'label': 'Apple n°41', 'poisonous': True}, {'label': 'Apple n°42', 'poisonous': True},
                           {'label': 'Apple n°43', 'poisonous': True}, {'label': 'Apple n°44', 'poisonous': True},
                           {'label': 'Apple n°45', 'poisonous': True}, {'label': 'Apple n°46', 'poisonous': False},
                           {'label': 'Apple n°47', 'poisonous': False}, {'label': 'Apple n°48', 'poisonous': False}]
        basket = construct_initial_basket()
        self.assertEqual(len(basket), 48)
        for cpt in range(1, number_max_of_apples + 1):
            apple = basket[cpt - 1]
            expected_apple = expected_basket[cpt - 1]
            self.assertEqual(apple, expected_apple)

    def test_basket_split_in_5_stacks(self):
        expected_stacks = [[{'label': 'Apple n°1', 'poisonous': True}, {'label': 'Apple n°2', 'poisonous': True},
                            {'label': 'Apple n°3', 'poisonous': True}, {'label': 'Apple n°4', 'poisonous': True},
                            {'label': 'Apple n°5', 'poisonous': True}, {'label': 'Apple n°6', 'poisonous': True},
                            {'label': 'Apple n°7', 'poisonous': True}, {'label': 'Apple n°8', 'poisonous': True},
                            {'label': 'Apple n°9', 'poisonous': True}],
                           [{'label': 'Apple n°10', 'poisonous': True}, {'label': 'Apple n°11', 'poisonous': True},
                            {'label': 'Apple n°12', 'poisonous': True}, {'label': 'Apple n°13', 'poisonous': True},
                            {'label': 'Apple n°14', 'poisonous': True}, {'label': 'Apple n°15', 'poisonous': True},
                            {'label': 'Apple n°16', 'poisonous': True}, {'label': 'Apple n°17', 'poisonous': True},
                            {'label': 'Apple n°18', 'poisonous': True}],
                           [{'label': 'Apple n°19', 'poisonous': True}, {'label': 'Apple n°20', 'poisonous': True},
                            {'label': 'Apple n°21', 'poisonous': True}, {'label': 'Apple n°22', 'poisonous': True},
                            {'label': 'Apple n°23', 'poisonous': True}, {'label': 'Apple n°24', 'poisonous': True},
                            {'label': 'Apple n°25', 'poisonous': True}, {'label': 'Apple n°26', 'poisonous': True},
                            {'label': 'Apple n°27', 'poisonous': True}],
                           [{'label': 'Apple n°28', 'poisonous': True}, {'label': 'Apple n°29', 'poisonous': True},
                            {'label': 'Apple n°30', 'poisonous': True}, {'label': 'Apple n°31', 'poisonous': True},
                            {'label': 'Apple n°32', 'poisonous': True}, {'label': 'Apple n°33', 'poisonous': True},
                            {'label': 'Apple n°34', 'poisonous': True}, {'label': 'Apple n°35', 'poisonous': True},
                            {'label': 'Apple n°36', 'poisonous': True}],
                           [{'label': 'Apple n°37', 'poisonous': True}, {'label': 'Apple n°38', 'poisonous': True},
                            {'label': 'Apple n°39', 'poisonous': True}, {'label': 'Apple n°40', 'poisonous': True},
                            {'label': 'Apple n°41', 'poisonous': True}, {'label': 'Apple n°42', 'poisonous': True},
                            {'label': 'Apple n°43', 'poisonous': True}, {'label': 'Apple n°44', 'poisonous': True},
                            {'label': 'Apple n°45', 'poisonous': True}, {'label': 'Apple n°46', 'poisonous': False},
                            {'label': 'Apple n°47', 'poisonous': False}, {'label': 'Apple n°48', 'poisonous': False}]]

        basket = construct_initial_basket()
        stacks = split_in_5_stacks(basket)
        for stack_idx in range (0, 5):
            self.assertEqual(stacks[stack_idx], expected_stacks[stack_idx])


if __name__ == '__main__':
    unittest.main()
