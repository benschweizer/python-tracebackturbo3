#!/usr/bin/env python3

import tracebackturbo as traceback

def erroneous_function():
    ham = u"unicode string with umlauts äöü."
    eggs = "binary string with umlauts äöü."
    i = 23
    if i>5:
        raise Exception("it's a trap!")

try:
    erroneous_function()
except:
    print(traceback.format_exc())
