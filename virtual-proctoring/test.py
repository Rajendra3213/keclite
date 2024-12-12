import cv2
import numpy as np

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of output file
filename = "Recording.avi"

# Specify frames per second (fps)
fps = 20.0

# Specify resolution (width, height)
resolution = (640, 480)

# Create VideoCapture object to capture from webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Creating a VideoWriter object to save the recording
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an empty window
cv2.namedWindow("Webcam Live", cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break
    
    # Resize the frame to match the specified resolution
    frame = cv2.resize(frame, resolution)
    
    # Write the frame to the output file
    out.write(frame)
    
    # Display the resulting frame
    cv2.imshow("Webcam Live", frame)
    
    # Stop recording when we press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()

# Destroy all windows
cv2.destroyAllWindows()
