import unittest
from lab_3.jackie_and_bananas import count_eating_speed


class Lab3Test(unittest.TestCase):
    def test_given_examples(self):
        self.assertEqual(count_eating_speed([3, 6, 7, 11], 8), 4)
        self.assertEqual(count_eating_speed([30, 11, 23, 4, 20], 6), 23)

    def test_edge_cases(self):
        self.assertEqual(count_eating_speed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(count_eating_speed([30, 30, 30, 30, 30], 5), 30)
        self.assertEqual(count_eating_speed([5, 2, 1, 3, 2], 15), 1)
        self.assertEqual(count_eating_speed([5, 2, 1, 3, 7], 18), 1)

    def test_bad_input(self):
        self.assertRaises(ValueError, count_eating_speed, [2, 5, 19, 84], 3)
        self.assertRaises(TypeError, count_eating_speed, [1, 22, 4, 5, 'a'], 7)
        self.assertRaises(TypeError, count_eating_speed, [1, 22, 4, [1, 3, 4], 7], 7)
        self.assertRaises(TypeError, count_eating_speed, [1, 22, 4, '1', 7], 7)
        self.assertRaises(TypeError, count_eating_speed, [2, 5, 19, 84], "15")


if __name__ == '__main__':
    unittest.main()
