# === RESIZING AND CROPPING IMAGES === #
import cv2
import numpy as np

img = cv2.imread("Resources/lambo.PNG")

# check the size/shape of an image
print(img.shape)

# Resize the pixels of an image (Does NOT improve image quality)
# Size format is (WIDTH, HEIGHT)
imgResize = cv2.resize(img, (1000, 500))

# Cropping image
# Size format is (HEIGHT, WIDTH)
imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)