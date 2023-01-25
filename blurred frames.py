import cv2

# Read in the video file
cap = cv2.VideoCapture("C:/Users/VENKATA SAI/OneDrive/Pictures/Camera Roll/project17.mp4")

# Initialize the threshold for the blur detection
threshold = 50

while True:
    # Read in the next frame
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use the Laplacian method to calculate the blurriness
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    score = abs(laplacian.var())

    # If the frame is considered "blurred", display it
    if score < threshold:
        cv2.imshow("Blurred Frame", frame)
        cv2.waitKey(0)

    # If the user presses 'q', break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
