import fileinput
import unittest
import argparse
import sys
import collections

def xors(l, r):
    for x in xrange(l,r+1):
        yield l ^ x

def max_xor_1(l,r):
    result = 0
    for x in xrange(l,r+1):
        result = max(max(xors(x,r)), result)
    return result

def max_xor(l,r):
    return max_xor_1(l,r)

def solve(inputs):
    l, r = [int(x) for x in inputs]
    print max_xor(l,r)

class Testcases(unittest.TestCase):
    def test_givens(self):
        self.assertEquals(7, max_xor(10,15))

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
