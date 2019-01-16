#!/usr/bin/python3
print "Content-type:text/html\r\n\r\n";
import cgi
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import constants
import dbcon
import comparator
try:
    form = cgi.FieldStorage();
    #print form["asdf"];
    fpdata = form["fp"].value
    #print data # below 3 lines used to store fingerprints temporary for debugging
    #fh = open("tmp1.png", "wb")
    #fh.write(fpdata.decode('base64'))
    #fh.close()
    data = comparator.compare5(fpdata)
    sql = ("SELECT *,SQRT(POWER(s1-\'%s\',2)+POWER(s2-\'%s\',2)+POWER(s3-\'%s\',2)+POWER(s4-\'%s\',2)+POWER(s5-\'%s\',2)) as distance FROM `fingerprints` WHERE 1 order by distance ASC") % (data[0],data[1],data[2],data[3],data[4])
    cursor = dbcon.cnx.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cnt = 0
    while row is not None:
        print(str(row[0])+ " "+str(row[8])+ " " + str(comparator.comparebase64(row[7],fpdata)))
        cnt = cnt+1;
        if comparator.comparebase64(row[7],fpdata) > 50 :
            print(cnt)
            sys.exit()
        row = cursor.fetchone()
    print("0")
except Exception, e:
    print str(e)
