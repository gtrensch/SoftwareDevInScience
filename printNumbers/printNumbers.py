# -*- coding: utf-8 -*-
#
# printNumbers.py
#
# This file is part of printNumbers.
#
# Copyright (C) 2017 G. Trensch, Simulation & Datalab Neuroscience, JSC, FZ Juelich
#
# printNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# printNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with printNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Software Development in Science Workshop
#     Python GitHub project example
#

"""
Usage:
  printNumbers.py -h --help
  printNumbers.py [--fibonacci|--factorial|--gaussiansummation] <operand>

Options:
  -h --help               Print usage.
  --fibonacci             Print the fibonacci sequence.
  --factorial             Print the factorial.
  --gaussiansummation     Print the sum of the first n integers
"""

from docopt import docopt
from parameters import *
from functions.fibonacci import *
from functions.factorial import *
from functions.gaussian_summation import *

#
# FUNCTION TABLE
#
functionTable = { CONST_FUNC_CODE_FIBONACCI : FibonacciRecursion,
                  CONST_FUNC_CODE_FACTORIAL : Factorial,
                  CONST_FUNC_CODE_GAUSSIAN_SUMMATION : GaussianSummation,
                }

#
# MAIN ENTRY
#
if __name__ == '__main__':
    print('')
    print(CONST_VERSION_STRING)
    print('')

    # Process command line arguments.
    params = Parameters(docopt(__doc__, version = CONST_VERSION))
    params.PrintParameters()

    # Call corresponding function with <functionIndex> from <functionTable>.
    result = functionTable[params.functionIndex](params.operand)

    # Print results depending on the executed function.
    if params.functionIndex == CONST_FUNC_CODE_FIBONACCI:
        print('fib(' + str(params.operand) + ') =', result)
    elif params.functionIndex == CONST_FUNC_CODE_FACTORIAL:
        print(str(params.operand) + '! =', str(result))
    elif params.functionIndex == CONST_FUNC_CODE_GAUSSIAN_SUMMATION:
        print('gaussian_summation(' + str(params.operand) + ') =', result)
