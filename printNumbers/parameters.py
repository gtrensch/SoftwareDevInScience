# -*- coding: utf-8 -*-
#
# parameters.py
#
## This file is part of printNumbers.
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
# Class to process and store program parameters.
#

CONST_VERSION = 'V1.0'
CONST_VERSION_STRING = '+ + PrintNumbers ' + CONST_VERSION + ' (Software Development in Science) + +'
CONST_DEF_OPERAND_VAL = 100
CONST_MAX_OPERAND_VAL = 20=
CONST_FUNC_CODE_FIBONACCI = 0
CONST_FUNC_CODE_FACTORIAL = 10

class Parameters(object):

    def __init__(self, cmdLineArgs):
        self.operand = CONST_DEF_OPERAND_VAL
        self.functionIndex = CONST_FUNC_CODE_FIBONACCI
        self.__setParameters(cmdLineArgs)

    def __setParameters(self, cmdLineArgs):
        self.operand = (int(cmdLineArgs['<operand>']))
        if cmdLineArgs['--fibonacci']:
            self.functionIndex = CONST_FUNC_CODE_FIBONACCI
        elif cmdLineArgs['--factorial']:
            self.functionIndex = CONST_FUNC_CODE_FACTORIAL

    @property
    def operand(self):
        return(self.__operand)

    @operand.setter
    def operand(self, n):
        if n <= 0 or n > CONST_MAX_OPERAND_VAL:
            print('Error: Operand out of range: 0 < <operand> <=', CONST_MAX_OPERAND_VAL)
            print('       The default value ( n =', CONST_DEF_OPERAND_VAL, ') is used.')
            print('')
            n = CONST_DEF_OPERAND_VAL
        self.__operand = n

    @property
    def functionIndex(self):
        return(self.__functionIndex)

    @functionIndex.setter
    def functionIndex(self, value):
        self.__functionIndex = value

    def PrintParameters(self):
        print('Following Parameters are in use:')
        print('--------------------------------')
        print('Function Code: ', self.functionIndex)
        print('Operand value: ' + str(self.operand))
        print('')
