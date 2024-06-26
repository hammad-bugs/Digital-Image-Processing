import cv2
import numpy as np
import matplotlib.pyplot as plt

# Replace 'your_image_path.jpg' with the path to your image
image_path = 'sample.jpg'

# Read the image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the intensity range for histogram shrinking
lower_bound = 100
upper_bound = 255

# Clip pixel values within the specified range
img_shrunk = np.clip(img, lower_bound, upper_bound)

# Display the original and shrunk images side by side
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(2,2,2)
plt.imshow(img_shrunk, cmap='gray')
plt.title('Shrunk Image')

# Display the histograms
plt.subplot(2,2,3)
plt.hist(img.flatten(), bins=256, range=[0, 256], color='r', alpha=0.7)
plt.title('Original Histogram')
plt.subplot(2,2,4)
plt.hist(img_shrunk.flatten(), bins=256, range=[0, 256], color='b', alpha=0.7)
plt.title('Shrunk Histogram')

plt.show()
