import cv2
from PIL import Image
import os

class exc_frame(object):

    def ext_frames(self,url):
        vidcap = cv2.VideoCapture(url)
        success,image = vidcap.read()
        count = 0
        path = '/home/akhi/Desktop/mp2/frames/'
        while success and count!=5:
            
            cv2.imwrite( os.path.join(path,"frame%d.jpg" % count), image)     # save frame as JPEG file     
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count +=1 

        return count