import numpy as np
import cv2
import pandas as pd
import os
import sklearn
import sys
import joblib

def IdentifyFlag(fn):
    knn=joblib.load('knn.pkl')
    
    try:    
        testimg=cv2.imread(fn)
        testimg = cv2.cvtColor(testimg, cv2.COLOR_BGR2RGB)
    except:
        print("Error: File not found!")
    else:
        dim = (5, 5)
        testimg_small = cv2.resize(testimg,dim,interpolation = cv2.INTER_AREA)
        testvec=testimg_small.flatten()
        result=knn.predict(testvec.reshape(1,-1))
        codes=pd.read_csv("data/wikipedia-iso-country-codes.csv")
        codes.set_index("Alpha-2 code", drop=True, inplace=True)
        codes=codes.to_dict(orient='index')
        print('Flag of ' + codes[result[0]]['Country'])
    
    
if __name__ == "__main__":
    IdentifyFlag(str(sys.argv[1]))