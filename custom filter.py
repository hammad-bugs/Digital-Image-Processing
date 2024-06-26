import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('sample.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a custom kernel
custom_kernel = np.array([[0, -1, 0],
                          [-1, 5, -1],
                          [0, -1, 0]])

# Apply the custom kernel using cv2.filter2D
custom_filtered_image = cv2.filter2D(gray_image, -1, custom_kernel)

# Display the original and custom-filtered images
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB))
plt.title('Original Grayscale Image')

plt.subplot(1, 2, 2)
plt.imshow(custom_filtered_image, cmap='gray')
plt.title('Custom Filtered Image')

plt.show()
