import cv2
import os
from .load_video import load_video
from .write_image import write_image


def video_to_frames(video_filename: str, images_output_directory: str):
    # Open the video file
    video = load_video(video_filename)

    # Create a directory to store the frames
    if not os.path.exists(images_output_directory):
        os.makedirs(images_output_directory)

    # Initialize variables
    frame_count = 0

    # Read and save each frame of the video
    while True:
        # Read the next frame
        ret, frame = video.read()

        # Break the loop if no frame is read
        if not ret:
            break

        frame_filename = f"{images_output_directory}/frame_{frame_count:04d}.jpg"
        write_image(frame_filename, frame)

        # Increment the frame count
        frame_count += 1

    # Release the video object
    video.release()

    # Print the total number of frames extracted
    print(f"Total frames extracted: {frame_count}")
