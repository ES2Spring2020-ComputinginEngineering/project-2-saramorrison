#File Name: KMeansClustering_driver

#This file is the driver file. It imports the functions from KMeansClustering_functions and runs them. It will display the final graph and the accuracy percentages when ran.

#Name: Sara Morrison
#Estimated time on this file: .25 hours

import KMeansClustering_functions as kmc #Use kmc to call your functions

glucose, hemoglobin, classification = kmc.openckdfile()  #opens file
glucose, hemoglobin, classification = kmc.normalizeData(glucose, hemoglobin, classification)  #assigns glucose, hemoglobin, and classificaiton to the normalized data

k = 2  #assigns a k value, can be changed if desired

number_of_runs = 100  #number of times that Iterate will be run, can be changed

assignment, newcentroid, glucose, hemoglobin, classification = kmc.Iterate(k, number_of_runs)  #runs the Iterate function with desired k value and number of runs
kmc.graphingKMeans(glucose, hemoglobin, assignment, newcentroid)  #runs the graphing function with the outputs of the Iterate function

kmc.Accuracy(classification, assignment)  #runs the accuracy function with the outputs from the iterate function