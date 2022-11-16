# -*- coding: utf-8 -*-
#
# factorial.py
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

import math

def Factorial(n):
    '''
    :param n:  Operand
    :return:   n!
    '''
    print("I'm in the Factorial func!")
    return(math.factorial(n))
