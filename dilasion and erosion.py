import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
image = cv2.imread('sample.jpg', 0)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform Erosion
erosion = cv2.erode(image, kernel, iterations = 1)

# Perform Dilation
dilation = cv2.dilate(image, kernel, iterations = 1)

# Display the results
plt.figure(figsize=(10, 7))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Erosion')
plt.imshow(erosion, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Dilation')
plt.imshow(dilation, cmap='gray')

plt.show()