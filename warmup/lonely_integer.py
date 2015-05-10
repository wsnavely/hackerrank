import fileinput
import unittest
import argparse
import sys
import collections

def lonely_int_1(vals):
    result = 0
    for v in vals:
        result = result ^ v
    return result

def lonely_int(vals):
    return lonely_int_1(vals)

def solve(inputs):
    vals = [int(x) for x in inputs[1].split()]
    print lonely_int(vals)

class Testcases(unittest.TestCase):
    def test_givens(self):
        self.assertEquals(7, lonely_int([1,1,7]))
        self.assertEquals(7, lonely_int([7,1,1]))
        self.assertEquals(7, lonely_int([1,7,1]))
        self.assertEquals(7, lonely_int([4,2,2,3,1,7,1,3,4]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()

    if(args.test):
        suite = unittest.TestLoader().loadTestsFromTestCase(Testcases)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        inputs = [x.strip() for x in fileinput.input()]
        solve(inputs)
