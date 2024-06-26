import cv2
import numpy as np
import matplotlib.pyplot as plt


def simple_smoothing_filter(image, kernel_size):
    # Define a simple smoothing filter kernel (box filter)
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)

    # Apply the filter using convolution operation
    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image


# Example usage:
# Read an image (grayscale or color)
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size for the smoothing filter
kernel_size = 3  # Adjust the kernel size as needed

# Apply simple smoothing filter
smoothed_output = simple_smoothing_filter(input_image, kernel_size)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display smoothed image
plt.subplot(1, 2, 2)
plt.imshow(smoothed_output, cmap='gray')
plt.title('Smoothed Image')
plt.axis('off')

# Show the plot
plt.show()
