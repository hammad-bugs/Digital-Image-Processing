import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)


# Apply Midpoint Filter
def midpoint_filter(image, filter_size):
    result = np.zeros_like(image, dtype=np.float64)
    pad_size = filter_size // 2
    padded_image = cv2.copyMakeBorder(image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REPLICATE)

    for i in range(pad_size, padded_image.shape[0] - pad_size):
        for j in range(pad_size, padded_image.shape[1] - pad_size):
            roi = padded_image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]
            min_val = np.min(roi)
            max_val = np.max(roi)
            result[i - pad_size, j - pad_size] = (min_val + max_val) / 2

    return np.uint8(result)


midpoint_filtered_image = midpoint_filter(original_image, filter_size=3)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(midpoint_filtered_image, cmap='gray')
plt.title('Midpoint Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
