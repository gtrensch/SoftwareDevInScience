# -*- coding: utf-8 -*-
#
# test_gt.py

# Unit test: 'g'.

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.g import *

class TestFactorial(unittest.TestCase):

    def test_value_0(self):
        self.assertEqual(g(0), 0)

    def test_value_1(self):
        self.assertEqual(g(1), 4.505223801027239e-17 )


def suite():
    suite = unittest.makeSuite(Testg, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
