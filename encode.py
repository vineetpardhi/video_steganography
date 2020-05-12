import string
import cv2
import numpy as np
import sys
from PIL import Image
import os

class encode_data(object):


    def genData(self,data): 
          
        # list of binary codes 
        # of given data 
        newd = []  
          
        for i in str(data,'utf-8'): 
            newd.append(format(ord(i), '08b')) 
        return newd

    def modPix(self,pix1,pix2,data): 
        
        datalist =self. genData(data) 
        lendata = len(datalist) 
        imdata1 = iter(pix1)
        imdata2=iter(pix2) 
    
        for i in range(lendata): 
            
        
            pix1 = [value for value in imdata1.__next__()[:3] +
                                    imdata1.__next__()[:3] +
                                    imdata1.__next__()[:3]] 

            pix2 = [value for value in imdata2.__next__()[:3] +
                                    imdata2.__next__()[:3] +
                                    imdata2.__next__()[:3]]
                                    
            # Pixel value should be made  
            # odd for 1 and even for 0 
            for j in range(0, 8): 
                if (datalist[i][j]=='0') and (abs(pix1[j]-pix2[j])% 2 != 0): 
                    if (abs(pix1[j]-pix2[j]) % 2 != 0): 
                        pix2[j] -= 1
                        
                elif (datalist[i][j] == '1') and (abs(pix1[j]-pix2[j]) % 2 == 0):
                    pix2[j] += 1
                    
            # Eigh^th pixel of every set tells  
            # whether to stop ot read further. 
            # 0 means keep reading; 1 means the 
            # message is over. 
            if (i == lendata - 1): 
                if (abs(pix1[-1]-pix2[-1]) % 2 == 0):
                    pix2[-1] += 1
            else: 
                if (abs(pix1[-1]-pix2[-1]) % 2 != 0): 
                    pix2[-1] -= 1
    
            pix = tuple(pix2) 
            yield pix[0:3] 
            yield pix[3:6] 
            yield pix[6:9] 
    
    def encode_enc(self,newimg1,newimg2, data): 
        w = newimg2.size[0] 
        (x, y) = (0, 0) 
        
        for pixel in self.modPix(newimg1.getdata(),newimg2.getdata(), data): 
            
            # Putting modified pixels in the new image 
            newimg2.putpixel((x, y), pixel) 
            if (x == w - 1): 
                x = 0
                y += 1
            else: 
                x += 1
                
    # Encode data into image 
    def encode(self,img1,img2,data):
        image1 = Image.open(img1, 'r')
        image2=Image.open(img2,'r')  
        if (len(data) == 0): 
            raise ValueError('Data is empty') 
        newimg1 = image1.copy()
        newimg2= image2.copy() 
        self.encode_enc(newimg1,newimg2,data) 
        

        newimg2.save(img2, str(img2.split(".")[1].upper())) 
  
    