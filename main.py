# Hello friend my name is Niket Tongare i crated this script to 
# convert or you can say extract frames from video 

# This script converts the videos from videos folder 
# of same dir to images and then save that images to frames/videoname folder 

# the current gap between frames is 10 
# if you want to change the gap just cange up value 
# when calling save_frames function from main


import os
import numpy as np
import cv2
from glob import glob


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")    


def save_frame(video_path, save_dir,gap):
    name = video_path.split("\\")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{save_path}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path}/{idx}.png", frame)

        idx += 1
    

if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "frames"

    for path in video_paths:
        save_frame(path, save_dir, gap=10)


        