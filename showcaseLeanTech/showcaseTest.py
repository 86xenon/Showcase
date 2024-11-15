import unittest
from main import compute_change

'''
Only valid inputs besides 0 used in unit tests because receive_input handles validation
Tests cover zero input, dollars/coins individually, random inputs
'''


class MyTestCase(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(compute_change(['0', '0']), ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['0', '1']), ([0, 0, 0, 0, 0, 0], [0, 0, 0, 1]))
        self.assertEqual(compute_change(['1', '0']), ([0, 0, 0, 0, 0, 1], [0, 0, 0, 0]))

    def test_dollar_individual(self):
        self.assertEqual(compute_change(['5', '0']), ([0, 0, 0, 0, 1, 0], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['10', '0']), ([0, 0, 0, 1, 0, 0], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['20', '0']), ([0, 0, 1, 0, 0, 0], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['50', '0']), ([0, 1, 0, 0, 0, 0], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['100', '0']), ([1, 0, 0, 0, 0, 0], [0, 0, 0, 0]))

    def test_coin_individual(self):
        self.assertEqual(compute_change(['0', '5']), ([0, 0, 0, 0, 0, 0], [0, 0, 1, 0]))
        self.assertEqual(compute_change(['0', '10']), ([0, 0, 0, 0, 0, 0], [0, 1, 0, 0]))
        self.assertEqual(compute_change(['0', '25']), ([0, 0, 0, 0, 0, 0], [1, 0, 0, 0]))

    def test_combination_dollar_coins(self):
        self.assertEqual(compute_change(['19', '99']), ([0, 0, 0, 1, 1, 4], [3, 2, 0, 4]))
        self.assertEqual(compute_change(['6', '36']), ([0, 0, 0, 0, 1, 1], [1, 1, 0, 1]))
        self.assertEqual(compute_change(['155', '16']), ([1, 1, 0, 0, 1, 0], [0, 1, 1, 1]))
        self.assertEqual(compute_change(['123', '87']), ([1, 0, 1, 0, 0, 3], [3, 1, 0, 2]))
        self.assertEqual(compute_change(['0', '41']), ([0, 0, 0, 0, 0, 0], [1, 1, 1, 1]))
        self.assertEqual(compute_change(['576', '0']), ([5, 1, 1, 0, 1, 1], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['186', '0']), ([1, 1, 1, 1, 1, 1], [0, 0, 0, 0]))
        self.assertEqual(compute_change(['0', '99']), ([0, 0, 0, 0, 0, 0], [3, 2, 0, 4]))
        self.assertEqual(compute_change(['345', '67']), ([3, 0, 2, 0, 1, 0], [2, 1, 1, 2]))
        self.assertEqual(compute_change(['0', '56']), ([0, 0, 0, 0, 0, 0], [2, 0, 1, 1]))
        self.assertEqual(compute_change(['1', '15']), ([0, 0, 0, 0, 0, 1], [0, 1, 1, 0]))

if __name__ == '__main__':
    unittest.main()
