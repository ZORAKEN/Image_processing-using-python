import cv2
import numpy as np

# Create a blank black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(img, (50, 50), (250, 250),
         (255, 0, 0), 3)

#rectangle
cv2.rectangle(img, (50, 50), (250, 200),
              (0, 255, 0), 3)
#circle
cv2.circle(img, (250, 250), 80,
           (0, 0, 255), 3)

cv2.ellipse(img, (250, 250), (100, 50),
            0, 0, 360, (0, 255, 255), 3)

#polygon
points = np.array([
    [250, 50],
    [100, 250],
    [400, 250]
], dtype=np.int32)

cv2.polylines(img, [points], True, (255, 0, 255), 3)

#to get afilled polygon
cv2.fillPoly(img, [points], (255, 0, 255))

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
