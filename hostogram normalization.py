import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to compute normalized histogram
def normalized_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist / np.sum(hist)

# Example usage:
# Read a grayscale image
gray_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
normalized_image = cv2.normalize(gray_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Display original image and its histogram
axs[0, 0].imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title("Original Image")
axs[0, 0].axis('off')
axs[0, 1].hist(gray_image.ravel(), bins=256, range=[0, 256], color='black')
axs[0, 1].set_title("Original Histogram")
axs[0, 1].set_xlabel("Pixel Intensity")
axs[0, 1].set_ylabel("Frequency")

# Display normalized image and its histogram
axs[1, 0].imshow(normalized_image, cmap='gray')
axs[1, 0].set_title("Normalized Image")
axs[1, 0].axis('off')
axs[1, 1].plot(normalized_histogram(normalized_image), color='black')
axs[1, 1].set_title("Normalized Histogram")
axs[1, 1].set_xlabel("Pixel Intensity")
axs[1, 1].set_ylabel("Normalized Frequency")

plt.tight_layout()
plt.show()
