#sobel filter is edge detector
import cv2
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('sample.jpg')


#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
#plt.imshow(gray_image, cmap='gray')
#plt.title('Grayscale Image')
#plt.show()
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Display the original image
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')


# Display the Sobel-filtered image
plt.subplot(1,2,2)
plt.imshow(sobel_magnitude, cmap='gray')
plt.title('Sobel Filtered Image')
plt.show()
