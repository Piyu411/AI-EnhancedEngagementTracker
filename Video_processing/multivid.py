import cv2
import os

folder_path = "C:/Users/tejac/OneDrive/Desktop/teja/"


for filename in os.listdir(folder_path):
   
    file_path = os.path.join(folder_path, filename)

    image = cv2.imread(file_path)
    if image is not None:
       
        cv2.imshow('Image', image)
        cv2.waitKey(0)      
        cv2.destroyAllWindows()
        print(f"{filename} dimensions: {image.shape}")
    else:
        print(f"Failed to load {filename}")

