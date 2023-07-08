import cv2
import os
from typing import Any


def write_image(output_folder: str, frame_filename: str, frame: Any):
    """
    Writes an image to disk using opencv at the prescribed filepath.

    Parameters
    ----------

    frame_filename: str
        Filepath to the location where the image should be stored.
    frame: Any
        The numPy array containing image data.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_filename = f"{output_folder}/{frame_filename}"
    cv2.imwrite(frame_filename, frame)
