#!/usr/bin/env python
# coding=utf-8

import types

num = 'hello world'

def display(num):
    print num ,'is',
    if isinstance(num,(int,long,float,complex)):
        print 'a number of type:',type(num).__name__
    else:
        print 'not a number at all !!'

