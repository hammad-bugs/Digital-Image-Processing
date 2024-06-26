import cv2
import numpy as np
import matplotlib.pyplot as plt

def power_law_transform(image, gamma=1.0):
    # Apply power law transformation
    power_transformed = np.uint8(np.power(image / 255.0, gamma) * 255)
    return power_transformed

# Example usage:
# Read a grayscale image
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Set gamma value (adjust as needed)
gamma_value = 0.5

# Apply power law transformation
power_transformed_output = power_law_transform(input_image, gamma_value)

# Display original and transformed images using Matplotlib
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display transformed image
plt.subplot(1, 2, 2)
plt.imshow(power_transformed_output, cmap='gray')
plt.title('Power Law Transformed Image')
plt.axis('off')

plt.show()
