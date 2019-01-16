#!/usr/bin/python
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import constants
import dbcon
import base64
import comparator
dir = '/home/mohammed/server/FMVLD/Impression_3/fp_1/'
tmp = dir + '6.jpg'
print(tmp)
image = open(tmp, 'rb')
image_read = image.read()
fpdata = base64.encodestring(image_read)
data = comparator.compare5(fpdata)
sql = ("SELECT *,SQRT(POWER(s1-\'%s\',2)+POWER(s2-\'%s\',2)+POWER(s3-\'%s\',2)+POWER(s5-\'%s\',2)) as distance FROM `fingerprints` WHERE 1 order by distance ASC") % (data[0],data[1],data[2],data[4])
cursor = dbcon.cnx.cursor()
cursor.execute(sql)
row = cursor.fetchone()
cnt = 0
while row is not None:
    '''print(str(row[0])+ " "+str(row[8])+ " " + str(comparator.comparebase64(row[7],fpdata)))
    print("here")'''
    cnt = cnt+1;
    score = comparator.compareFiles(row[6],tmp)
    print(str(row[6]) + ' Distance ' + str(row[8]) + ' Score :' + str(score))
    if score > 50:
        print(cnt)
        sys.exit()
    '''if comparator.comparebase64(row[7],fpdata) > 100 :
        print(cnt)
        sys.exit()'''
    row = cursor.fetchone()
