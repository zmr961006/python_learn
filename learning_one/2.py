#!/usr/bin/env python
# coding=utf-8

import os
import sys
ls = os.linesep

fname = '2.cc'

while True:

    if os.path.exists(fname):
        print "ERROR '%s' already exits" % fname
        sys.exit()
    else:
        break

all = []

print 'please enter file name '

while True:
    entry= raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s' % (x) for x in all])
fobj.close()
print 'Done'


