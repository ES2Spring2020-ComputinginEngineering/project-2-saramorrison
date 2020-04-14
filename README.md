This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

More in depth descriptions of functions are located within the files.

File Name: NearestNeighborClassification
This file graphs hemoglobin and glucose data. It also creates and graphs a test case and classifies it based on its nearest neighbor and its k number of nearest neighbors.
To run this file, specify a k value within the kNearestNeighborClassifier function.
Functions within:
openckdfile opens the ckd data and returns arrays of hemoglobin, glucose, and classification.
normalizeData normalizes the hemoglobin and glucose data and returns glucose_normalized and hemoglobin_normalized.
GraphData graphs the origininal data.
createTestCase generates random glucose and hemoglobin values and returns them as newglucose and newhemoglobin.
Distance calculates the distance between the original data points and the new test case.
calculateDistanceArray() uses the Distance() function to create an array of all of the distances and returns the array.
graphTestCase graphs the original data as well as the test case.
nearestNeighborClassifier This function finds the nearest neighbor to the test case by using the smallest distance from the Distance Array. 
kNearestNeighborClassifier takes the distance of a number of points “k” that are closest to the test case and returns the average classification of the points.

File Name: KMeansClustering_functions
This file contains functions that create centroids for data points and updates the centroids so they better fit the data. The functions also graph the data and centroids and calculate the accuracy of the assignment of the points to a centroid. 
Functions within:
openckdfile is the same as above.
normalizeData is the same as above.
Distance is the same as above
Start creates k number of random centroids.
Assignments assigns each data point in the original data point to its nearest centroid.
Update uses the assigned centroids to find an average location and updates the centroid to the average location and returns newcentroids.
Iterate runs through the Assignment function and the Update function a desired amount of times to increase accuracy of results.
graphingKMeans graphs the original data and the newcentroids.
Accuracy determines the accuracy of the assingments of points to centroids by comparing the assignments to the original classifications.

File Name: KMeansClustering_driver
This file is the driver file. It imports the functions from KMeansClustering_functions and runs them. It will display the final graph and the accuracy percentages when ran.
To run this, a k value must be specified along with a number of run times.
