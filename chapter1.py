# === READ IMAGES, VIDEOS AND WEBCAMS === #
import cv2

# ==== IMAGE ==== #

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)
# 0 is infinite delay

# ==== VIDEO ==== #

# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# # a video is a stream of images
# while True:
#     # read each image from the video capture
#     success, img = cap.read()
#     # If successful, show the image on a window
#     cv2.imshow("Video", img)
#     # wait for keyboard button 'q' to be pressed to exit
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# ==== WEBCAM ==== #

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# a video is a stream of images
while True:
    # read each image from the video capture
    success, img = cap.read()
    # If successful, show the image on a window
    cv2.imshow("Video", img)
    # wait for keyboard button 'q' to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
