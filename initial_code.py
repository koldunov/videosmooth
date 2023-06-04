import cv2
import numpy as np

# Define the number of frames to smooth
smooth_window = 30

# Open the video file
cap = cv2.VideoCapture('your_imput_file_name.MOV')

# Get the width and height of the frames in the video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec using VideoWriter_fourcc and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('your_output_file_name.mp4', fourcc, 30.0, (frame_width, frame_height))

# Initialize buffer
buffer = []

while cap.isOpened():
    ret, frame = cap.read()

    # Break the loop if this frame is not valid
    if not ret: 
        break

    # Add frame to buffer
    buffer.append(frame)

    # Ensure buffer does not exceed the smooth window size
    if len(buffer) > smooth_window:
        buffer.pop(0)

    # Calculate the average frame
    avg_frame = np.average(buffer, axis=0).astype(np.uint8)

    # Write the averaged frame to file
    out.write(avg_frame)

# Release the VideoWriter and VideoCapture objects
cap.release()
out.release()
