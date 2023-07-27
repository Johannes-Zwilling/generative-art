# imports
import cv2
import glob
import numpy as np

# resolution 476px
slices = 50
dotSizer = 50


###############################################################
# Get Images
###############################################################
for file in sorted(glob.glob("/Users/johanneszwilling/Desktop/00XX__Record3d/video/imagesConverted/*.png")):

    img = cv2.imread(file)
    #print(file)
    #print('height:', img.shape[0],', width:', img.shape[1])

    # use height and width to determine stepSize
    stepSize = round(img.shape[0]/slices)
    #print('Every', stepSize, 'Pixel')


###############################################################
# Collect Coordinates
###############################################################

    coordinates = []
    xCord = 0
    yCord = 0

    # Collect and save coordinates
    # column level
    for y in range(img.shape[0]):
        coordinate = []

        if y % stepSize != 0:
            continue
        yCord = y

        #row/pixel level
        for x in range(img.shape[1]):
            if x % stepSize != 0:
                continue
            xCord = x

            coordinate.append([xCord, yCord])


        coordinates.extend(coordinate)

    # for _ in coordinates:
    #     print(_)
    # print('len(coordinates):', len(coordinates))


###############################################################
# Collect pixel values
###############################################################

    # get pixel value
    # middle
    #pixel = img[int(img.shape[0]/2), int(img.shape[1]/2)][0]
    # upper right
    #pixel = img[stepSize, int(img.shape[1] - 1)][0]
    # lower left
    #pixel = img[int(img.shape[0] - 1), stepSize][0]
    #print(pixel)

    pixels = []

    for _ in coordinates:
        pixel = img[_[0], _[1]][0]
        pixels.append(pixel)

    # for _ in pixels:
    #     print(_)


###############################################################
# Draw circles
###############################################################

    img = np.zeros((img.shape), np.uint8)
    img.fill(255)

    for coordinate, pixel in zip(coordinates, pixels):
        # cv.circle(image, centerOfCircle, radius, color, thickness)
        cv2.circle(img, tuple(coordinate), int(pixel/dotSizer), (0,0,0), -1, lineType = cv2.LINE_AA)



    window_name = 'stream'
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = cv2.flip(img, 1)
    cv2.imshow(window_name, img)
    cv2.moveWindow(window_name, 500, 300)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
