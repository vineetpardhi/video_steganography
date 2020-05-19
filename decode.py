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

    def decode(self,img1,img2,flag): 
        image2 = Image.open(img2, 'r')
        image1= Image.open(img1,'r') 
        
        data = '' 
        imgdata1 = iter(image1.getdata()) 
        imgdata2 = iter(image2.getdata())

        
        i=0
        while (True):
            i+=1
            


            pixels1=[value for value in imgdata1.__next__()[:3] +
                                    imgdata1.__next__()[:3] +
                                    imgdata1.__next__()[:3] ]
            
        
            pixels2=[value for value in imgdata2.__next__()[:3] +
                                    imgdata2.__next__()[:3] +
                                    imgdata2.__next__()[:3] ]

            binstr=str()

            for a,b in zip(pixels1[:8],pixels2[:8]):
                if (abs(a-b) % 2 == 0): 
                    binstr += '0'
                else: 
                    binstr += '1'
                    
            data += chr(int(binstr, 2)) 
            if(i-1==(image1.size[0]*image1.size[1])//3 and flag==0 ):
                return data,0
            elif( abs(pixels1[-1]-pixels2[-1]) % 2 != 0):
                print('decoded no more data') 
                return data,1

            

             



    