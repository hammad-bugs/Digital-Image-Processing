import cv2
import numpy as np
import matplotlib.pyplot as plt

def logarithmic_transform(image, c=1):
    # Apply logarithmic transformation
    log_transformed = c * np.log1p(image)

    # Normalize transformed image to 0-255 range
    log_transformed = (255 * log_transformed / np.max(log_transformed)).astype(np.uint8)

    return log_transformed

# Example usage:
# Read a grayscale image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Apply logarithmic transformation
log_transformed_output = logarithmic_transform(input_image)

# Display original and transformed images using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display logarithmically transformed image
plt.subplot(1, 2, 2)
plt.imshow(log_transformed_output, cmap='gray')
plt.title('Logarithmic Transformed Image')
plt.axis('off')

# Show the plot
plt.show()
