import cv2
import numpy as np
import matplotlib.pyplot as plt

def grey_level_slicing(image, lower_threshold, upper_threshold, highlight_color=255, background_color=0):
    # Apply grey level slicing
    output_image = np.where((image >= lower_threshold) & (image <= upper_threshold), highlight_color, background_color)
    return output_image

# Example usage:
# Read a grayscale image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define lower and upper thresholds
lower_threshold = 100
upper_threshold = 200

# Apply grey level slicing
sliced_output = grey_level_slicing(input_image, lower_threshold, upper_threshold)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display sliced image
plt.subplot(1, 2, 2)
plt.imshow(sliced_output, cmap='gray')
plt.title('Sliced Image')
plt.axis('off')

# Show the plot
plt.show()
