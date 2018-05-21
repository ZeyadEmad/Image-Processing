import cv2
import numpy as np

import os

# Playing video from file:
cap = cv2.VideoCapture('video1.mp4')
EOFcheck = cap.read()

datacheck = input("Dataset Ready ?")

Predatacheck = input("Pre-Processing Data Ready ?")

try:
    if not os.path.exists('data1'):
        os.makedirs('data1')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if datacheck != "y":
        # Save image of the current frame in jpg file
        name = './data1/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

    elif datacheck == "y":
        name = './data1/frame' + str(currentFrame) + '.jpg'

    if Predatacheck != "y":
        # Pre Processing Color Based Elimination
        img = cv2.imread(name, 1)
        height, width, channel = img.shape

        for col in range(1, width):
            for row in range(1, height):
                px = img[row, col]
                b, g, r = px
                maxi = max(r,g,b)

                if maxi < 145 and maxi > 55 and maxi == g:
                    px = 0,0,0

                img[row, col] = px


        try:
            if not os.path.exists('data1Pre'):
                os.makedirs('data1Pre')
        except OSError:
            print('Error: Creating directory of data')

        newname = './data1Pre/frame' + str(currentFrame) + '.jpg'
        print('Processing...' + newname)
        cv2.imwrite(newname, img)

    # To stop duplicate images
    currentFrame += 1

    # End of file
    if EOFcheck is None:
        break

cap.release()
cv2.destroyAllWindows()
