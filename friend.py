import os 
import cv2

path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.jpg', '.png' '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)

        images.append( file_name)

print(len(images))
count = len(images)
Frame = cv2.imread(images [0])
h,w,c = Frame.shape
print(h,w,c)

out=cv2.VideoWriter('friendforever.mp4', cv2.VideoWriter_fourcc(*"DIVX"), 1, (w,h))

for friend in range(0,count):
    Frame = cv2.imread(images[friend])
    out.write(Frame)

out.release()