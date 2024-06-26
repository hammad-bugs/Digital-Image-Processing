import cv2
import matplotlib.pyplot as plt

def negative_image(image):
    # Invert pixel intensities
    negative_image = 255 - image
    return negative_image

# Example usage:
# Read an image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Apply negative transformation
negative_output = negative_image(input_image)

# Display original and negative images using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display negative image
plt.subplot(1, 2, 2)
plt.imshow(negative_output, cmap='gray')
plt.title('Negative Image')
plt.axis('off')

# Show the plot
plt.show()
