import binascii
from PIL import Image
import os
import string
import cv2
import numpy as np
import sys
from PIL import Image
import os

class decd_data(object):



    def extract_image(self,a,b,url):                 #-----extract image----#
        head_tail=os.path.split(url)
        img_path=head_tail[0].replace("\\","/")
        img_path1=img_path+'/frames/frame'+str(a)+'.png'
        img_file1 = img_path1
        img = cv2.imread(img_file1, cv2.IMREAD_COLOR)  
        img_path2=img_path+'/frames/frame'+str(b)+'.png'
        img_file2=img_path2
        return img_file1,img_file2


    def decode(self,img):
        #print(img)
        image = Image.open(img, 'r') 
        
        data = '' 
        imgdata = iter(image.getdata()) 
        
        while (True): 
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]] 
            # string of binary data 
            binstr = '' 
            
            for i in pixels[:8]: 
                if (i % 2 == 0): 
                    binstr += '0'
                else: 
                    binstr += '1'
                    
            data += chr(int(binstr, 2)) 
            if (pixels[-1] % 2 != 0):
                print(data) 
                return data