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

C) Image_Colour :- From the input image given, increase the quality of colour comination in the image ![t](https://github.com/user-attachments/assets/4b172b25-94c0-4e76-99f2-23854ef57e98)

D) Image_Concatenation :- From the input images given, we can conacatenate those images generally used for 2 or more images![sp](https://github.com/user-attachments/assets/30b9aedb-6503-459d-b612-74dd10b95cf8)

E) Image_Contour :-it is used to detects contours in a grayscale image using a binary threshold and cv2.findContours(). The contours are drawn onto the original image in green.![al](https://github.com/user-attachments/assets/8cdc87e7-e838-43a1-abc8-e10c5b17f7f2)

F) Image_Crop :- From the input image given, we can crop the image ![v](https://github.com/user-attachments/assets/63de225c-9d0a-45b0-a9dd-6c0284d06ea1)

G) Image_Detection and Erosion :- From the input image given, we can detect the image and erosion ![l1](https://github.com/user-attachments/assets/f1cd8bf1-9a6f-41dd-ab7b-b2ee1d8f3a0b)

H) Image_edge detection :- From the input image given, we can detect the edges of image ![j1](https://github.com/user-attachments/assets/63679669-3b49-4b63-8b4d-e8b21bd9dce5)

I) Image_histogram_equalization:-This enhances the contrast of a grayscale image using histogram equalization.![h](https://github.com/user-attachments/assets/7e3d33ce-72ba-4b57-b20d-d0567e4220e0)
J) Image_hsv :-From the input image given, we can converts a color image from the BGR color space to HSV.![pp](https://github.com/user-attachments/assets/a76532a5-672b-418e-86f2-fdee0d55d31a)

K)  Image_blur :- From the input image given, we can blur the image![rs](https://github.com/user-attachments/assets/ec31566b-0f03-4a20-a9df-f8c101e10c2d)

L) Image_resize :- From the input image given, we can resize the image ![lm](https://github.com/user-attachments/assets/a6a6e65a-d1c1-4b25-a837-eee1dfdca4db)

M) Image_rgb to gray :- From the input image given, we can convert the image from colour to gray ![a11](https://github.com/user-attachments/assets/d9f1f83f-72e9-402c-a015-8ebb1393785f)



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
