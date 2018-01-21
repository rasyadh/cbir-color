import numpy as np
import csv
import json

class Searcher:
    def __init__(self, indexPath):
        # Store our index path
        self.indexPath = indexPath

    def search(self, queryFeature, limit = 10):
        # Init dictionary result
        results = {}

        # Open the index file for reading
        with open(self.indexPath) as f:
            # Load json features
            data = json.load(f)

            # Init features
            features = []

            # Loop over the row
            for row in data['features']:
                # Get feature each region
                features.append(row['region_1'])
                features.append(row['region_2'])
                features.append(row['region_3'])
                features.append(row['region_4'])

                # Compute distance with chi-squared
                d = self.chi2_distance(features, queryFeature)
 
				# Update result dict with imageID and distance
                results[row['name']] = d

                # Clear features
                features = []
 
			# Close the reader
            f.close()

		# sort our results, so that the smaller distances at first
		# (i.e. the more relevant images are at the front of the list)
        results = sorted([(v, k) for (k, v) in results.items()])
 
		# return our (limited) results
        return results[:limit]

    def chi2_distance(self, histA, histB, eps=1e-10):
        # Compute chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
 
		# return the chi-squared distance
        return d