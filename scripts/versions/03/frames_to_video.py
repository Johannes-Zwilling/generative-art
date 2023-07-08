from generative_art.video_processing.frames_to_video import frames_to_video

if __name__ == "__main__":
    images_folder = "data/versions/00/images"
    output_video_filename = "output4.mp4"

    frames_to_video(images_folder, output_video_filename)
