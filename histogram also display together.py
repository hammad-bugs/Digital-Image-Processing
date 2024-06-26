import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image in grayscale
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Compute and plot the histogram of the original image
plt.subplot(2, 2, 1)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Original Image Histogram')

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Compute and plot the histogram of the equalized image
plt.subplot(2, 2, 2)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Equalized Image Histogram')

# Display the original and equalized images
plt.subplot(2, 2, 3)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Equalized Image')

plt.show()
