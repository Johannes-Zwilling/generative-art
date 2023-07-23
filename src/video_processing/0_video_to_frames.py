from .load_video import load_video
from .write_image import write_image
from uuid import uuid4


def video_to_frames(video_filename: str, images_output_directory: str):
    # Open the video file
    video_frames = load_video(video_filename)

    # Read and save each frame of the video
    frame_count = 0
    uuid_folder_name = uuid4()
    for frame_index, frame in video_frames:
        write_image(f"{images_output_directory}/{uuid_folder_name}", f"frame_{frame_index:04d}.jpg", frame)
        frame_count += 1
        
    # Print the total number of frames extracted
    print(f"Total frames extracted: {frame_count}")
    print(f"Successfully extracted images in folder '{uuid_folder_name}'")
