import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image and the target histogram image
original_image = cv2.imread('source.jpg', cv2.IMREAD_GRAYSCALE)
target_histogram_image = cv2.imread('target.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histograms of the original and target images
original_hist = cv2.calcHist([original_image], [0], None, [256], [0, 256])
target_hist = cv2.calcHist([target_histogram_image], [0], None, [256], [0, 256])

# Normalize histograms to obtain cumulative distribution functions (CDFs)
original_cdf = np.cumsum(original_hist) / np.sum(original_hist)
target_cdf = np.cumsum(target_hist) / np.sum(target_hist)

# Map the intensity values of the original image to match the target histogram
mapping = np.interp(original_cdf, target_cdf, range(256))
matched_image = cv2.LUT(original_image, mapping.astype('uint8'))

# Calculate histograms for the matched image
matched_hist = cv2.calcHist([matched_image], [0], None, [256], [0, 256])

# Display the original, target histogram, and matched images along with their histograms
plt.figure(figsize=(20, 10))

plt.subplot(2, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(target_histogram_image, cmap='gray')
plt.title('Target Histogram Image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(matched_image, cmap='gray')
plt.title('Matched Image')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.plot(original_hist, color='r')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 5)
plt.plot(target_hist, color='b')
plt.title('Target Histogram Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 6)
plt.plot(matched_hist, color='g')
plt.title('Matched Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
