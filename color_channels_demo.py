import os
import cv2
import numpy as np

# Expects George.png to sit next to this script.
img = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)), "George.png"))
h, w = img.shape[:2]

painting = np.zeros((h*2, w*3, 3), dtype=np.uint16)

im1 = img.copy()
im2 = img.copy()
im3 = img.copy()
im4 = img.copy()
im5 = img.copy()
im6 = img.copy()

# 0 Blue
im1[:, :, 0] = 0
# 1 Green
im2[:, :, 1] = 0
# 2 Red
im3[:, :, 2] = 0

im4[:, :, 0] = 255
im5[:, :, 0] = 255
im6[:, :, 0] = 255

cv2.imshow("hi", img)
cv2.waitKey(0)
