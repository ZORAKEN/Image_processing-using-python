
import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    raise FileNotFoundError("Could not find image.jpg")

# 1. Mean / averaging filter
mean = cv2.blur(img, (3, 3))

# 2. Gaussian filter
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Median filter
#Removes white noise salt and pepper
median = cv2.medianBlur(img, 5)

# 4. Bilateral filter
#better for preserving edges the gaussian
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 5. Custom sharpening filter
#sharpen details
kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

sharpened = cv2.filter2D(img, -1, kernel)

# Display all results
cv2.imshow("Original", img)
cv2.imshow("Mean", mean)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.imshow("Bilateral", bilateral)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
