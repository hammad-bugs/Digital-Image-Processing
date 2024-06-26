

#Gussian is use to reduce noise

import cv2
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('sample.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale imag
'''
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()'''
# Apply Gaussian filter
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Display the original image
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')


# Display the greyed blurred image
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Greyed Blurred Image')
plt.show()
