import fileinput
import unittest
import argparse
import sys

def is_funny_1(s):
    diffs = [abs(ord(s[i]) - ord(s[i+1])) for i in xrange(len(s)-1)]
    return diffs == list(reversed(diffs))

def is_funny_2(s):
    for ii in xrange(len(s) / 2):
        diff1 = abs(ord(s[ii]) - ord(s[ii+1]))
        diff2 = abs(ord(s[-(ii+1)]) - ord(s[-(ii+2)]))
        if diff1 != diff2:
            return False
    return True

def is_funny(s):
    return is_funny_2(s)

def solve(inputs):
    testcases = inputs[1:]
    for testcase in testcases:
        if is_funny(testcase.strip()):
            print "Funny"
        else:
            print "Not Funny"

class Testcases(unittest.TestCase):
  def test_givens(self):
      self.assertTrue(is_funny("acxz"))
      self.assertFalse(is_funny("bcxz"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()

    if(args.test):
        suite = unittest.TestLoader().loadTestsFromTestCase(Testcases)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        inputs = [x for x in fileinput.input()]
        solve(inputs)
