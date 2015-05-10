import fileinput
import unittest
import argparse
import sys
import collections

def is_kaprekar(n):
    square = str(n*n)
    digits = len(str(n))
    split = len(square) - digits
    r = square[split:]
    l = square[:split]

    ri = int(r)
    if len(l) == 0:
        return n == ri
    else:
        li = int(l)
        return li > 0 and ri > 0 and n == li + ri

def kaprekar_1(p,q):
    for n in range(p,q+1):
        if is_kaprekar(n):
            yield n

def kaprekar(p,q):
    return kaprekar_1(p,q)

def solve(inputs):
    p = int(inputs[0])
    q = int(inputs[1])
    result = list(kaprekar(p,q))
    if len(result) == 0:
        print "INVALID RANGE"
    else:
        print " ".join([str(x) for x in result])

class Testcases(unittest.TestCase):
    def test_givens(self):
        self.assertEquals([1,9,45,55,99], list(kaprekar(1,100)))

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
