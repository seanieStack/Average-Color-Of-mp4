import cv2
import numpy as np
import os
import sys
import shutil
from PIL import Image
import easygui

INPUT_FPS = 1

# checks if ./temp exisits, if yes, it deletes it and all its content, then creates it, if no it creates it
try:
    if os.path.exists('./temp'):
        shutil.rmtree("./temp")

    os.makedirs('./temp')
except OSError:
    print("Error: Creating Derictory of data")

inputVideo = easygui.fileopenbox(filetypes=["*.mp4"])

if inputVideo == None:
    sys.exit("Please Select A video File")

# sets up our capture object
cap = cv2.VideoCapture(inputVideo)

if not cap.isOpened():
    sys.exit("Error Creating Capture Device")

# gets the number of frames for the input video
length_of_input_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
INPUT_FPS = cap.get(cv2.CAP_PROP_FPS)


# for counter
lastPercent = 0

# loops through all frames in video
for currentFrame in range(0, length_of_input_video):

    # reads current frame
    ret, frame = cap.read()

    # if current frame doesn't exist
    if ret == False:
        break

    currentPercent = round((currentFrame / length_of_input_video)*100)
    if currentPercent != lastPercent:
        print(
            f"Creating Frames: {round((currentFrame /  length_of_input_video)*100)}%")
        lastPercent = currentPercent

    # sets the name of the next frame
    name = f'./temp/frame{str(currentFrame)}.jpg'

    # saves an image of the currrent frame
    cv2.imwrite(name, frame)

# closes video capture objects
cap.release()
cv2.destroyAllWindows()

# creates arrary to list of arrays
averageColor = []

# function to add the average color to array


def colorOfCurrentFrame(frame):

    try:
        # creates a img object
        img = cv2.imread(frame, cv2.IMREAD_COLOR)

        # gets height and width of the current image
        height, width, channels = img.shape

        # gets the average of the 3d array
        bgr = np.average(np.average(img, axis=0), axis=0)

        # adds new color to end of color array
        averageColor.append(bgr)
    except:
        sys.exit("Error Reading Frame")


# checks if ./tmp exisits, if yes, it deletes it and all its content, then creates it, if no it creates it
try:
    if os.path.exists('./tmp'):
        shutil.rmtree("./tmp")

    os.makedirs('./tmp')
except OSError:
    print("Error: Creating Derictory of data")

# loops through frames
averageColorPercent = 0
for i in range(0, len(next(os.walk("./temp"))[2])):
    currentPercent = round(i / len(next(os.walk("./temp"))[2]) * 100)

    if currentPercent != averageColorPercent:
        print(f"Getting Average Color: {currentPercent}%")
        averageColorPercent = currentPercent

    colorOfCurrentFrame(f"./temp/frame{i}.jpg")

i = 0
framePercent = 0
for color in averageColor:
    # percent counter
    currentPercent = round((i / len(averageColor)) * 100)
    if currentPercent != framePercent:
        print(f"Generating New Frames: {currentPercent}%")
        framePercent = currentPercent

    # creates a new image with each color
    img = Image.new('RGB', (1920, 1080), (int(
        color[2]), int(color[1]), int(color[0])))
    ret = img.save(f"./tmp/finished{i}.jpg")

    i = i + 1

images = []
# loops through all images in tmp dir
tmpPercent = 0
for i in range(0, len(next(os.walk("./tmp"))[2])):

    # percent counter
    currentPercent = round((i / len(next(os.walk('./tmp'))[2])) * 100)
    if currentPercent != tmpPercent:
        print(
            f"Gathering Images { currentPercent}%")
        tmpPercent = currentPercent

    # addes image location to end of image array
    images.append(f"./tmp/finished{i}.jpg")


# setup for video writer
frame = cv2.imread(images[0])
height, width, layers = frame.shape
video = cv2.VideoWriter("output.avi", 0, INPUT_FPS, (width, height))

it = 0
imgPercent = 0

# loops though all images in images array
for image in images:
    # percent counter
    currentPercent = round((it / len(images)) * 100)
    if currentPercent != imgPercent:
        print(f"Writing Images to Video {currentPercent}%")
        imgPercent = currentPercent
    it += 1

    # writes each image to the end of the video
    video.write(cv2.imread(image))

# closes all windows and releases video object
cv2.destroyAllWindows()
video.release()

# deletes all tmp dirs
shutil.rmtree("./temp")
shutil.rmtree("./tmp")
