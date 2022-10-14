import cv2
import os

path = "IMAGES"
images = []

for i in os.listdir(path):
    root, ext = os.path.splitext(i)
    if ext in [".jpg",".jpeg",".png",".webp"]:
        file_name = path + "/" + i
        print(file_name)
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
width, height , channels = frame.shape
size = (width , height)
out = cv2.VideoWriter("friendshipMeansALot.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8 , size)

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
out.write(frame) 
out.release() 
    # releasing the video generated 
print("Done")










