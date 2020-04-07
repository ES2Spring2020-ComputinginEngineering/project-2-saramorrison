#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial import distance
import math


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    glucose_normalized = []
    hemoglobin_normalized = []
    for g in glucose:
        glucose_normalized.append((g / 70)/(490 - 70))
    for h in hemoglobin:
        hemoglobin_normalized.append((h - 3.1)/(17.8 - 3.1))
    glucose_normalized = np.array(glucose_normalized)
    hemoglobin_normalized = np.array(hemoglobin_normalized)
    return glucose_normalized, hemoglobin_normalized, classification
    

def createTestCase():
    newglucose = random.randint(1, 500)
    newhemoglobin = random.randint(1, 20)
#    plt.plot([newhemoglobin], [newglucose], marker = "o", markersize = 6, color = "limegreen")
#    plt.show
    return newhemoglobin, newglucose

def Distance(newhemoglobin, hemoglobin, newglucose, glucose):
    dist = math.sqrt(((newhemoglobin-hemoglobin)**2)+(newglucose-glucose)**2)
    return dist

def calculateDistanceArray():
    n = 0
    DistanceArray = []
    for i in classification:
        g = glucose[n]
        h = hemoglobin[n]
        DistanceArray.append(distance(newhemoglobin, h, newglucose, g))
        n += 1
    return DistanceArray



# MAIN SCRIPT
    
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
newpoint = ()
newglucose, newhemoglobin = createTestCase()




plt.figure()
createTestCase()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()