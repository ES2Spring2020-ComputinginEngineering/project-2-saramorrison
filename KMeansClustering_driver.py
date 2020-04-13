#Please place your FUNCTION code for step 4 here.

import KMeansClustering_functions as kmc #Use kmc to call your functions

glucose, hemoglobin, classification = kmc.openckdfile()
glucose, hemoglobin, classification = kmc.normalizeData(glucose, hemoglobin, classification)

k = 2

assigned_centroids, newcentroid, glucose, hemoglobin, classification = kmc.Iterate(2, 100)
kmc.graphingKMeans(glucose, hemoglobin, assigned_centroids, newcentroid)