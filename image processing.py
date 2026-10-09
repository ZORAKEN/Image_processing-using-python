#cropping
import cv2

img = cv2.imread("image.jpg")

# Crop the image
cropped = img[100:300, 200:500]

cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
