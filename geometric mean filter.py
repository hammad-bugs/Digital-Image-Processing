import cv2
import numpy as np
import matplotlib.pyplot as plt

def geometric_mean_filter(input_img, kernel_size=(5, 5)):
    # Define the kernel
    kernel = np.ones(kernel_size, dtype=np.float32)

    # Convert input image to float32
    input_img_float32 = np.float32(input_img)

    # Apply geometric mean filter
    output_img = cv2.pow(cv2.filter2D(input_img_float32, -1, kernel), 1.0 / (kernel_size[0] * kernel_size[1]))

    return np.uint8(output_img)

# Load image
input_img = cv2.imread('img.png')

# Apply geometric mean filter
output_img = geometric_mean_filter(input_img)

# Display both images in the same window using Matplotlib
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Output Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
plt.title('Geometric mean filter Image')
plt.axis('off')

plt.show()
