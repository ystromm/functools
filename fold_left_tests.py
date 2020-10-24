import unittest

#from src.reduce import reduce

# foldLeft(f, init, lista)
# foldleft(f, init, []) = init
# foldleft(f, init, [a]) = f(init, a)
# foldleft(f, init, [a1, a2]) = f(f(init, a1), a2)
#
# foldleft(+, 0, [1]) = 0+1
# foldleft(+, 0, [1, 2]) = f(f(0,1), 2) = 0+1+2 = 3

# reduce(+, []) => ValueError
# reduce(+, [], 1) => 1
# reduce(+, [1]) => 1
# reduce(+, [1, 1]) => 2
# reduce(+, [1], 1) => 2
from functools import reduce

from src.fold_left import fold_left


def f(a: str, b: int):
    return a+str(b)

# print(reduce(f, [], "0"))
#
# print(reduce(f, [1], "0"))
# print(reduce(f, ["0", 1]))
#
# print(reduce(f, [1, 2], "0"))

def x(b,a):
    return b + [a+1]

class ReduceTestCase(unittest.TestCase):

    def test_should_return_init(self):
        self.assertEqual(0, fold_left(lambda x,y: x+y, 0, []))

    def test_should_return_sum_for_a_very_short_list(self):
        self.assertEqual(1, fold_left(lambda x,y: x+y, 0, [1]))

    def test_should_return_sum(self):
        self.assertEqual(3, fold_left(lambda x,y: x+y, 0, [1,2]))

    def test_something(self):
        self.assertEqual("12", fold_left(f, "", [1,2]))

    def test_something_else(self):
        self.assertEqual([2,3], fold_left(x, [], [1,2]))


    def test_empty_list(self):
        reduce(lambda x, y: x + y, [])

    def test_bad_value(self):
        reduce(lambda x, y: x + y, None)

    def test_strange_value(self):
        self.assertEqual("", reduce(lambda x, y: x + y+"-", "abc", ""))

if __name__ == '__main__':
    unittest.main()
