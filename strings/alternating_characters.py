import fileinput
import unittest
import argparse
import sys

def count_deletions_1(s):
    return sum([int(s[i]==s[i+1]) for i in xrange(len(s)-1)])

def count_deletions(s):
    return count_deletions_1(s)

def solve(inputs):
    testcases = inputs[1:]
    for testcase in testcases:
        print count_deletions(testcase.strip())

class Testcases(unittest.TestCase):
    def test_givens(self):
        self.assertEquals(count_deletions("AAAA"), 3)
        self.assertEquals(count_deletions("BBBBB"), 4)
        self.assertEquals(count_deletions("ABABABAB"), 0)
        self.assertEquals(count_deletions("BABABA"), 0)
        self.assertEquals(count_deletions("AAABBB"), 4)

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
