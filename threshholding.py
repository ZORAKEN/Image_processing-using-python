
import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    raise FileNotFoundError("Image not found!")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply all five thresholding operations
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

_, binary_inv = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY_INV
)

_, trunc = cv2.threshold(
    gray, 127, 255, cv2.THRESH_TRUNC
)

_, tozero = cv2.threshold(
    gray, 127, 255, cv2.THRESH_TOZERO
)

_, tozero_inv = cv2.threshold(
    gray, 127, 255, cv2.THRESH_TOZERO_INV
)

# Display results
cv2.imshow("Original Grayscale", gray)
cv2.imshow("Binary", binary)
cv2.imshow("Binary Inverse", binary_inv)
cv2.imshow("Truncation", trunc)
cv2.imshow("To Zero", tozero)
cv2.imshow("To Zero Inverse", tozero_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
