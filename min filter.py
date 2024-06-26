import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Apply Min Filter
def min_filter(image, filter_size):
    kernel = np.ones((filter_size, filter_size), dtype=np.uint8)
    result = cv2.erode(image, kernel, iterations=1)
    return result

min_filtered_image = min_filter(original_image, filter_size=3)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(min_filtered_image, cmap='gray')
plt.title('Min Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
