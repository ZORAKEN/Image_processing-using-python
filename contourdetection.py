import cv2

# Read the image
img = cv2.imread("image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
ret, thresh = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Find contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Display the results
cv2.imshow("Original Image with Contours", img)
cv2.imshow("Threshold Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
