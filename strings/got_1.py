import fileinput
import unittest
import argparse
import sys
import collections

def possible_palindrome_1(s):
    freqs = collections.defaultdict(int)
    for c in s:
        freqs[c] += 1

    odd_count = sum([v % 2 for v in freqs.values()])
    return odd_count == len(s) % 2

def possible_palindrome(s):
    return possible_palindrome_1(s)

def solve(inputs):
    for testcase in inputs:
        if possible_palindrome(testcase.strip()):
            print "YES"
        else:
            print "NO"

class Testcases(unittest.TestCase):
    def test_givens(self):
        self.assertTrue(possible_palindrome("aaabbbb"))
        self.assertTrue(possible_palindrome("cdcdcdcdeeeef"))
        self.assertFalse(possible_palindrome("cdefghmnopqrstuvw"))

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
