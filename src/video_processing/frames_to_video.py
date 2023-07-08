import os
import cv2

# Directory containing the frames
frame_dir = 'output4'

# Frame rate for the export (modify as needed)
frame_rate = 60

# Get the list of frame filenames in the directory
frame_files = sorted([f for f in os.listdir(frame_dir) if f.endswith('.jpg')])

# Read the first frame to get the dimensions
frame = cv2.imread(os.path.join(frame_dir, frame_files[0]))
height, width, channels = frame.shape

# Create a VideoWriter object to save the frames as an MP4 video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_file = 'output4.mp4'
out = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

# Write each frame to the video file
for frame_file in frame_files:
    frame_path = os.path.join(frame_dir, frame_file)
    frame = cv2.imread(frame_path)
    out.write(frame)

# Release the VideoWriter
out.release()

# Print the output file path
print(f'Video saved as: {output_file}')
