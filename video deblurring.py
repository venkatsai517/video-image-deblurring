import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture("C:/Users/VENKATA SAI/OneDrive/Pictures/Camera Roll/project17.mp4")

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the width and height of the frames in the video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('deblurred_video.mp4',fourcc, fps, (frame_width,frame_height))

# Define the kernel for the blur removal
kernel = (7,7)

# Read each frame from the video
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Apply the blur removal using the GaussianBlur function
    deblurred_frame = cv2.GaussianBlur(frame, kernel, 0)
    # Write the deblurred frame to the output video
    out.write(deblurred_frame)

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()
