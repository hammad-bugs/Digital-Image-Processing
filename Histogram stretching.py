import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img_2.png', cv2.IMREAD_GRAYSCALE)

# Perform histogram stretching or shrinking
def histogram_stretching(image, low=0, high=255):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = ((image - min_val) / (max_val - min_val)) * (high - low) + low
    return np.uint8(np.clip(stretched_image, low, high))

# Define the range for stretching or shrinking
low_range = 0
high_range = 255

# Apply histogram stretching or shrinking
stretched_image = histogram_stretching(original_image, low_range, high_range)

# Calculate histograms for both images
hist_original = cv2.calcHist([original_image], [0], None, [256], [0, 256])
hist_stretched = cv2.calcHist([stretched_image], [0], None, [256], [0, 256])

# Display the original and stretched images along with their histograms
plt.figure(figsize=(15, 7))

# Plot original image and its histogram
plt.subplot(2, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Plot stretched image and its histogram
plt.subplot(2, 2, 3)
plt.imshow(stretched_image, cmap='gray')
plt.title('Shrunken Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.plot(hist_stretched, color='black')
plt.title('Shrunken Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
