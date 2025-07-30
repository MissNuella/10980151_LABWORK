import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('image_labwork.jpg')

# Convert color spaces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Display images
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)

# Save converted images
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)

# Plot histogram of grayscale image
plt.figure(figsize=(8, 6))
plt.hist(gray.ravel(), bins=256, range=(0, 256), color='gray')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
