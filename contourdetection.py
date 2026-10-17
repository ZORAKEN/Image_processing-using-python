
import cv2

# 1. Read the image
img = cv2.imread("image.jpg")

if img is None:
    raise FileNotFoundError("Image not found!")

# Keep a copy of the original image
result = img.copy()

# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Apply thresholding
ret, thresh = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# 4. Find contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 5. Process each contour
for contour in contours:

    # Contour area
    area = cv2.contourArea(contour)
    print("Area:", area)

    # Ignore small contours
    if area < 100:
        continue

    # Contour perimeter
    perimeter = cv2.arcLength(contour, True)
    print("Perimeter:", perimeter)

    # Approximate contour
    epsilon = 0.02 * perimeter
    approx = cv2.approxPolyDP(
        contour, epsilon, True
    )

    print("Number of vertices:", len(approx))

    # Draw the contour
    cv2.drawContours(
        result, [contour], -1, (0, 255, 0), 2
    )

    # Bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    cv2.rectangle(
        result, (x, y), (x + w, y + h),
        (255, 0, 0), 2
    )

    # Rotated rectangle
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = box.astype("int32")

    cv2.drawContours(
        result, [box], 0, (255, 0, 0), 2
    )

    # Centroid using moments
    M = cv2.moments(contour)

    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        cv2.circle(
            result, (cx, cy), 5, (0, 0, 255), -1
        )

    # Convex hull
    hull = cv2.convexHull(contour)

    cv2.drawContours(
        result, [hull], -1, (255, 0, 255), 2
    )

    # Minimum enclosing circle
    (center_x, center_y), radius = (
        cv2.minEnclosingCircle(contour)
    )

    center = (int(center_x), int(center_y))
    radius = int(radius)

    cv2.circle(
        result, center, radius, (0, 255, 255), 2
    )

# 6. Display results
cv2.imshow("Original Image", img)
cv2.imshow("Threshold Image", thresh)
cv2.imshow("Contour Detection", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
