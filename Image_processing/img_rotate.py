import cv2
img = cv2.imread(r"C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\o.jpeg", cv2.IMREAD_GRAYSCALE)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()