# AI-EnhancedEngagementTracker
Overview
AI-EnhancedEngagementTracker is an AI-driven project designed to monitor, analyze, and improve user engagement across various platforms. It utilizes machine learning models and data analytics to provide actionable insights, helping teams to better understand user behavior, boost engagement, and tailor content or services accordingly.

Features

Real-time Engagement Tracking: Monitors user activities and interactions in real-time.
Data Visualization: Displays engagement metrics via interactive graphs and charts.
Sentiment Analysis: Uses natural language processing (NLP) to assess user sentiment from comments and feedback.
Predictive Analytics: Forecasts engagement trends based on historical data.
Customizable Dashboards: Tailor dashboards for different departments and objectives.
Notifications and Alerts: Sends alerts based on user-defined conditions for engagement levels or sentiments.
Getting Started
Prerequisites
Python 3.10 or later
Anaconda (recommended for environment management)
Visual Studio Code (recommended for code editing)
Installation
Clone the repository:

git clone https://github.com/Piyu411/AI-EnhancedEngagementTracker.git

cd AI-EnhancedEngagementTracker
Create a virtual environment with Anaconda:
conda create -n engagement-tracker python=3.10
conda activate engagement-tracker
Install the required packages:
pip install -r requirements.txt
(Optional) Set up API keys for any external services used, like sentiment analysis APIs.


Project Structure::-
Image Processing Libraries or Frame Works used - opencv Version - 4.10.0.84 Developed Logics -
A) Image_Noise removal & Closing Gaps :- From the input image given, used to remove the noise and close the gaps 
![i](https://github.com/user-attachments/assets/c678c6f1-b3f8-401e-b1fd-da2f5e79a4fb)![i2](https://github.com/user-attachments/assets/3ba2e7a8-8ad1-45c7-a3a2-5d7e89f1a5d3)![i3](https://github.com/user-attachments/assets/53c67a48-ab6c-48e9-a35d-8d59a3187475)

B) Image_Template :- From the image given, we can modify the image using it
![t](https://github.com/user-attachments/assets/c92d20ca-3735-4837-8a69-5378b0139d09)

C) Image_Colour :- From the input image given, increase the quality of colour comination in the image 
D) Image_Concatenation :- From the input images given, we can conacatenate those images generally used for 2 or more images
E) Image_Contour :-
F) Image_Crop :- From the input image given, we can crop the image 
G) Image_Detection and Erosion :- From the input image given, we can detect the image and erosion 
H) Image_edge detection :- From the input image given, we can detect the edges of image 
I) Image_equalized :- From the input image given, we can equalize the image 
J) Image_hsv :-
K) Image_morph :-
L) Image_resize :- From the input image given, we can resize the image 
M) Image_rgb to gray :- From the input image given, we can convert the image from colour to gray 
N) Image_single image :-
O) Image_blur :- From the input image given, we can blur the image

Video Processing Libraries or Frame Works used - opencv Version - 4.10.0.84 Developed Logics - 
A) Video_multivideo :- From the video recorded live or given, can add multiple video side by side 
B) Video_fps :- From the video recorded live or given, we can change the frames per second in the video 
C) Video_save :- From the video recorded live or given, we can save the video into the folder 
D) Video_stack :- From the video recorded live or given, we can combine the videos 
E) Video_stream From this we can stream or record the video through web cam
 
Annotations Libraries or Frame Works used - opencv, labelImg Version - 4.10.0.84, 1.8.6 Developed Logics - 
A) data_segregate :- From this we can segregate the data of images that we are taken 
B) label From this label, we can label the images 
C) label_manipulate From this label_manipulate, we can update the labels

Face Recognition Libraries or Frame Works used - opencv, labelImg, dlib, face_recognition, imutils Version - 4.10.0.84, 1.8.6, 19.24.6, 1.3.0, 0.5.4 Developed Logics - 
A) Face_recognition 
B) Attendence_save 
C) test 
D) tools 
E) excel_sc 
F) excel_sc_dt 
G) landmark 
H) atten_score 
I) avg_atten_score

Obama

Usage
Launch the main script:
python main.py
Configure settings such as engagement metrics, notification thresholds, and data sources through the provided interface.

Access your customizable dashboard to monitor real-time data and view engagement insights.

License

This project is licensed under the MIT License. See the LICENSE file for details.





Image Processing
Libraries or Frameworks Used:
OpenCV: Version 4.10.0.84
NumPy: For array manipulation
Developed Logics:
A) image_concatenation
This function resizes two images to a specified pixel range and combines them both horizontally and vertically. The results are displayed in separate windows.

Input:

Image 1

Image 2

Output:

Concatenated Image

B) image_contour
This detects contours in a grayscale image using a binary threshold and cv2.findContours(). The contours are drawn onto the original image in green.

Input:

Image 1

Output:

Contoured Image

C) image_crop
This function extracts a specific region of an image based on pixel range and displays the cropped section.

Input:

Image 2

Output:

Cropped Image

D) image_dilation & erosion
This function applies morphological operations, dilation and erosion, to enhance and reduce features in an image, respectively.

Input:

Image 1

Output:

Dilated and Eroded Image

E) image_edge_detection
This applies the Canny edge detection algorithm to detect edges in a grayscale image.

Input:

Image 1

Output:

Edge Detected Image

F) image_histogram_equalization
This enhances the contrast of a grayscale image using histogram equalization.

Input:

Image 2

Output:

Histogram Equalized Image

G) image_hsv
This converts a color image from the BGR color space to HSV.

Input:

Image 2

Output:

HSV Image

H) image_morphological_transformation
This applies opening and closing morphological operations to a grayscale image to remove noise and fill gaps.

Input:

Image 1

Output:

Morphologically Transformed Image

I) image_resize
This resizes an image to specified dimensions.

Input:

Image 1

Output:

Resized Image

J) image_rgb2gray
This converts a color image to grayscale.

Input:

Image 2

Output:

Grayscale Image

K) image_rotate
This rotates an image by 90 degrees around its center.

Input:

Image 2

Output:

Rotated Image

L) image_blur
This applies a Gaussian blur to an image to reduce noise and detail.

Input:

Image 1

Output:

Blurred Image

M) image_noise_removal & closing_gaps
This function removes noise and fills gaps using morphological operations.

N) image_template
This function performs template matching to locate a template image within a larger image.

Video Processing
Libraries or Frameworks Used:
OpenCV: Version 4.10.0.84
Developed Logics:
A) Video_multivideo
This function reads and displays images from a specified folder, printing the dimensions of each image.

B) Video_fps
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

C) Video_save
This function captures live video and saves it to a specified output file.

D) Video_stack
This function reads and resizes two video files, concatenating them horizontally.

E) Video_stream
This function captures live video from the webcam and displays it in real-time.

Annotations
Libraries or Frameworks Used:
OpenCV: Version 4.10.0.84
LabelImg: Version 1.8.6
Developed Logics:
A) data_segregate
This function organizes images and their label files into matched and unmatched directories.

Input:
Screenshot 2024-11-13 174954

Output:
Screenshot 2024-11-13 174816

B) label
This function draws bounding boxes on images based on annotations in the label files.

Input:
gun4

Output:
gun4

C) label_manipulate
This function updates class numbers in label files for object detection tasks.

Input:
Screenshot 2024-11-13 174620

Output:
Screenshot 2024-11-13 174644

Face Recognition
Libraries or Frameworks Used:
OpenCV: Version 4.10.0.84
LabelImg: Version 1.8.6
dlib: Version 19.24.6
face_recognition: Version 1.3.0
imutils: Version 0.5.4
Developed Logics:
A) Face_recognition
This performs real-time face recognition to identify whether the person in live video frames a known image by comparing. His name is displayed if He/She is recognized; otherwise, "Not He/She" appears.

Input:
teja

Output:
Screenshot 2024-11-13 175926

B) Attendence_save
Using a live video stream, this performs real-time face recognition to identify He/She. When He/She's face is recognized, his/her name is displayed on the video feed, and the recognition event is logged with the date and time in an Excel file. After every 5 recognitions, the current log is saved to an Excel file, and the recognition counter and DataFrame are reset.

Input:
teja

Output:
Screenshot 2024-11-13 175926

Screenshot 2024-11-13 180336

C) test
This performs real-time face recognition to identify He/She in a live video feed, logging each recognition event with the date and time into an Excel file every 30 seconds. It tracks recognition intervals to avoid duplicate entries and displays He/She or "Not He/She" based on identification.

Input:
teja

Output:
Screenshot 2024-11-13 175926

Screenshot 2024-11-13 181026

D) tools
This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.

Input:
teja

Output:
Screenshot 2024-11-13 175926

Screenshot 2024-11-13 181459

E) excel_sc
Input:

Output:

F) excel_sc_dt
Input:

Output:

G) landmark
This code is a face recognition and attentiveness tracking system that operates in real time. Key functions include:

Face Recognition: Detects and recognizes "His/Her's face" from the camera using a pre-loaded image.
Attentiveness Detection: Uses facial landmarks and head pose estimation to assess if the subject is attentive.
Logging: Records each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, saving every 30 seconds.
Live Feedback: Displays "Attentive" or "Not Attentive" on the video feed along with facial landmarks.
The system continues until you press 'q' to exit.

Input:
teja

Output: Guru Teja_2024-11-07_20-16-27
Screenshot 2024-11-13 181911

H) atten_score
This script captures real-time webcam video to recognize "His/Her's face" and assess attentiveness based on head pose:

Setup: Loads His/Her's face data and initializes detectors.
Face Recognition: Compares detected faces with the known face, identifying if it's a match.
Attentiveness Check: Estimates head orientation (yaw/pitch) to compute an attentiveness score.
Logging: Logs details (name, date, time, attentiveness, screenshot) in an Excel file every 30 seconds if attentive.
Display: Shows video with face labels, attentiveness status, and facial landmarks.
Exits on 'q' press, ensuring the final save to Excel.

Input:
teja

Output:
Guru Teja_2024-11-07_21-34-50

Screenshot 2024-11-13 182336

I) avg_atten_score
Input:

Output:
