from video_processing.video_to_frames import video_to_frames

if __name__ == "__main__":
    images_path = video_to_frames("data/versions/03/03.mp4", "data/versions/03/images")

    print(images_path)
