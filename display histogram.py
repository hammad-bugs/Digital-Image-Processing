import cv2
import matplotlib.pyplot as plt

def display_gray_and_histogram(image_path):
    # Read the color image
    color_image = cv2.imread(image_path)

    # Convert color image to grayscale
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    # Calculate histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Plot histogram
    plt.subplot(1, 2, 2)
    plt.plot(hist, color='black')
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Show the plot
    plt.show()

# Example usage:
image_path = 'sample.jpg'
display_gray_and_histogram(image_path)
