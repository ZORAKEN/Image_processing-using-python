#cropping
import cv2

img = cv2.imread("image.jpg")

# Crop the image
cropped = img[100:300, 200:500]

cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing
import cv2

img = cv2.imread("image.jpg")

resized = cv2.resize(img, (500, 300))

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Maintain the original aspect ratio
resized = cv2.resize(
    img, None,
    fx=0.5,
    fy=0.5
)

#rotate
rotated = cv2.rotate(
    img,
    cv2.ROTATE_90_CLOCKWISE
)
rotated = cv2.rotate(
    img,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)
rotated = cv2.rotate(
    img,
    cv2.ROTATE_180
)

#flipping
import cv2

img = cv2.imread("image.jpg")
flipped_1 = cv2.flip(img, 0)
flipped = cv2.flip(img, 1)
#0 vertical.-1 for both
cv2.imshow("Horizontal Flip", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
