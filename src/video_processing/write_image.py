import cv2
import os
from .load_video import load_video
from typing import Any


def write_image(frame_filename: str, frame: Any):
    """
    Writes an image to disk using opencv at the prescribed filepath.

    Parameters
    ----------

    frame_filename: str
        Filepath to the location where the image should be stored.
    frame: Any
        The numPy array containing image data.
    """
    cv2.imwrite(frame_filename, frame)
