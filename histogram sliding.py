import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img_2.png', cv2.IMREAD_GRAYSCALE)

# Define the amount of histogram sliding
slide_amount = 50  # Adjust as needed

# Apply histogram sliding
slid_image = original_image + slide_amount
slid_image = np.clip(slid_image, 0, 255)  # Clip to ensure intensity values stay within [0, 255]

# Display the original and slid images along with their histograms
plt.figure(figsize=(15, 7))

# Plot original image and its histogram
plt.subplot(2, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(original_image.flatten(), bins=256, range=(0, 255), color='r')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Plot slid image and its histogram
plt.subplot(2, 2, 3)
plt.imshow(slid_image, cmap='gray')
plt.title('Slid Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(slid_image.flatten(), bins=256, range=(0, 255), color='b')
plt.title('Slid Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
