
# exaples
# in command line:
# python videosmooth.py IMG_2871.MOV output7.mp4 average7.jpg --start_time 5 --end_time 10 --smooth_window 10
# Define start time and end time in seconds, smooth_window in frames
# You can skip --start_time, --end_time,  --smooth_window,
# so you can use this command:
# python videosmooth.py IMG_2871.MOV output7.mp4 average7.jpg



import argparse
import cv2
import numpy as np
from tqdm import tqdm

def main(infname, outvname, outiname, start_time, end_time, smooth_window):
    # Open the video file
    cap = cv2.VideoCapture(infname)

    # Get the width and height of the frames in the video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec using VideoWriter_fourcc and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Use H.264 codec
    out = cv2.VideoWriter(outvname, fourcc, fps, (frame_width, frame_height))

    # Initialize buffer
    buffer = []

    # Initialize a running sum and count for average image calculation
    running_sum = None
    frame_count = 0

    # Calculate the start frame and end frame
    start_frame = int(start_time * fps) if start_time else 0
    end_frame = int(end_time * fps) if end_time else int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Initialize progress bar
    pbar = tqdm(total=end_frame-start_frame, ncols=70)

    # Skip frames until the start frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    while cap.isOpened() and frame_count < end_frame - start_frame:
        ret, frame = cap.read()

        # Update progress bar
        pbar.update(1)

        # Break the loop if this frame is not valid
        if not ret: 
            break

        # Add frame to buffer
        buffer.append(frame)

        # Update running sum and count
        if running_sum is None:
            running_sum = frame.astype(np.float64)
        else:
            running_sum += frame
        frame_count += 1

        # Ensure buffer does not exceed the smooth window size
        if len(buffer) > smooth_window:
            buffer.pop(0)

        # Calculate the average frame
        avg_frame = np.average(buffer, axis=0).astype(np.uint8)

        # Write the averaged frame to file
        out.write(avg_frame)

    # Close progress bar
    pbar.close()

    # Release the VideoWriter and VideoCapture objects
    cap.release()
    out.release()

    # Calculate the average of all frames
    avg_image = (running_sum / frame_count).astype(np.uint8)

    # Write the average image to file
    cv2.imwrite(outiname, avg_image)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Smooth video frames and create an average image.')
    parser.add_argument('infname', type=str, help='Input video file name')
    parser.add_argument('outvname', type=str, help='Output video file name')
    parser.add_argument('outiname', type=str, help='Output average image file name')
    parser.add_argument('--start_time', type=int, default=None, help='Start time in seconds (default: start of video)')
    parser.add_argument('--end_time', type=int, default=None, help='End time in seconds (default: end of video)')
    parser.add_argument('--smooth_window', type=int, default=30, help='Number of frames to smooth (default: 30)')
    
    args = parser.parse_args()
    
    main(args.infname, args.outvname, args.outiname, args.start_time, args.end_time, args.smooth_window)

