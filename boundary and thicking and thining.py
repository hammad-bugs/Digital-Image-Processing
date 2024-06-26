import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
image = cv2.imread('sample.jpg', 0)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform Dilation for thickening
thickening = cv2.dilate(image, kernel, iterations = 1)

# Perform Erosion for thinning
thinning = cv2.erode(image, kernel, iterations = 1)

# Perform Boundary Extraction (Morphological Gradient)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 4, 2)
plt.title('Thickening')
plt.imshow(thickening, cmap='gray')

plt.subplot(1, 4, 3)
plt.title('Thinning')
plt.imshow(thinning, cmap='gray')

plt.subplot(1, 4, 4)
plt.title('Boundary Extraction')
plt.imshow(gradient, cmap='gray')

plt.show()