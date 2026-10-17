
import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Create background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam")
        break

    # Apply background subtraction
    mask = background_subtractor.apply(frame)

    # Remove small noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )

    # Find contours of moving regions
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        # Ignore small regions
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)

            # Draw bounding box
            cv2.rectangle(
                frame, (x, y), (x + w, y + h),
                (0, 255, 0), 2
            )

            cv2.putText(
                frame, "Moving Object",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2
            )

    # Display webcam and detection mask
    cv2.imshow("Object Detection", frame)
    cv2.imshow("Foreground Mask", mask)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
