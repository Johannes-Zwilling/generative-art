import cv2
import os


def load_video(video_filename: str):
    """
    Loads a video based on its filepath into memory for further processing.

    Parameters
    ----------

    video_filename: str
        Path where the video file is located.
    """
    video_streamer = cv2.VideoCapture(video_filename)
    frame_index = 0
    frame = None
    while True:
        there_are_more_frames, frame = video_streamer.read()
        if not there_are_more_frames:
            video_streamer.release()
            return

        yield frame_index, frame
        frame_index += 1
