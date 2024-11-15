import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
img = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg", cv2.IMREAD_GRAYSCALE)

# Verify if the image is loaded
if img is None:
    print("Error: Could not load image.")
else:
    # Define the kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Apply opening (erosion followed by dilation) to remove noise
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # Apply closing (dilation followed by erosion) to fill gaps
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Function to display an image using Matplotlib
    def display_image(image, title):
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()

    # Display the original, opening, and closing images
    display_image(img, "Original Image")
    display_image(opening, "After Opening (Noise Removal)")
    display_image(closing, "After Closing (Gap Filling)")
