#!/usr/bin/python
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import constants
import dbcon
import base64
import comparator
import random
dir = '/home/mohammed/server/FMVLD/Impression_1/fp_1/'
dir2 = '/home/mohammed/server/FMVLD/Impression_1/fp_1/'
i=0
for x in range(100):
    i = random.randint(1,1001)
    tmp = dir + str(i) + '.jpg'
    tmp2 = dir2 + str(i) + '.jpg'
    image = open(tmp, 'rb')
    image_read = image.read()
    fpdata = base64.encodestring(image_read)
    data = comparator.compare5(fpdata)
    sql = ("SELECT *,SQRT(POWER(s1-\'%s\',2)+POWER(s2-\'%s\',2)+POWER(s3-\'%s\',2)+POWER(s4-\'%s\',2)+POWER(s5-\'%s\',2)) as distance FROM `fingerprints` WHERE 1 order by distance ASC") % (data[0],data[1],data[2],data[3],data[4])
    cursor = dbcon.cnx.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cnt = 0
    while row is not None:
        cnt+=1
        if row[6] == tmp2:
            print(str(row[0])+ ',' + str(cnt))
        row = cursor.fetchone()
