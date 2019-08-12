import cv2
import numpy as np


# Image Reading
image = cv2.imread("Pictures/2.jpg")
blurred_image = cv2.GaussianBlur(image, (5, 5), 1)    

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    

print(image.shape)

cv2.imshow("Image", image)


cv2.waitKey(0)
cv2.destroyAllWindows()
