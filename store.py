#!/usr/bin/python3
print ("Content-type:text/html\r\n\r\n");
import cgi
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import constants
import dbcon
import comparator
#from matplotlib import pyplot as plt
try:
    form = cgi.FieldStorage();
    #print form["asdf"];
    fpdata = form['fp'].value
    name = form['name'].value
    #print data
    data = comparator.compare5(fpdata)
    query = ("INSERT INTO `fingerprints`(`s1`, `s2`, `s3`, `s4`, `s5`, `name`, `fp`) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')")%(data[0],data[1],data[2],data[3],data[4],name,fpdata)
    cursor = dbcon.cnx.cursor()
    cursor.execute(query)
    dbcon.cnx.commit()
    print ("1")
except Exception as e:
    print(str(e))
