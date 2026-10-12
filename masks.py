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
