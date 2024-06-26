import cv2
import matplotlib.pyplot as plt

def threshold_image(image, threshold):
    # Apply binary thresholding
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

# Example usage:
# Read a grayscale image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Set threshold value (adjust as needed)
threshold_value = 125

# Apply thresholding
binary_output = threshold_image(input_image, threshold_value)

# Display both images in one screen using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display thresholded image
plt.subplot(1, 2, 2)
plt.imshow(binary_output, cmap='gray')
plt.title('Thresholded Image')
plt.axis('off')

# Show the plot
plt.show()
