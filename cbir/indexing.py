from cbir.colordescriptor import ColorDescriptor
import os, json
import cv2
import csv
import numpy as np

class Indexing():
    def indexer():
        # Dataset PATH
        PATH_DATASET = "project/static/dataset/"

        # Initialize ColorDescriptor and bins
        descriptor = ColorDescriptor((8, 12, 3))

        # Init dataset features
        dataset_features = {}
        dataset_features['features'] = []

        # Iterate through PATH_DATASET
        for imagePath in os.listdir(PATH_DATASET):
            # Extract image ID
            imageID = imagePath
            
            # Load image
            image = cv2.imread(PATH_DATASET + imagePath)
            
            # Describe the image
            features = descriptor.describe(image)

            # Write the feature to file
            features = [f for f in features]

            # Append feature to dict
            dataset_features['features'].append({
                'name': imageID,
                'region_1': features[0].tolist(),
                'region_2': features[1].tolist(),
                'region_3': features[2].tolist(),
                'region_4': features[3].tolist(),
                'url': 'ansjdn'
            })

        # Write to json file
        with open('dataset_features.json', 'w') as outfile:
            json.dump(dataset_features, outfile)