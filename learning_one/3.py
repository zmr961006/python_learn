#!/usr/bin/env python
# coding=utf-8

fname = raw_input('>')
print

try:
    fobj = open(fname,'r')

except IOError,e:
    print "**** file open error:",e

else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()
