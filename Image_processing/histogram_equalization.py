import cv2

# Load the image in grayscale
img = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image.")
else:
    # Apply histogram equalization
    equalized = cv2.equalizeHist(img)

    # Display the result
    cv2.imshow('Equalized Image', equalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
