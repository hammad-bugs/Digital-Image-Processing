import cv2
import matplotlib.pyplot as plt

def display_gray_and_equalized(image_path):
    # Read the grayscale image
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Equalize the histogram
    equalized_image = cv2.equalizeHist(gray_image)

    # Calculate histograms
    hist_gray = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    # Display original grayscale image and its histogram
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.plot(hist_gray, color='black')
    plt.title('Original Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Display equalized image and its histogram
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.plot(hist_equalized, color='black')
    plt.title('Equalized Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage:
image_path = 'sample.jpg'
display_gray_and_equalized(image_path)
