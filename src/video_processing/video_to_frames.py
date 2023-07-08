from .load_video import load_video
from .write_image import write_image


def video_to_frames(video_filename: str, images_output_directory: str):
    # Open the video file
    video = load_video(video_filename)

    # Create a directory to store the frames

    # Initialize variables
    frame_count = 0

    # Read and save each frame of the video
    while True:
        # Read the next frame
        ret, frame = video.read()

        # Break the loop if no frame is read
        if not ret:
            break

        write_image(images_output_directory, "frame_{frame_count:04d}.jpg", frame)

        # Increment the frame count
        frame_count += 1

    # Release the video object
    video.release()

    # Print the total number of frames extracted
    print(f"Total frames extracted: {frame_count}")
