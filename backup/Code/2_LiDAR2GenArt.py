# imports
import cv2
import glob
import numpy as np
import os

# resolution 1440px
slices = 50
dotSizer = 0.07

###############################################################
# Get Images
###############################################################
gotCoordinates = False
printed = False
frameNo = -1

for file in sorted(glob.glob("/Users/johanneszwilling/Desktop/00XX__Record3d/videos/03/frames/*.jpg")):

    frameNo += 1

    img = cv2.imread(file)
    # print(file)
    # print('height:', img.shape[0],', width:', img.shape[1])

    # use height and width to determine stepSize
    stepSize = int(np.ceil(img.shape[0]/slices))

    if not printed:
        print('Grid width:', stepSize, 'Pixels')
        print('Max dot size:', int(dotSizer * 255), 'Pixels')

        printed = True

###############################################################
# Collect Coordinates
###############################################################

    if not gotCoordinates:

        #print('Getting Coords')
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
        gotCoordinates = True

        # for _ in coordinates:
        #     print(_)
        # print('len(coordinates):', len(coordinates))

        continue

###############################################################
# Collect pixel values
###############################################################

    else:

        #print('NOT getting Coords')

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

        #img = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        #img[:] = (179, 200, 250)

        for coordinate, pixel in zip(coordinates, pixels):
            if pixel <= 50:
               pixel = 50

            # cv.circle(image, centerOfCircle, radius, color, thickness)
            #cv2.circle(img, tuple(coordinate), int(pixel * dotSizer), (255 - int(pixel), 255 - int(pixel), 255 - int(pixel)), -1, lineType = cv2.LINE_AA)
            cv2.circle(img, tuple(coordinate), int(pixel * dotSizer), (0,0,0), -1, lineType = cv2.LINE_AA)
            #cv2.rectangle(img, tuple(coordinate), tuple([int(tuple(coordinate)[0]+ (pixel * dotSizer)), int(tuple(coordinate)[1]+ (pixel * dotSizer))]), (156, 71, 96), -1)

        #print(tuple([tuple(coordinate)[0]+ (pixel * dotSizer), tuple(coordinate)[1]+ (pixel * dotSizer)]))
        #print(pixel)

        window_name = 'stream'
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        img = cv2.flip(img, 1)
        #cv2.imshow(window_name, img)
        cv2.moveWindow(window_name, 50, 50)
        cv2.waitKey(1)
        cv2.destroyAllWindows()

###############################################################
# Saving
###############################################################

    # Defines filename for image-saving. Frame-count helps naming the image-files chronologically.
    filename = "screen_%04d.jpg" % (frameNo)

    # Saves frame as image in computer's home folder
    cv2.imwrite(filename, img)
    print('Saving frame:', frameNo)





        #
