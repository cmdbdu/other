#coding:utf8
import os
import os.path
import sys
import fileinput
rootdir = sys.argv[1]                                   

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        for line in fileinput.input(os.path.join(parent, filename)):
            if line.startswith(sys.argv[2]):
                pass
            elif line.strip() == '':
                pass
            else:
                print line.rstrip()
