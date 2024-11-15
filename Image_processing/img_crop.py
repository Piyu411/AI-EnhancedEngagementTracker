import cv2

img = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg")
cropped = img[50:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()