from .load_video import load_video
from .write_image import write_image


def video_to_frames(video_filename: str, images_output_directory: str):
    # Open the video file
    video_frames = load_video(video_filename)

    # Read and save each frame of the video
    frame_count = 0
    for frame_index, frame in video_frames:
        write_image(images_output_directory, f"frame_{frame_index:04d}.jpg", frame)
        frame_count += 1

    # Print the total number of frames extracted
    print(f"Total frames extracted: {frame_count}")
