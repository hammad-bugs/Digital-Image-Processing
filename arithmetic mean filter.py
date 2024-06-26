import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Apply Arithmetic Mean Filter
def arithmetic_mean_filter(image, filter_size):
    kernel = np.ones((filter_size, filter_size), dtype=np.float32) / (filter_size ** 2)
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

arithmetic_filtered_image = arithmetic_mean_filter(original_image, filter_size=5)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(arithmetic_filtered_image, cmap='gray')
plt.title('Arithmetic Mean Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
