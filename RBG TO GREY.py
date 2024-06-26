
import cv2
import matplotlib.pyplot as plt

def rgb_to_gray(rgb_image):
    # Convert RGB image to grayscale using OpenCV
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
    return gray_image

# Example usage:
# Read an RGB image
rgb_image = cv2.imread('sample.jpg')

# Convert RGB image to grayscale
gray_image = rgb_to_gray(rgb_image)

# Display original and grayscale images using Matplotlib
fig, axes = plt.subplots(1, 2)

# Display original RGB image
axes[0].imshow(cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

# Display grayscale image
axes[1].imshow(gray_image, cmap='gray')
axes[1].set_title('Grayscale Image')
axes[1].axis('off')

# Show the plot
plt.show()
