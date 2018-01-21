from cbir.colordescriptor import ColorDescriptor
from cbir.searcher import Searcher
import cv2
import numpy as np
import json

class Search:
    
    def __init__(self, image, name):
        self.image = image
        self.name = name

    def query_search(self):
        # Read image
        query = cv2.imdecode(np.fromstring(self.image, np.uint8), cv2.IMREAD_UNCHANGED)
        fname = self.name

        print(query)

        # Initialize ColorDescriptor and bins
        descriptor = ColorDescriptor((8, 12, 3))

        # Describe feature of query image
        feature = descriptor.describe(query)

        # Perform the search
        searcher = Searcher('dataset_features.json')
        results = searcher.search(feature)

        # Init dict result
        query, result = {}, {}
        result['result'], query['query'] = [], []
        # Loop over the results
        for (score, resultID) in results:
            # Save result to dict
            result['result'].append({
                'name': resultID,
                'photo': 'dataset/' + resultID,
                'score': score,
                'url': 'tes'
            })

        query['query'].append({
            'name': fname,
            'photo': 'dataset/' + fname,
            'url': 'tes'
        })

        return result, query