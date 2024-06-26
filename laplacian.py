#
import cv2
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('sample.jpg')


#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
#plt.imshow(gray_image, cmap='gray')
#plt.title('Grayscale Image')
#plt.show()

laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Display the original image
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# Display the Laplacian-filtered image
plt.subplot(1,2,2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Filtered Image')

plt.show()