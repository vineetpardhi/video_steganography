import string
import cv2
import numpy as np
import sys
from PIL import Image
import os

class encode_data(object):


    def __init__(self):
        self.rgb_list = []
        self.rgb_list_enc = []

    def save_img(self,nurl,copy_url,name):
        img = cv2.imread(copy_url)
        path=nurl 
        cv2.imwrite(os.path.join(path , name), img)
        cv2.waitKey(0)

        return str(os.path.join(path , name))

    def genData(self,data): 
          
        # list of binary codes 
        # of given data 
        newd = []  
          
        for i in str(data,'utf-8'): 
            newd.append(format(ord(i), '08b')) 
        return newd
    def modPix(self,pix1,pix2,data): 
        
        datalist =self.genData(data) 
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
            self.rgb_list=pix2                       
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
            self.rgb_list_enc=pix2
            yield pix[0:3] 
            yield pix[3:6] 
            yield pix[6:9] 
    
    
    def encode_enc(self,newimg1,newimg2, data,enc_length): 
        w = newimg2.size[0] 
        (x, y) = (0, 0) 
        i=0
        for pixel in self.modPix(newimg1.getdata(),newimg2.getdata(), data):
            i+=1
            enc_length+=1 
            
            
            # Putting modified pixels in the new image 
            newimg2.putpixel((x, y), pixel) 
            if (x == w - 1): 
                x = 0
                y += 1
            else: 
                x += 1
            if(i-1==(newimg2.size[0]*newimg2.size[1])//3):
                print('new_frame required')
                return enc_length 


            
        return enc_length
                
    # Encode data into image 
    def encode(self,img1,img2,data,enc_length,url):
        image1 = Image.open(img1, 'r')
        image2=Image.open(img2,'r')  
        if (len(data) == 0): 
            raise ValueError('Data is empty') 
        newimg1 = image1.copy()
        newimg2= image2.copy() 

        newimg3=image2.copy()

        enc_length=self.encode_enc(newimg1,newimg2,data,enc_length) 
        
        # print(self.rgb_list[0:5])
        # print(self.rgb_list_enc[0:5])

        sum_squared_error = 0

        rg1=np.array(self.rgb_list)
        rg2=np.array(self.rgb_list_enc)

     

        rg1.flatten()
        rg2.flatten()

        # for ctr in range(len(rg1)):
        #         err = rg1[ctr] - rg2[ctr]
        #         sum_squared_error += err*err

        # mean_squared_error = sum_squared_error/len(rg1)
        # print('mean squared error is:'+str(mean_squared_error))
        # print('root mean square error is:'+str(pow(mean_squared_error,0.5)))


        
         
        newimg2.save(img2, str(img2.split(".")[1].upper()))
        

        # directory="new_frames"
        # head_tail=os.path.split(url)
        # mod_url = os.path.join(head_tail[0],directory)
        # save_url=mod_url+"\\newframe1"

        # newimg3.save(save_url,str(img2.split(".")[1].upper()))
        return enc_length
  
    