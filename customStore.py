#!/usr/bin/python
import sys #Import for next statement
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib") # Import for custom libraries
import constants # Constants used in code
import dbcon # DB connection object
import base64 #Base64 enocding and decoding for http transfers
import cv2 # Import openCV 3.4
import comparator # Functions to compare fingerprints
dir = '/home/mohammed/server/FMVLD/Impression_1/fp_1/' # directory to pick fingerprints from
i = 147
while i != 148: # run from 1 to 1000
    tmp = dir+str(i)+'.jpg' # file name generated
    image = open(tmp, 'rb')
    image_read = image.read()
    fpdata = base64.encodestring(image_read) # calculate base64, for compare5 function
    data = comparator.compare5(fpdata) # get comparision scores for 5 templates
    print(str(data[0]) + " " + str(data[1]) + " " + str(data[2]) + " "+ str(data[3]) + " "+ str(data[4]) + " ")
    query = ("INSERT INTO `fingerprints`(`s1`, `s2`, `s3`, `s4`, `s5`, `name`, `fp`) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\"%s\")")%(data[0],data[1],data[2],data[3],data[4],tmp,fpdata)
    #sql Query to insert the data
    cursor = dbcon.cnx.cursor() # get cursor to execute query
    cursor.execute(query)
    #dbcon.cnx.commit() # commit changes
    print("Added Fingerprint "+ tmp) # print log
    i+=1


'''
image = open('/home/mohammed/server/FMVLD/', 'rb')
image_read = image.read()
fpdata = base64.encodestring(image_read)
data = comparator.compare5(fpdata)
query = ("INSERT INTO `fingerprints`(`s1`, `s2`, `s3`, `s4`, `s5`, `name`, `fp`) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')")%(data[0],data[1],data[2],data[3],data[4],name,fpdata)
cursor = dbcon.cnx.cursor()
cursor.execute(query)
dbcon.cnx.commit()
'''
