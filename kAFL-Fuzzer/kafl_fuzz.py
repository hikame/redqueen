#!/usr/bin/env python

"""
This file is part of the Redqueen fuzzer.

Sergej Schumilo, 2019 <sergej@schumilo.de> 
Cornelius Aschermann, 2019 <cornelius.aschermann@rub.de> 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Redqueen.  If not, see <http://www.gnu.org/licenses/>. 
"""

import sys
import common.color
from common.self_check import self_check

__author__ = 'sergej'

def main():
    f = open("help.txt")
    for line in f:
        print(line.replace("\n", ""))
    f.close()

    print("<< " + common.color.BOLD + common.color.OKGREEN + sys.argv[0] + ": Kernel Fuzzer " + common.color.ENDC + ">>\n")

    if not self_check():
        return 1

    from fuzzer.core import start
    return start()


if __name__ == "__main__":
    main()
