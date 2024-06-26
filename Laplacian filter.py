import cv2
import numpy as np
import matplotlib.pyplot as plt


def laplacian_filter(image, kernel_size):
    # Apply Gaussian smoothing to reduce noise
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Apply Laplacian filter
    laplacian_image = cv2.Laplacian(blurred_image, cv2.CV_64F)

    # Convert back to uint8 and scale to 0-255 range
    laplacian_image = np.uint8(np.abs(laplacian_image))

    return laplacian_image


# Example usage:
# Read an image (grayscale or color)
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size for Gaussian smoothing
gaussian_kernel_size = 5  # Adjust the kernel size as needed

# Apply Laplacian filter
laplacian_output = laplacian_filter(input_image, gaussian_kernel_size)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display Laplacian-filtered image
plt.subplot(1, 2, 2)
plt.imshow(laplacian_output, cmap='gray')
plt.title('Laplacian Filtered Image')
plt.axis('off')

# Show the plot
plt.show()
