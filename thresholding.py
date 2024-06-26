import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image in grayscale
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Apply thresholding (adjust the threshold value as needed)
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Thresholded Image')

plt.show()
