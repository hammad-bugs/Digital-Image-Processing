import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image, bit_position):
    # Extract specified bit plane
    bit_plane = (image >> bit_position) & 1
    return np.uint8(bit_plane * 255)

# Example usage:
# Read a grayscale image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Define bit position (0-7 for 8-bit images)
bit_position = 5  # Example: Visualize bit plane 4

# Apply bit plane slicing
bit_plane_image = bit_plane_slice(input_image, bit_position)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display bit plane sliced image
plt.subplot(1, 2, 2)
plt.imshow(bit_plane_image, cmap='gray')
plt.title(f'Bit Plane {bit_position} Sliced Image')
plt.axis('off')

# Show the plot
plt.show()
