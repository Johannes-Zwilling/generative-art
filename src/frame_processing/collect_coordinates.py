from .load_frame import load_frame
import cv2


def collect_coordinates(frames_path: str, slices = 50):
     img = load_frame()

     # get shape
     #print(img.shape[0])

     # use shape with slices to get coordinates 
     # store how?

     #print('Collect coordinates')
     print(frames_path)

     #return coordinates



""" 
def collect_coordinates(frame_filename: str,  slices: int):

    # Create empty list
    coordinates = []

    x_cord = 0
    y_cord = 0

    # Take in frame
    img = 

    # Get img.shape[0] (this assumes frame has always aspect ratio of 1:1)
    
    # column level
    for y in range(img.shape[0]):

        # Use slices to derive coordinates
        if y % step_size != 0:
                continue
            y_cord = y

            #row/pixel level
            for x in range(img.shape[1]):
                if x % step_size != 0:
                    continue
                x_cord = x

                coordinate.append([x_cord, y_cord])

            # Write coordinates to list
            coordinates.extend(coordinate)
        
    # Return list
    #return coordinates
    
    pass 

"""