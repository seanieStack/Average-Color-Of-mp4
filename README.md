#Average Color of A Video
#### Description:
Asks the user for a video.

Takes each frame from of a video,
saves it as a file in a temp Directory,
calulates the average color of that frame,
creates new images that are the average color,
then recompiles all those images back into an output video file.

##### Requirements:
* Open CV2
`pip3 install opencv-python`

* Numpy
`pip install numpy`

* Python Image Library
`pip install pillow`

* EasyGUI
`pip install easygui`

* tqdm
`pip install tqdm`

* Requires to be run on an OS with a graphical interface

##### What Imports Do what?

The python files imports multiple libraries, including `Numpy`, `Python Image Library`, `Open CV 2` and `EasyGUI`.

Numpy is used to do Faster arthicmatic on the very large 3D arrays.

Python Image Library is used to create new images given an rgb value, hight and width.

Open CV 2 is used for disassembling the input video and recompiling the video at the end.

EasyGUI is used to get Input file from the user.

---

##### Rought Description
The first thing the program does is ask the user to select the input video.
It then breaks a video up into many images that it saves into a directory after
this it then loops through all these images and calculates the average color of
each and saves it to an array it then creates an image using PIL and saves that
to another temp directory once these have been created then loads all these
images at appends it to the end of video object created by open cv.

---

##### Step by Step Guide
1. Imports
2. Creates ./temp Directory
3. Gets input video using EasyGUI
4. Creates A Capture Device
5. Get Lenght and FPS of video and Stores in Varibles
6. Loops through each frame in video and save a an image
7. Create ./tmp Directory
8. Loop through each image in ./tmp
9. Call function each image, caluclate the average value of each using Numpy
10. Add the average color to an array
11. Loop through the array
12. Create a new image using the average color and save it to disk
13. create a new video object using Open CV
14. loop through all images in ./tmp
15. Save video
16. Release cv 2 windows and video object
17. Delete ./tmp and ./temp

---

##### Why make this?

I decided to make this as i had some videos for school work.
Someone said to me that my colours in the video was all over the place.
He said that it should change color less or less sporadically.
I was coming to the end of cs50, so i wanted to my new found skills to the test.
My First version was painfully slow, i totally redisgned the program.
And Found my main issue was a very slow way find the average of the 3D array.
After trying a few fixes, i found numpy array artmatic, which was alot more effecient.
I ended up having a speed increase of over 500% going from 6 minute to run to only 1
for a 15 second video, while it may still not be the fastest. I am happy with it.

---

Thanks for Reading - Seanie ^^
