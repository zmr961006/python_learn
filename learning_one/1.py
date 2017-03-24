#!/usr/bin/env python
# coding=utf-8

import sys
import os

debug = True

class FoolClass(object):
    "Fool class"
    pass

def test():
    "test function"
    foo = FoolClass()
    if debug:
        print "run test"


if __name__ == '__main__':
    test()

