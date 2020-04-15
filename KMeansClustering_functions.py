#File Name: KMeansClustering_functions

#This file contains functions that create centroids for data points and updates the centroids so they better fit the data. The functions also graph the data and centroids and calculate the accuracy of the assignment of the points to a centroid. 

#Name: Sara Morrison
#Estimated time on this file: 3.5 hours

#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random

#FUNCTIONS

"""This function opens the ckd file.
It takes no arguments.
It returns glucose, hemoglobin, and classification."""
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

"""This function calculates the distance from the new test case with the random hemoglobin and glucose values and the original data points.
It takes four arguments: newhemoglobin, hemoglobin, newglucose, and glucose.
It returns dist"""
def Distance(h_centroid, hemoglobin, g_centroid, glucose):
    dist = np.sqrt(((h_centroid - hemoglobin)**2)+(g_centroid - glucose)**2)
    return dist

"""This function creates k number of random centroids.
It takes one argument: k.
It returns centroids, which are the random centroids."""
def Start(k):
    centroids = np.random.random((k, 2))
    return centroids

"""This function assigns each data point in the original data point to its nearest centroid.
It uses the distance function to determine the distance between the points and the centroids.
It takes three arguments: centroids, glucose, and hemoglobin.
It returns assignment and distance."""
def Assignments(centroids, glucose, hemoglobin):
    r = centroids.shape[0]
    distance = np.zeros((r, (158)))
    assignment = np.zeros(158)
    for i in range(r):
        h_centroid = centroids[i, 0]
        g_centroid = centroids[i, 1]
        distance[i]=(Distance(h_centroid, hemoglobin, g_centroid, glucose))
    assignment = np.argmin(distance, axis = 0)
    return assignment, distance

"""This function uses the assigned centroids to find an average location and updates the centroid to the average location.
It takes four arguments: k, assignment, glucose, and hemoglobin.
It returns the newcentroid, which are the new centroid locations."""
def Update(k, assignment, glucose, hemoglobin):
    newcentroid = np.zeros((k, 2))
    hemo_centroid = np.zeros((1))
    glucose_centroid = np.zeros((1))
    for i in range(newcentroid.shape[0]):
        hemo_centroid = np.average(hemoglobin[assignment == i])
        glucose_centroid = np.average(glucose[assignment == i])
        newcentroid[i] = np.append(hemo_centroid, glucose_centroid)
    return newcentroid

"""This function runs through the Assignment function and the Update function a desired amount of times to increase accuracy of results.
It takes two arguments: k and number_of_runs.
It returns assignment, newcentroid, glucose, hemoglobin, and classification."""
def Iterate(k, number_of_runs):
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    newcentroid = Start(k)
    for i in range(number_of_runs):
        assignment, distance = Assignments(newcentroid, glucose, hemoglobin)
        newcentroid = Update(k, assignment, glucose, hemoglobin)
    return assignment, newcentroid, glucose, hemoglobin, classification
 
"""This function graphs the centroids and the original data, assigining the original data points to centroids.
It takes four arguments: glucose, hemoglobin, assignment, and newcentroid.
It is a void function"""
def graphingKMeans(glucose, hemoglobin, assignment, newcentroid):
    plt.figure()
    for i in range(int(np.amax(assignment))+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(newcentroid[i, 0], newcentroid[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
 
"""This function determines the accuracy of the assingments of points to centroids by comparing the assignments to the original classifications.
It takes two argumments: classification and assignment.
It prints the accuracies as percentages, but has no return value"""
def Accuracy(classification, assignment):
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0
    CKD = 0
    No_CKD = 0
    for i in range(158):
        if classification[i] == assignment[i] == 1:
            true_negatives = true_negatives + 1
            No_CKD = No_CKD + 1
        if classification[i] == 1 and assignment[i] == 0:
            false_positives = false_positives + 1
            No_CKD = No_CKD + 1
        if classification[i] == assignment[i] == 0:
            true_positives = true_positives + 1
            CKD = CKD + 1
        if classification[i] == 0 and assignment[i] == 1:
            false_negatives = false_negatives + 1
            CKD = CKD + 1
    print("The Rate of True Positives is " + str((true_positives / CKD)*100)+ " %")
    print("The Rate of True Negatives is " + str((true_negatives / No_CKD)*100) + " %")
    print("The Rate of False Positives is " + str((false_positives / No_CKD)*100) + " %")
    print("The Rate of False Negatives is " + str((false_negatives / CKD)*100) + " %")

   