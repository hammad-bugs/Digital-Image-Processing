import cv2
import numpy as np
import matplotlib.pyplot as plt


def piecewise_linear_transform(image, breakpoints, slopes):
    # Initialize output image
    transformed_image = np.zeros_like(image)

    # Apply piecewise linear transformation
    for i in range(len(breakpoints) - 1):
        mask = cv2.inRange(image, breakpoints[i], breakpoints[i + 1])
        transformed_image = transformed_image + slopes[i] * (image - breakpoints[i]) * mask

    # Clip pixel values to [0, 255] range
    transformed_image = np.clip(transformed_image, 0, 255)

    return np.uint8(transformed_image)


# Example usage:
# Read a grayscale image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define breakpoints and slopes for piecewise linear transformation
breakpoints = [0, 100, 150, 200, 255]
slopes = [1, 2, 1.5, 0.5]

# Apply piecewise linear transformation
piecewise_transformed_output = piecewise_linear_transform(input_image, breakpoints, slopes)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display transformed image
plt.subplot(1, 2, 2)
plt.imshow(piecewise_transformed_output, cmap='gray')
plt.title('Piecewise Transformed Image')
plt.axis('off')

# Show the plot
plt.show()
