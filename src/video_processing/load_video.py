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
    return cv2.VideoCapture(video_filename)
