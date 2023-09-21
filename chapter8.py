# === CONTOURS / SHAPE DETECTION === #
import cv2
import numpy as np
import chapter6 as ch6

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            # print(perimeter)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            print(len(approx))
            objectCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objectCorners == 3: objectType = "Tri"
            elif objectCorners == 4:
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objectCorners > 4: objectType = "Circle"
            else: objectType = "None"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

# Find edges in image
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

imgBlank = np.zeros_like(img)

imgStack = ch6.stackImages(0.6, ([img, imgGray, imgBlur],
                                                [imgCanny, imgContour, imgBlank]))

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)