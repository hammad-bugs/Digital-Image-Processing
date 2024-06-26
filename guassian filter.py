import cv2
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('sample.jpg')

# Display the original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()


# Apply Gaussian filter
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the blurred image
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image')
plt.show()
