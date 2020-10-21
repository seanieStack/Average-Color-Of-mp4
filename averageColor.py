import cv2
import numpy as np
import os
from PIL import Image

cap = cv2.VideoCapture('sherk.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print("Error: Creating Derictory of data")

currentFrame = 0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
while (currentFrame < length):
    ret, frame = cap.read()

    name = './data/frame' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)

    currentFrame += 1

cap.release()
cv2.destroyAllWindows()    

def getAverageColor(image_path):

    image = Image.open(curImage)
    width, height = 0, 0
    width, height = image.size

    r, g, b = 0, 0, 0
    count = 0

    for s in range(1, width):
        for t in range(1, height):
            pixl_r, pixl_g, pixl_b = image.getpixel((s, t))
            r += pixl_r
            b += pixl_b
            g += pixl_g
            count += 1
    return ((r//count), (g//count), (b//count))

DIR = './data'
files = next(os.walk(DIR))[2]
numOfFrames = len(files)

for q in range(1, numOfFrames):
    try:
        if not os.path.exists('fin'):
            os.makedirs('fin')
    except OSError:
        print("Error: Creating Derictory of data")

    curImage = DIR + "/frame" + str(q) + ".jpg"
    color = getAverageColor(curImage)

    print(color)

    newImg = Image.new('RGB', (1920, 1080), color)
    newImg = newImg.save("./fin/newFrame" + str(q) + ".jpg")
