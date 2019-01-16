import numpy as np
import cv2
import base64
from matplotlib import pyplot as plt
def compare5(encoded_string):
    FLANN_INDEX_LSH = 6
    index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    img2 = base64.b64decode(encoded_string)
    img2 = np.fromstring(img2, dtype=np.uint8)
    img2 = cv2.imdecode(img2,0)
    sift = cv2.ORB_create()
    kp2, des2 = sift.detectAndCompute(img2,None)
    test = []
    score = []
    test.append("/home/mohammed/server/FMVLD/templates/101_1.tif")
    test.append("/home/mohammed/server/FMVLD/templates/102_4.tif")
    test.append("/home/mohammed/server/FMVLD/templates/103_8.tif")
    test.append("/home/mohammed/server/FMVLD/templates/107_6.tif")
    test.append("/home/mohammed/server/FMVLD/templates/108_6.tif")
    for x in range(0,5):
        img1 = cv2.imread(test[x],0)
        kp1, des1 = sift.detectAndCompute(img1,None)
        matches = flann.knnMatch(des1,des2,k=2)
        good = []
        for m_n in matches:
            if(len(m_n) != 2):
                continue
            (m,n) = m_n
            if m.distance < 0.75*n.distance:
                good.append(m)
        score.append(len(good))
    return score
def comparebase64(target,key):
    img1 = base64.b64decode(target)
    img2 = base64.b64decode(key)
    FLANN_INDEX_KDTREE = 0
    sift = cv2.ORB_create()
    FLANN_INDEX_LSH = 6
    index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    img2 = np.fromstring(img2, dtype=np.uint8)
    img2 = cv2.imdecode(img2,0)
    img1 = np.fromstring(img1, dtype=np.uint8)
    img1 = cv2.imdecode(img1,0)
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    matches = flann.knnMatch(des1,des2,k=2)
    good = []
    for m_n in matches:
        if len(m_n) != 2:
            continue
        (m,n) = m_n
        if m.distance < 0.75*n.distance:
            good.append(m)
    return len(good)
def compareFiles(target,key):
    img1 = cv2.imread(target,0)
    img2 = cv2.imread(key,0)
    FLANN_INDEX_KDTREE = 0
    sift = cv2.ORB_create()
    FLANN_INDEX_LSH = 6
    index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    matches = flann.knnMatch(des1,des2,k=2)
    good = []
    for m_n in matches:
        if len(m_n) != 2:
            continue
        (m,n) = m_n
        if m.distance < 0.75*n.distance:
            good.append(m)
    return len(good)
