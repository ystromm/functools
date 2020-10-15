import unittest

from src.reduce import reduce

# reduce(+, []) => ValueError
# reduce(+, [], 1) => 1
# reduce(+, [1]) => 1
# reduce(+, [1, 1]) => 2
# reduce(+, [1], 1) => 2

class ReduceTestCase(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
