# -*- coding: utf-8 -*-
#
# test_factorial.py
#
# This file is part of PrintNumbers.
#
# Copyright (C) 2017 G. Trensch, Simulation & Datalab Neuroscience, JSC, FZ Juelich
#
# PrintNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PrintNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrintNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Unit tests: 'factorial'.
#

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.factorial import *

class TestFactorial(unittest.TestCase):

    def test_value_0(self):
        self.assertEqual(Factorial(0), 1)

    def test_value_1(self):
        self.assertEqual(Factorial(1), 1)

    def test_value_2(self):
        self.assertEqual(Factorial(2), 2)

    def test_value_20(self):
        self.assertEqual(Factorial(20), 2432902008176640000)


def suite():
    suite = unittest.makeSuite(TestFactorial, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
