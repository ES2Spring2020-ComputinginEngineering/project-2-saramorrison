#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


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

def Distance(newhemoglobin, hemoglobin, newglucose, glucose):
    dist = np.sqrt(((newhemoglobin - hemoglobin)**2)+(newglucose - glucose)**2)
    return dist

def Start(k):
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    centroids = array = np.random.random((k, 2))
    return centroids

def Assignments(k, centroid):
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    distance = np.zeros((len(glucose), k))
    for i in range(k):
        distance1 = np.array(Distance(centroid[i, 1], hemoglobin, centroid[i, 0], glucose))
        distance[:, i] = distance1
    assignment = np.zeros(len(glucose))
    for i in range(len(glucose)):
        min = np.argmin(distance[i])
        assignment[i] = min
    assignment = np.argmin(distance, axis = 0)
    return assignment

def Update(k, assignment):
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    newcentroid = np.zeros((k, 2))
    for x in range(k):
        glucose_centroid = np.zeros((1))
        hemo_centroid = np.zeros((1))
        assign_centroid, = np.where(assignment == x)
        for i in assign_centroid:
            glucose_centroid = np.append(glucose_centroid, [glucose[i]])
            hemo_centroid = np.append(hemo_centroid, [hemoglobin[i]])
        newcentroid[x:, 1] = np.average(glucose_centroid)
        newcentroid[x:, 0] = np.average(hemo_centroid)
    return newcentroid

def Iterate(k, number_of_runs):
    centroid = Start(k)
    for i in range(number_of_runs):
        assignment = Assignments(k, centroid)
        centroid = Update(k, assignment)
    return assignment, centroid
    
def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    plt.figure()
    for i in range(int(np.amax(assignment))+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()