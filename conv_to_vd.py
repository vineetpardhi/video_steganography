import cv2
import numpy as np
import os
from os.path import isfile,join
import natsort

class cnvt_vdo(object):

    def convert_frames_to_video(self,pathIn,pathOut,fps):
        frame_arr=[]
        frames_path= pathIn+'\\frames\\'
        files=[f for f in os.listdir(frames_path) if isfile(join(frames_path,f))]
        
        
        files.sort(key=lambda x: int(x[5:-4]))

        for i in range(len(files)):
            filename=frames_path+files[i]
            img=cv2.imread(filename)
            height,width,layers=img.shape
            size=(width,height)
            frame_arr.append(img)

        out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'XVID'),fps,size)

        for i in range(len(frame_arr)):
            out.write(frame_arr[i])
        out.release()
        return pathIn+"\\"+pathOut
        #print("the video is saved at location"+str(pathIn))

        

