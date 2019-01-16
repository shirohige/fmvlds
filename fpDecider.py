#!/usr/bin/python
import sys
sys.path.insert(0,"/home/mohammed/server/FMVLD/lib")
import constants
import dbcon
import base64
import cv2
import comparator
dir = '/home/mohammed/server/FMVLD/Impression_1/fp_1/'
sift = cv2.ORB_create()
check = 2
tmp = dir + str(check) + '.jpg'
img1 = cv2.imread(tmp,0)
kp1, des1 = sift.detectAndCompute(img1,None)
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2

search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)
i=0
while i<1001:
    i+=1
    if i == check:
        continue
    img2 = cv2.imread(dir+str(i)+'.jpg',0)
    kp2, des2 = sift.detectAndCompute(img2,None)
    matches = flann.knnMatch(des1,des2,k=2)
    good = []
    for m_n in matches:
        if len(m_n) != 2:
            continue
        (m,n) = m_n
        if m.distance < 0.75*n.distance:
            good.append(m)
    matches = flann.knnMatch(des2,des1,k=2)
    good2 = []
    for m_n in matches:
        if len(m_n) != 2:
            continue
        (m,n) = m_n
        if m.distance < 0.75*n.distance:
            good2.append(m)
    print(str(i) + ',' + str(len(good)) + ',' + str(len(good2)))
