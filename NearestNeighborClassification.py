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
        glucose_normalized.append((g - 70)/(420))
    for h in hemoglobin:
        hemoglobin_normalized.append((h - 3.1)/(14.7))
    glucose_normalized = np.array(glucose_normalized)
    hemoglobin_normalized = np.array(hemoglobin_normalized)
    return glucose_normalized, hemoglobin_normalized, classification

def GraphData(glucose, hemoglobin, classification):
    plt.figure()
    createTestCase()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()    

def createTestCase():
    newglucose = random.uniform(0, 1)
    newhemoglobin = random.uniform(0, 1)
    return newhemoglobin, newglucose

def Distance(newhemoglobin, hemoglobin, newglucose, glucose):
    dist = math.sqrt(((newhemoglobin-hemoglobin)**2)+(newglucose-glucose)**2)
    return dist

#def calculateDistanceArray(newglucose, glucose, newhemoglobin, hemoglobin):
#    n = 0
#    DistanceArray = []
#    for i in classification:
#        g = glucose[n]
#        h = hemoglobin[n]
#        DistanceArray.append(Distance(newhemoglobin, h, newglucose, g))
#        n += 1
#    return DistanceArray

def calculateDistanceArray(newglucose, glucose, newhemoglobin, hemoglobin):
    dist = np.sqrt(((newhemoglobin - hemoglobin)**2) + (newglucose - glucose)**2)
    return dist

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend() 
    plt.plot([newhemoglobin], [newglucose], marker = "o", markersize = 6, color = "limegreen")
    plt.show

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distances = calculateDistanceArray()
    smallestDistance = np.argmin(distances)
    return(classification(smallestDistance))
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    zeros = 0
    ones = 0
    classMajority = 0
    sorted_indices = np.argsort(distance)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    for i in k_classifications:
        if i == 0:
            zeros = 1 + zeros
        if i == 1:
            ones = 1 + ones
    if ones > zeros:
        classMajority = 1.0
    else:
        classMajority = 0.0
    return k_classifications, classMajority
    

# MAIN SCRIPT
    
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
newpoint = ()
newglucose, newhemoglobin = createTestCase()
distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)

