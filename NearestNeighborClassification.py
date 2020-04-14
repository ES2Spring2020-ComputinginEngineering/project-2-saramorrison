#File Name: Nearest Neighbor Classification

#This file graphs hemoglobin and glucose data. It also creates a test case and classifies it based on its nearest neighbor and its k number of nearest neighbors.

#Name: Sara Morrison
#Estimated Time on this file: 3 hours

# IMPORT STATEMENTS

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial import distance
import math


# FUNCTIONS

"""This function opens the ckd file with the glucose, hemoglobin, and classification data.
It takes no arguments and returns the arrays glucose, hemoglobin, and classification."""
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

"""This function normalizes the three arrays.
It takes three arguements: glucose, hemoglobin, and classification.
It returns glucose_normalized, hemoglobin_normalized, and classification"""
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

"""This function is a void function and graphs the glucose and hemoglobin data and shows the classification.
It takes three arguments: glucose, hemoglobin, and classification"""
def GraphData(glucose, hemoglobin, classification):
    plt.figure()
    createTestCase()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()    

"""This function generates random glucose and hemoglobin values.
It takes no arguments and returns newhemoglobin and newglucose."""
def createTestCase():
    newglucose = random.uniform(0, 1)
    newhemoglobin = random.uniform(0, 1)
    return newhemoglobin, newglucose

"""This function calculates the distance from the new test case with the random hemoglobin and glucose values and the original data points.
It takes four arguments: newhemoglobin, hemoglobin, newglucose, and glucose
It returns dist"""
def Distance(newhemoglobin, hemoglobin, newglucose, glucose):
    dist = math.sqrt(((newhemoglobin-hemoglobin)**2)+(newglucose-glucose)**2)
    return dist

"""This function creates a 1D array, DistanceArray. It uses the Distance function.
It takes four arguments: glucose, newglucose, hemoglobin, newhemoglobin.
It returns the DistanceArray"""
def calculateDistanceArray(glucose, newglucose, hemoglobin, newhemoglobin):
    n = 0
    DistanceArray = []
    for i in classification:
        g = glucose[n]
        h = hemoglobin[n]
        DistanceArray.append(Distance(newhemoglobin, h, newglucose, g))
        n += 1
    return DistanceArray

"""This function graphs the original data and the test case created in the createTestCase function.
It take five arguments: newglucose, newhemoglobin, glucose, hemoglobin, and classification.
It is a void function."""
def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend() 
    plt.plot([newhemoglobin], [newglucose], marker = "o", markersize = 6, color = "limegreen")
    plt.show

"""This function finds the nearest neighbor to the test case by using the smallest distance from the Distance Array.
It takes five arguments: newglucose, newhemoglobin, glucose, hemoglobin, and classification.
It returns the classification of the smallest difference."""
def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distances = calculateDistanceArray(glucose, newglucose, hemoglobin, newhemoglobin)
    smallestDistance = np.argmin(distances)
    return classification[smallestDistance]

"""This function takes the distance of a number of points “k” that are closest to the test case and returns the average classification of the points.
It takes six arguments: k, newglucose, newhemoglobin, glucose, hemoglobin, and classification.
It returns k_classifications, which is the classifications of each point, and final_classification, which is the classification of the majority of the points"""   
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    CKD = 0
    no_CKD = 0
    final_classification = 0
    sorted_indices = np.argsort(distance)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    for i in k_classifications:
        if i == 0:
           CKD = 1 + CKD
        if i == 1:
            no_CKD = 1 + no_CKD
    if no_CKD > CKD:
        final_classification = 1.0
    else:
        final_classification = 0.0
    print(k_classifications, final_classification)
    

# MAIN SCRIPT
    
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
newpoint = ()
newglucose, newhemoglobin = createTestCase()
distance = calculateDistanceArray(glucose, newglucose, hemoglobin, newhemoglobin)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
kNearestNeighborClassifier(4, newglucose, newhemoglobin, glucose, hemoglobin, classification)
