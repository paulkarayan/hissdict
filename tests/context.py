# -*- coding: utf-8 -*-

#this is used to get around the relative import challenges
# see: http://stackoverflow.com/questions/11536764/attempted-relative-import-in-non-package-even-with-init-py

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import hissdict
