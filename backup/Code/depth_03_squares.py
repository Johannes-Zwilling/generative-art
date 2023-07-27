# imports
import cv2
import glob
import numpy as np

# resolution 476px
slices = 70
dotSizer = 0.015


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
        #cv2.circle(img, tuple(coordinate), int(pixel * dotSizer), (0,0,0), -1, lineType = cv2.LINE_AA)
        # cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.rectangle(img, tuple(coordinate), tuple([int(tuple(coordinate)[0]+ (pixel * dotSizer)), int(tuple(coordinate)[1]+ (pixel * dotSizer))]), (0,0,0), -1)

    #print(tuple([tuple(coordinate)[0]+ (pixel * dotSizer), tuple(coordinate)[1]+ (pixel * dotSizer)]))

    window_name = 'stream'
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = cv2.flip(img, 1)
    cv2.imshow(window_name, img)
    cv2.moveWindow(window_name, 100, 300)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
