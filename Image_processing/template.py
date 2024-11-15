import cv2

# Load the main image and template in grayscale for template matching
img = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg", cv2.IMREAD_GRAYSCALE)
template = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\p.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the images are loaded correctly
if img is None:
    print("Error: Could not load the main image.")
elif template is None:
    print("Error: Could not load the template image.")
else:
    # Perform template matching
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Find the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = template.shape[:2]
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Reload the main image in color to draw the rectangle
    img_color = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg")
    cv2.rectangle(img_color, top_left, bottom_right, (0, 255, 0), 3)

    # Display the result
    cv2.imshow('Detected Template', img_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
