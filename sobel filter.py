import cv2
import numpy as np
import matplotlib.pyplot as plt


def sobel_filter(image):
    # Apply Sobel filter for horizontal and vertical changes
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute gradient magnitude
    gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    # Normalize gradient magnitude to 0-255 range
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude


# Example usage:
# Read an image (grayscale or color)
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter
sobel_output = sobel_filter(input_image)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display Sobel-filtered image
plt.subplot(1, 2, 2)
plt.imshow(sobel_output, cmap='gray')
plt.title('Sobel Filtered Image')
plt.axis('off')

# Show the plot
plt.show()
