import cv2 as cv
import face_recognition
import dlib
import pandas as pd
import numpy as np
from datetime import datetime
import os
from imutils import face_utils

# Initialize dlib's face detector and facial landmark predictor
p = "C:\\Users\\piyus\\anaconda3\\Lib\\site-packages\\face_recognition_models\\models\\shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(p)

# Create a directory to save screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Load the known image
known_image = face_recognition.load_image_file("C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\p.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time', 'Screenshot', 'Attentive', 'Attention Score', 'Blinks']
df = pd.DataFrame(columns=columns)

# Initialize variables
attention_scores = []
blink_count = 0  # Counter for blinks
EAR_THRESHOLD = 0.25  # Eye aspect ratio threshold for detecting a blink
CONSEC_FRAMES = 3  # Consecutive frames to confirm a blink
frame_count = 0
blink_frame_counter = 0

# Launch the live camera or video
cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Camera not working")
    exit()

# Helper functions
def eye_aspect_ratio(eye):
    # Compute the distances between the two sets of vertical eye landmarks (x, y) coordinates
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    # Compute the distance between the horizontal eye landmark (x, y) coordinates
    C = np.linalg.norm(eye[0] - eye[3])
    # Compute the eye aspect ratio
    EAR = (A + B) / (2.0 * C)
    return EAR

while True:
    frame_count += 1
    ret, frame = cam.read()
    
    if not ret:
        print("Can't receive frame")
        break

    frame = cv.resize(frame, (640, 480))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)
    if not faces:
        continue

    for face in faces:
        # Extract landmarks
        landmarks = landmark_predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)
        
        # Extract eye coordinates
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]
        
        # Calculate EAR for both eyes
        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        avg_EAR = (left_EAR + right_EAR) / 2.0

        # Check if EAR is below the blink threshold
        if avg_EAR < EAR_THRESHOLD:
            blink_frame_counter += 1
        else:
            if blink_frame_counter >= CONSEC_FRAMES:
                blink_count += 1  # Blink detected
            blink_frame_counter = 0

        # Draw eye landmarks
        for (x, y) in left_eye:
            cv.circle(frame, (x, y), 2, (0, 255, 0), -1)
        for (x, y) in right_eye:
            cv.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # Draw rectangle and display blink count
        cv.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
        cv.putText(frame, f"Blinks: {blink_count}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Optional: Track attentiveness (you can reuse your attentiveness logic here if needed)

    # Display the frame
    cv.imshow("Live Video Feed", frame)

    # Exit loop on 'q' key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Create a new entry for the attendance with blink count
new_entry = pd.DataFrame({
    'Name': ['Piyush Singh'],
    'Date': [datetime.now().strftime("%Y-%m-%d")],
    'Time': [datetime.now().strftime("%H:%M:%S")],
    'Screenshot': [''],
    'Attentive': [''],
    'Attention Score': [''],
    'Blinks': [blink_count]  # Total blink count
})

# Concatenate the new entry with the existing DataFrame
df = pd.concat([df, new_entry], ignore_index=True)

# Save the DataFrame to Excel
df.to_excel(r'C:\Users\piyus\OneDrive\Desktop\coding\FACE UNDER RECO\face_recognition\avg_atten_score\attendance_with_attention_and_blinks.xlsx', index=False)

print(f"Saved attendance log with attentiveness and blink count. Total Blinks: {blink_count}")

# Release resources
cam.release()
cv.destroyAllWindows()
