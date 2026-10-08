pip install opencv-python#install
import cv2 
image = cv2.imread("image.jpg")#to read the image

cv2.imshow("My Image", image)#to display the image
cv2.waitKey(0)
cv2.destroyAllWindows()
