#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from clint.textui import colored

text = 'THIS TEXT IS COLORED %s!'

if __name__ == '__main__':

	for color in colored.__all__:
		print getattr(colored, color)(text % color.upper())