# ab-Initio Configuration Sampling tool kit (abICS)
# Copyright (C) 2019- The University of Tokyo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.

class Error(Exception):
    """Base class for exceptions in abICS"""
    pass


class InputError(Error):
    """Exception raised for errors in the input

    Attributes
    ----------
    message: str
        explanation
    """
    def __init__(self, message):
        self.message = message


class MatrixParseError(Error):
    """Exception raised for matrix parse errors

    Attributes
    ----------
    message: str
        explanation
    """
    def __init__(self, message):
        self.message = message
