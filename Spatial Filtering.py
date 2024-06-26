import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_user_defined_filter(image, kernel):
    # Apply user-defined spatial filter using convolution operation
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

# Example usage:
# Read an image (grayscale or color)
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define a user-defined filter kernel (example: edge detection)
user_defined_kernel = np.array([[1/9, 2/9, 1/9],
                                [2/9, 1/9, 2/9],
                                [1/9, 2/9, 1/9]])

# Apply user-defined spatial filter
filtered_output = apply_user_defined_filter(input_image, user_defined_kernel)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display filtered image
plt.subplot(1, 2, 2)
plt.imshow(filtered_output, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')

# Show the plot
plt.show()
