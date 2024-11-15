# AI-EnhancedEngagementTracker
Overview
AI-EnhancedEngagementTracker is an AI-driven project designed to monitor, analyze, and improve user engagement across various platforms. It utilizes machine learning models and data analytics to provide actionable insights, helping teams to better understand user behavior, boost engagement, and tailor content or services accordingly.

# Features

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
A) Image_Noise removal & Closing Gaps :- From the input image given, used to remove the noise and close the gaps.

![i](https://github.com/user-attachments/assets/c678c6f1-b3f8-401e-b1fd-da2f5e79a4fb)![i2](https://github.com/user-attachments/assets/3ba2e7a8-8ad1-45c7-a3a2-5d7e89f1a5d3)![i3](https://github.com/user-attachments/assets/53c67a48-ab6c-48e9-a35d-8d59a3187475)

B) Image_Template :- From the image given, we can modify the image using it.

![t](https://github.com/user-attachments/assets/c92d20ca-3735-4837-8a69-5378b0139d09)

C) Image_Colour :- From the input image given, increase the quality of colour comination in the image.
![t](https://github.com/user-attachments/assets/4b172b25-94c0-4e76-99f2-23854ef57e98)

D) Image_Concatenation :- From the input images given, we can conacatenate those images generally used for 2 or more images.
![sp](https://github.com/user-attachments/assets/30b9aedb-6503-459d-b612-74dd10b95cf8)

E) Image_Contour :-it is used to detects contours in a grayscale image using a binary threshold and cv2.findContours(). The contours are drawn onto the original image in green.
![al](https://github.com/user-attachments/assets/8cdc87e7-e838-43a1-abc8-e10c5b17f7f2)

F) Image_Crop :- From the input image given, we can crop the image. 
![v](https://github.com/user-attachments/assets/63de225c-9d0a-45b0-a9dd-6c0284d06ea1)

G) Image_Detection and Erosion :- From the input image given, we can detect the image and erosion
![l1](https://github.com/user-attachments/assets/f1cd8bf1-9a6f-41dd-ab7b-b2ee1d8f3a0b)

H) Image_edge detection :- From the input image given, we can detect the edges of image
![j1](https://github.com/user-attachments/assets/63679669-3b49-4b63-8b4d-e8b21bd9dce5)

I) Image_histogram_equalization:-This enhances the contrast of a grayscale image using histogram equalization.
![h](https://github.com/user-attachments/assets/7e3d33ce-72ba-4b57-b20d-d0567e4220e0)
J) Image_hsv :-From the input image given, we can converts a color image from the BGR color space to HSV.
![pp](https://github.com/user-attachments/assets/a76532a5-672b-418e-86f2-fdee0d55d31a)

K)  Image_blur :- From the input image given, we can blur the image.
![rs](https://github.com/user-attachments/assets/ec31566b-0f03-4a20-a9df-f8c101e10c2d)

L) Image_resize :- From the input image given, we can resize the image.
![lm](https://github.com/user-attachments/assets/a6a6e65a-d1c1-4b25-a837-eee1dfdca4db)

M) Image_rgb to gray :- From the input image given, we can convert the image from colour to gray.
![a11](https://github.com/user-attachments/assets/d9f1f83f-72e9-402c-a015-8ebb1393785f)



Video Processing Libraries or Frame Works used - opencv Version - 4.10.0.84 Developed Logics - 
A) Video_multivideo :- From the video recorded live or given, can add multiple video side by side 
B) Video_fps :- From the video recorded live or given, we can change the frames per second in the video 
C) Video_save :- From the video recorded live or given, we can save the video into the folder 
D) Video_stack :- From the video recorded live or given, we can combine the videos 
E) Video_stream From this we can stream or record the video through web cam
 
Annotations Libraries or Frame Works used :-
opencv, labelImg- 4.10.0.84
Version -1.8.6 

Developed Logics - 
A) data_segregate :- This function organizes images and their label files into matched and unmatched directories.
input::
![gh](https://github.com/user-attachments/assets/4f78268f-82fa-4f47-a151-14e9d675c1dc)

output::
![ghj](https://github.com/user-attachments/assets/49494ce7-7081-460d-98d6-cf07dcc8e47d)


B) label-This function draws bounding boxes on images based on annotations in the label files.
![gun](https://github.com/user-attachments/assets/f2615c4d-5cbd-4249-947b-f9e990768881)

C) label_manipulate- This function updates class numbers in label files for object detection tasks.
input-![j](https://github.com/user-attachments/assets/98d02966-306a-4ad0-9716-f84ea8a0ff0f)
output-![d](https://github.com/user-attachments/assets/756ca73d-31d3-43e7-89d4-0a3cb05f5de0)



Face Recognition Libraries or Frame Works used - 
opencv-python= 4.10.0.84
face_recognition=1.3.0
dlib =19.24.6
pandas= 2.2.3
numpy = 1.26.4
datetime=5.5
os
imutils=0.5.4

Developed Logics - 
A) Face_recognition:-This code performs real-time facial recognition using OpenCV and Face Recognition libraries. It compares faces detected from a live camera feed to a known face encoding, logging recognized faces into an Excel file.
![fr](https://github.com/user-attachments/assets/77dc7c0b-f6ae-41ae-8478-dc0fa61edb04)

B) Attendence_save:-This updated code streamlines the facial recognition and logging of recognized individuals in real-time.
![as](https://github.com/user-attachments/assets/8edeb2be-cbec-4b3e-babf-eef14e2c1521)
![hh](https://github.com/user-attachments/assets/7310099c-cbd1-4bad-a3bf-c4cf096f7291)


C) test:This version includes several improvements in handling the recognition logic, logging, and saving data.
![bm](https://github.com/user-attachments/assets/e6979737-ded9-480d-91d7-271daae85d87)
![kaax](https://github.com/user-attachments/assets/6fa401ea-a355-430c-b74c-4157addc5223)

D) tools:This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.
![piu](https://github.com/user-attachments/assets/aaae6ed0-8ca6-421f-8a1b-e25f691158f4)
![dnh](https://github.com/user-attachments/assets/824222d8-44e5-437b-baf2-e8e222495358)



E) excel_sc:This version of the code is set up to recognize anyone using facial recognition and logs recognized entries into an Excel file.
![alsk](https://github.com/user-attachments/assets/f97819e5-8d4a-45c5-9d37-e7d55a4ec008)
![apsi](https://github.com/user-attachments/assets/7f0138fa-dbe6-4b40-9a4e-fc2fc845ea79)

F) excel_sc_dt :This code effectively performs real-time face recognition for anyone using the camera feed. It detects a face and checks if it matches a pre-loaded image of that person within a specified confidence threshold. If a match is found, it logs the entry with a timestamp into a DataFrame, which it then saves periodically and upon exiting
Image and Face Encoding: The code loads a reference image of "Piyush Singh" and computes its face encoding.
Recognition Timing Controls:
entry_duration: Ensures the same person is only logged once within a 2-minute period.
gap_time: Allows another entry if the person appears again after a 5-minute gap.
Frame Skipping: Every 2nd frame is processed to balance performance.
Data Logging: Recognized entries are periodically saved in an Excel file. Additionally, if the session ends, all remaining data is saved to a specified path.
![bsjda](https://github.com/user-attachments/assets/8b7fc388-7085-410d-8df8-60b9bd823d18)
![adnjsdkq](https://github.com/user-attachments/assets/041c4f59-c078-49c7-a7c1-5181eb0a619e)


G) landmark::-In this code, we've introduced additional functionality to calculate the average attention score over the duration of the session. Here’s a summary of the modifications:
Key Changes
Each frame's calculated attention score is stored in a list (attention_scores). After the video feed ends, the average attention score is calculated from this list.
At the end, the average attention score is appended as a new entry in the DataFrame under the name “Average.” This entry makes it easy to log a session-wide attention metric.
The final DataFrame, including individual entries and the overall average score, is saved to an Excel file attendance_with_attention_and_average.xlsx.
Other Functional Points
Real-time Attention Feedback: As before, individual frames display whether the person is attentive or not based on their attention score.
Enhanced Output: The attendance log, including attention status and scores for each detected instance, along with the average attention score, is saved to a specified directory.
Potential Adjustments
Attention Score Thresholds: Consider fine-tuning MAX_YAW_THRESHOLD and MAX_PITCH_THRESHOLD based on real-world testing, as these values impact attentiveness classification.
Performance Optimizations: Depending on hardware, you might consider further downsampling frames or optimizing loop efficiency for better real-time performance.
This code provides a detailed attentiveness analysis and comprehensive logging for face recognition sessions.
![sgs](https://github.com/user-attachments/assets/15bf1c82-5ba8-4dca-a085-af19e1cb3412)
![hwjw](https://github.com/user-attachments/assets/7df6c58f-a2fa-4955-9570-459b3868bcca)
![zdm](https://github.com/user-attachments/assets/72b74d9e-8af0-4130-810b-ae1860a49457)


H) atten_score :This code is designed for real-time face recognition and attentiveness analysis using a webcam feed.Face Recognition: The code loads a reference image of "Piyush Singh" and computes its face encoding. In each frame, it checks if the face detected matches the reference with a confidence threshold of 0.6.
Landmark Detection & Head Pose Estimation:
Dlib's landmark detector identifies 68 facial points. Specific points are used to estimate head pose, which provides the yaw and pitch angles. These angles help determine attentiveness.
Using yaw and pitch angles, an attention score is calculated between 0 (not attentive) and 1 (fully attentive). If the attention score is 0.5 or higher, the person is marked as "Attentive."
When the person is recognized, their name, date, time, attention status, score, and a screenshot path are logged in a DataFrame.
Screenshots are saved in a folder named "screenshots," and each log entry includes a reference to the image file.
Real-time feedback is shown on the frame, displaying whether "Piyush Singh" is recognized and attentive or not.

At the end of the session, all log data, including attention scores, are saved to attendance_with_attention.xlsx.

![shdgxwsh](https://github.com/user-attachments/assets/722f1f09-fd2e-4cc1-b3ec-353d24ec2406)
![sdk](https://github.com/user-attachments/assets/cc920e50-31f0-4aa3-868c-39afdeb84621)


I) avg_atten_score:_This code is designed for real-time face recognition and attentiveness analysis using a webcam feed. Here’s an overview of the key functionalities and flow:
Face Recognition: The code loads a reference image of "Piyush Singh" and computes its face encoding. In each frame, it checks if the face detected matches the reference with a confidence threshold of 0.6.
Landmark Detection & Head Pose Estimation:
Dlib's landmark detector identifies 68 facial points. Specific points are used to estimate head pose, which provides the yaw and pitch angles. These angles help determine attentiveness.
Attentiveness Scoring:
Using yaw and pitch angles, an attention score is calculated between 0 (not attentive) and 1 (fully attentive). If the attention score is 0.5 or higher, the person is marked as "Attentive."
Logging & Screenshots:
When the person is recognized, their name, date, time, attention status, score, and a screenshot path are logged in a DataFrame.
Screenshots are saved in a folder named "screenshots," and each log entry includes a reference to the image file.
Real-time feedback is shown on the frame, displaying whether "Piyush Singh" is recognized and attentive or not.
At the end of the session, all log data, including attention scores, are saved to attendance_with_attention.xlsx.
![sjbj](https://github.com/user-attachments/assets/5b74c38f-e71f-43a0-9fec-6522c7db2e5b)
![snjd](https://github.com/user-attachments/assets/efb6320d-a924-45ec-9d37-3006b70cecff)



Usage
Launch the main script:
python main.py
Configure settings such as engagement metrics, notification thresholds, and data sources through the provided interface.

Access your customizable dashboard to monitor real-time data and view engagement insights.

License

This project is licensed under the MIT License. See the LICENSE file for details.
