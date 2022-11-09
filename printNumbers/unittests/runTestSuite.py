# -*- coding: utf-8 -*-
#
# runTestSuite.py
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
# Run unit test suite.
#

import unittest

import test_factorial
import test_fibonacci


def suite():
    suite = unittest.TestSuite()

    suite.addTest(test_factorial.suite())
    suite.addTest(test_fibonacci.suite())

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())
