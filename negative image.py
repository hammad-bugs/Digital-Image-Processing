import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('sample.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Create a negative image
negative_image = 255 - gray_image

# Display the original and negative images
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')

plt.show()
