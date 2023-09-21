# === ADDING SHAPES AND TEXT TO IMAGES === #
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)

# Color the whole image blue, BGR
# img[:] = 255,0,0

# Draw a line
# Format: Point 1, Point 2, BGR Color, thickness
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Draw rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# Draw Circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# Text
cv2.putText(img, " OPENCV ", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)