import cv2                      # reading and writing video
import numpy as np              # calculaing colors of input images in arrays
import os                       # making directories and os details
from sys import exit            # exiting file instead of throwing exeptions
from shutil import rmtree       # deleting file directories with all files
from PIL import Image           # create new images
from easygui import fileopenbox # get input video file
from tqdm import tqdm           # progress bars

# function to add the average color to array
def colorOfCurrentFrame(frame: str) -> None:
    try:
        # creates a img object
        img = cv2.imread(frame, cv2.IMREAD_COLOR)

        # gets the average of the 3d array and appends to end of array
        averageColor.append(np.average(np.average(img, axis=0), axis=0))        
    except:
        exit("Error Reading Frame")

def main() -> None:
    # checks if ./temp exisits, if yes, it deletes it 
    # and all its content, then creates it, if no it creates it
    try:
        if os.path.exists('./temp'):
            rmtree("./temp")
        os.makedirs('./temp')
    except OSError:
        exit("Error: Creating Derictory of data")

    # Gets input video from file browser
    inputVideo = fileopenbox(filetypes=["*.mp4"])

    # close if user inputs nothing
    if inputVideo == None:
        exit("Please Select A video File")

    # sets up our capture object
    cap = cv2.VideoCapture(inputVideo)

    # if capture device fails, close program
    if not cap.isOpened():
        exit("Error Creating Capture Device")

    # gets the number of frames for the input video
    length_of_input_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    INPUT_FPS = cap.get(cv2.CAP_PROP_FPS)

    # loops through all frames in video
    for currentFrame in tqdm(range(0, length_of_input_video),\
        desc="Saving Frames As Images"):

        # reads current frame
        ret, frame = cap.read()

        # if current frame doesn't exist
        if ret == False:
            break

        # sets the name of the next frame
        name = f'./temp/frame{str(currentFrame)}.jpg'

        # saves an image of the currrent frame
        cv2.imwrite(name, frame)

    # closes video capture objects
    cap.release()
    cv2.destroyAllWindows()

    # creates arrary to list of arrays
    global averageColor
    averageColor = []

    # checks if ./tmp exisits, if yes, it deletes it and all
    # its content, then creates it, if no it creates it
    try:
        if os.path.exists('./tmp'):
            rmtree("./tmp")
        os.makedirs('./tmp')
    except OSError:
        print("Error: Creating Derictory of data")

    # loops through frames
    for i in tqdm(range(0, len(next(os.walk("./temp"))[2])),\
        desc="Finding average color of frames"):

        colorOfCurrentFrame(f"./temp/frame{i}.jpg")

    for i, color in enumerate(tqdm(averageColor,\
        desc="Creating images of New Color")):

        # creates a new image with each color
        img = Image.new('RGB', (1920, 1080), (int(
            color[2]), int(color[1]), int(color[0])))
        ret = img.save(f"./tmp/finished{i}.jpg")

    images = []
    # loops through all images in tmp dir
    for i in tqdm(range(0, len(next(os.walk("./tmp"))[2])),\
        desc="Saving Collect File Locations"):

        # addes image location to end of image array
        images.append(f"./tmp/finished{i}.jpg")

    # setup for video writer
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    video = cv2.VideoWriter("output.avi", 0, INPUT_FPS, (width, height))

    # loops though all images in images array
    for image in tqdm(images, desc="Compiling Images to a Video"):
        # writes each image to the end of the video
        video.write(cv2.imread(image))

    # closes all windows and releases video object
    cv2.destroyAllWindows()
    video.release()

    # deletes all tmp dirs
    rmtree("./temp")
    rmtree("./tmp")

if __name__ == "__main__":
    main()
