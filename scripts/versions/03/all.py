from video_processing.video_to_frames import video_to_frames
from frame_processing.collect_coordinates import collect_coordinates

if __name__ == "__main__":
    frames_path = video_to_frames("data/versions/03/03.mp4", "data/versions/03/images")
    #print(images_path)

    coordinates = collect_coordinates(frames_path)
