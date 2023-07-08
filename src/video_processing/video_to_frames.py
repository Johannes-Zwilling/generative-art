import cv2
import os


def video_to_frames(video_filename: str):
    # Open the video file
    video = cv2.VideoCapture(video_filename)

    # Create a directory to store the frames
    frame_dir = "frames"
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    # Initialize variables
    frame_count = 0

    # Read and save each frame of the video
    while True:
        # Read the next frame
        ret, frame = video.read()

        # Break the loop if no frame is read
        if not ret:
            break

        # Save the frame as an image file
        frame_filename = f"{frame_dir}/frame_{frame_count:04d}.jpg"
        cv2.imwrite(frame_filename, frame)

        # Increment the frame count
        frame_count += 1

    # Release the video object
    video.release()

    # Print the total number of frames extracted
    print(f"Total frames extracted: {frame_count}")
