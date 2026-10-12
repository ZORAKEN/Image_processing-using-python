
import cv2
import numpy as np

# Create two black images
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

# Draw white shapes on the images
cv2.rectangle(img1, (50, 50), (200, 200), 255, -1)
cv2.circle(img2, (180, 150), 80, 255, -1)

# 1. BITWISE AND
bitwise_and = cv2.bitwise_and(img1, img2)

# 2. BITWISE OR
bitwise_or = cv2.bitwise_or(img1, img2)

# 3. BITWISE XOR
bitwise_xor = cv2.bitwise_xor(img1, img2)

# 4. BITWISE NOT
bitwise_not = cv2.bitwise_not(img1)

# Display results
cv2.imshow("Image 1 - Rectangle", img1)
cv2.imshow("Image 2 - Circle", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
