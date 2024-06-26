import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian filter
gaussian_filtered_image = cv2.GaussianBlur(original_image, (5, 5), 1)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gaussian_filtered_image, cmap='gray')
plt.title('Gaussian Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
