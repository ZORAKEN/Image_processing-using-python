import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Create a black mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Make a rectangular region white
mask[100:300, 100:300] = 255

# Apply the mask
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

#polygon mask

mask = np.zeros(img.shape[:2], np.uint8)
points = np.array([
    [[100, 100], [300, 100], [200, 300]]
], dtype=np.int32)

cv2.fillPoly(mask, points, 255)

#color masking
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0, 100, 100])
upper = np.array([10, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(
    img, img, mask=mask
)

import cv2
import numpy as np

img = cv2.imread("image.jpg")

mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Select a rectangle
mask[100:300, 150:400] = 255

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

circular masking
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Draw a filled white circle
cv2.circle(
    mask,
    (250, 200),  # center: (x, y)
    100,         # radius
    255,         # white color
    -1           # filled circle
)

result = cv2.bitwise_and(img, img, mask=mask)

#color masking
import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Convert BGR image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Lower and upper limits for a red hue range
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Create binary mask
mask = cv2.inRange(hsv, lower_red, upper_red)

# Apply mask to original color image
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Red Objects", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

threshhold masking
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

result = cv2.bitwise_and(img, img, mask=mask)



#blending
import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

# Resize images to the same dimensions
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Add weighted images
result = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Blended Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
