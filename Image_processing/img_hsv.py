import cv2

# Load the image in color
img = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg", cv2.IMREAD_COLOR)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image.")
else:
    # Convert the image to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Display the HSV image
    cv2.imshow('HSV Image', hsv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
