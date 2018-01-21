import numpy as np
import cv2

class ColorDescriptor:
    def __init__(self, bins):
        # Store the number of bin for the histogram
        self.bins = bins

    def describe(self, image):
        # Convert image to HSV color
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # Init features array
        features = []

        # Grab dimension and center of image
        (h, w) = image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))

        # Divide image to four regions
        # (top-left, top-right, bottom-left, bottom-right)
        regions = [(cX, 0, 0, cY), (cX, 0, w, cY), (0, cY, cX, h), (cX, cY, w, h)]

        # Loop over the regions
        for (startX, startY, endX, endY) in regions:
            regionMask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(regionMask, (startX, startY), (endX, endY), 255, -1)

            # Extract color histogram from image
            hist = self.histogram(image, regionMask)
            # Update feature
            features.append(hist)

        return features

    def histogram(self, image, mask):
        # Extract color histogram using supplied bin
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])
        # Normalize the histogram
        dst = np.zeros(hist.shape[:0], dtype="float")
        hist = cv2.normalize(hist, dst)
        hist = hist.flatten()

        return hist