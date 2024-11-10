import cv2 as cv
import face_recognition
import pandas as pd
from datetime import datetime, timedelta
import os

# Create a directory to save screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Load the known image of Piyush Singh
known_image = face_recognition.load_image_file("C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\p.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time', 'Screenshot']
df = pd.DataFrame(columns=columns)

# Launch the live camera or video
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

# Set thresholds and parameters
confidence_threshold = 0.6
frame_skip = 2
frame_count = 0
recognition_count = 0
recognized_names = set()

# Time tracking variables
last_recognition_time = None
entry_time = None
entry_duration = timedelta(minutes=2)
gap_time = timedelta(minutes=5)

try:
    while True:
        ret, frame = cam.read()
        
        if not ret:
            print("Can't receive the frame")
            break

        frame = cv.resize(frame, (640, 480))
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            continue

        face_encodings = face_recognition.face_encodings(frame, face_locations)
        recognized = False

        for face_encoding in face_encodings:
            distance = face_recognition.face_distance([known_faces], face_encoding)[0]

            if distance < confidence_threshold:
                recognized = True
                now = datetime.now()

                if last_recognition_time is None or (now - last_recognition_time) >= entry_duration:
                    screenshot_filename = f"screenshots/Piyush_Singh_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                    cv.imwrite(screenshot_filename, frame)

                    new_entry = pd.DataFrame({
                        'Name': ['Piyush Singh'],
                        'Date': [now.strftime("%Y-%m-%d")],
                        'Time': [now.strftime("%H:%M:%S")],
                        'Screenshot': [screenshot_filename]
                    })
                    df = pd.concat([df, new_entry], ignore_index=True)
                    last_recognition_time = now
                    entry_time = now

                elif (now - entry_time) >= gap_time:
                    screenshot_filename = f"screenshots/Piyush_Singh_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                    cv.imwrite(screenshot_filename, frame)

                    new_entry = pd.DataFrame({
                        'Name': ['Piyush Singh'],
                        'Date': [now.strftime("%Y-%m-%d")],
                        'Time': [now.strftime("%H:%M:%S")],
                        'Screenshot': [screenshot_filename]
                    })
                    df = pd.concat([df, new_entry], ignore_index=True)
                    entry_time = now

                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv.putText(frame, 'Piyush Singh', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                               (255, 0, 0), 2, cv.LINE_AA)

        if not recognized:
            cv.putText(frame, 'Not Piyush Singh', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (255, 0, 0), 2, cv.LINE_AA)

        cv.imshow('Video Stream', frame)

        if cv.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if not df.empty:
        df.to_excel("C:\\Users\\piyus\\OneDrive\\Desktop\\coding\\FACE UNDER RECO\\excel_dt\\attendance_with_screenshots.xlsx", index=False)
        print("Attendance and screenshots saved.")

    cam.release()
    cv.destroyAllWindows()
