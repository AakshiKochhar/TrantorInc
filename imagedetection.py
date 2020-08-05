""" This program will detect an object and draw a rectangle around the
recognized object when located.
"""

import cv2
from matplotlib import pyplot

# Open picture
image = cv2.imread("stopsign.jpg")

# Convert photo from color to grayscale and vice versa.
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
color_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

object_detection = cv2.CascadeClassifier('haar_cascades.xml')
object_sizeDetector = object_detection.detectMultiScale(
    grayscale_image, minSize=(20, 20))

objects_found = len(object_sizeDetector)
if objects_found != 0:
    for (x, y, width, height) in object_sizeDetector:
        cv2.rectangle(color_image, (x, y),
                      (x + height, y + width),
                      (0, 250, 0), 5)   # Draw a rectangle around
        # every detected and recognized object.

pyplot.subplot(1, 1, 1)
pyplot.imshow(color_image) # Display data as image.
pyplot.show() # Look and display all recognizable objects in an interactive window.
