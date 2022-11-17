# -*- coding: utf-8 -*-
#
# test_sum_squares.py
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
# Unit tests: 'sum_of_squares'.
#

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.sum_squares import *

class TestSum_of_squares(unittest.TestCase):

    def test_value_neg(self):
        self.assertEqual(Sum_of_squares(-2), 0)

    def test_value_0(self):
        self.assertEqual(Sum_of_squares(0), 0)

    def test_value_1(self):
        self.assertEqual(Sum_of_squares(1), 1)

    def test_value_2(self):
        self.assertEqual(Sum_of_squares(2), 5)

    def test_value_3(self):
        self.assertEqual(Sum_of_squares(3), 14)

    def test_value_10(self):
        self.assertEqual(Sum_of_squares(10), 10 * 11 * 21 / 6)


def suite():
    suite = unittest.makeSuite(TestSum_of_squares, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
