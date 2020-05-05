import cv2
from PIL import Image
import os

class exc_frame(object):

    def ext_frames(self,url):
        vidcap = cv2.VideoCapture(url)
        success,image = vidcap.read()
        count = 0
        directory="frames"
        head_tail=os.path.split(url)
        path = os.path.join(head_tail[0],directory)
        os.mkdir(path)
        while success and count!=5:
            
            cv2.imwrite( os.path.join(path,"frame%d.png" % count), image)     # save frame as PNG file     
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count +=1

        return count