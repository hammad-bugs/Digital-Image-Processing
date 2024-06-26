import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Apply Median Filter
def median_filter(image, filter_size):
    result = cv2.medianBlur(image, filter_size)
    return result

median_filtered_image = median_filter(original_image, filter_size=5)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(median_filtered_image, cmap='gray')
plt.title('Median Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
