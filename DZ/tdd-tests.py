import unittest
import math
import time
from itertools import islice
from main import createF, use_generator

class TestFib(unittest.TestCase):
    def test_createF(self):
        self.assertEqual(createF(0), 0)
        self.assertEqual(createF(-4), -3)
        self.assertEqual(createF(10), 55)

    def test_use_generator(self):
        self.assertEqual(list(use_generator(0)), [0])
        self.assertEqual(list(use_generator(-10)), [0, 1, -1, 2, -3, 5, -8, 13, -21, 34])
        self.assertEqual(list(use_generator(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        time1 = time.time()
        a = list(islice(use_generator(1000), 500))
        time2 = time.time()
        b = list(islice([createF(x) for x in range(1000)], 500))
        time3 = time.time()
        self.assertLess(time2 - time1, time3 - time2, "Это не ленивые вычисления.")


if __name__ == "__main__":
    unittest.main()