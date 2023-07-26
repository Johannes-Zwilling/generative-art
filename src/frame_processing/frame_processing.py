from .load_frame import load_frame
from .collect_coordinates import collect_coordinates
from .collect_pixel_values import collect_pixel_values

#from video_processing.video_to_frames import video_to_frames.uuid_folder_name


def frame_processing():

    # load frame
    frame = load_frame()

    # load coordinates
    coordinates = collect_coordinates()

    # sample pixel values
    pixel_values = collect_pixel_values()

    # store pixel values

    # How to find unique uuid4-folder? 
    ## video_to_frames.uuid_folder_name?

    # How to store generative_parameters?

    pass