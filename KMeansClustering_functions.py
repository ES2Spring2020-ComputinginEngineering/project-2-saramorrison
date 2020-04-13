#Please place your FUNCTION code for step 4 here.


    
   
  #Name: Sara Morrison

#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random

#FUNCTIONS

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
    random_centroids = np.random.random((k, 2))
    return random_centroids

def Assignments(random_centroids, glucose, hemoglobin):
    s = random_centroids.shape[0]
    distance = np.zeros((s, (158)))
    assigned_centroids = np.zeros(158)
    for i in range(s):
        h = random_centroids[i, 0]
        g = random_centroids[i, 1]
        distance[i]=(Distance(h, hemoglobin, g, glucose))
    assigned_centroids = np.argmin(distance, axis = 0)
    return assigned_centroids, distance

def Update(k, assigned_centroids, glucose, hemoglobin):
    newcentroid = np.zeros((k, 2))
    hemo_centroid = np.zeros((1))
    glucose_centroid = np.zeros((1))
    for i in range(newcentroid.shape[0]):
        hemo_centroid = np.average(hemoglobin[assigned_centroids == i])
        glucose_centroid = np.average(glucose[assigned_centroids == i])
        newcentroid[i] = np.append(hemo_centroid, glucose_centroid)
    return newcentroid

def Iterate(k, number_of_runs):
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    newcentroid = Start(k)
    for i in range(number_of_runs):
        assigned_centroids, distance = Assignments(newcentroid, glucose, hemoglobin)
        newcentroid = Update(k, assigned_centroids, glucose, hemoglobin)
    return assigned_centroids, newcentroid, glucose, hemoglobin, classification
    
def graphingKMeans(glucose, hemoglobin, assigned_centroids, newcentroid):
    plt.figure()
    for i in range(assigned_centroids.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assigned_centroids==i],glucose[assigned_centroids==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(newcentroid[i, 0], newcentroid[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()