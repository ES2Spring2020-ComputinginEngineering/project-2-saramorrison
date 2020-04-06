#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial import distance


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def createTestCase():
    newglucose = random.randint(1, 500)
    newhemoglobin = random.randint(1, 20)
    plt.plot([newhemoglobin], [newglucose], marker = "o", markersize = 6, color = "limegreen")
    return newhemoglobin, newglucose
    plt.show

def calculateDistanceArray():
    newglucose = random.randint(1, 500)
    newhemoglobin = random.randint(1, 20)
    a = (newhemoglobin, newglucose)
    b = (hemoglobin, glucose)
    dist = distance.euclidean(a, b)
    return np.array(dist)

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

calculateDistanceArray()

plt.figure()
createTestCase()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()