#!/usr/bin/python
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import constants
import dbcon
import base64
import comparator
dir1 = '/home/mohammed/server/FMVLD/Impression_1/fp_1/'
dir2 = '/home/mohammed/server/FMVLD/Impression_3/fp_1/'
i = 1
while(i!= 101):
    tmp1 = dir1 + str(i) + '.jpg'
    tmp2 = dir2 + str(i) + '.jpg'
    score = comparator.compareFiles(tmp1,tmp2)
    print(str(i) + "->" + str(score))
    i+=1
