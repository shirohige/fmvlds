#!/usr/bin/python
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import dbcon
sql = ("SELECT *FROM `fingerprints` WHERE 1")
cursor = dbcon.cnx.cursor()
cursor.execute(sql)
row = cursor.fetchone()
print('fp_id,s1,s2,s3,s4,s5,name')
while row is not None:
    print(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(row[4]) + ',' + str(row[5]) + ',' + str(row[6]))
    row = cursor.fetchone()
