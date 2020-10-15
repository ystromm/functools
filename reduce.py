import unittest

from src.reduce import reduce

# reduce(+, []) => ValueError
# reduce(+, [], 1) => 1
# reduce(+, [1]) => 1
# reduce(+, [1, 1]) => 2
# reduce(+, [1], 1) => 2

class MyTestCase(unittest.TestCase):
    def test_reduce_should_return_none(self):
        # should this example raise typerror
        self.assertEqual(reduce(lambda a, b: b, []), None)

    def test_reduce_should_return_initializer(self):
        self.assertEqual(reduce(lambda a, b: b, [], 1), 1)

    def test_reduce_should_return_last_value(self):
        self.assertEqual(reduce(lambda a, b: b, [1]), 1)

    def test_reduce_should_return_sum_of_initializer(self):
        self.assertEqual(reduce(lambda a, b: a+b, [2], 1), 3)

    def test_reduce_should_raise(self):
        with self.assertRaises(ValueError):
            reduce(lambda a, b: a+b, [2])

    def test_reduce_should_return_sum(self):
        self.assertEqual(reduce(lambda a, b: a + b, [1, 2]), 3)


if __name__ == '__main__':
    unittest.main()
