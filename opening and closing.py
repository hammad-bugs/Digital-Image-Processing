import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
image = cv2.imread('sample.jpg', 0)

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Perform Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the results
plt.figure(figsize=(10, 7))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Opening')
plt.imshow(opening, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Closing')
plt.imshow(closing, cmap='gray')

plt.show()