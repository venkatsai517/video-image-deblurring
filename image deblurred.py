import cv2

# Read the input image
img = cv2.imread("C:/Users/VENKATA SAI/OneDrive/Pictures/Camera Roll/hi.jpg")

# Define the kernel for the blur removal
kernel = (7, 7)

# Apply the blur removal using the GaussianBlur function
deblurred_img = cv2.GaussianBlur(img, kernel, 0)

# Save the deblurred image
cv2.imwrite("C:/Users/VENKATA SAI/OneDrive/Pictures/Camera Roll/hi.jpg",deblurred_img)
