import string
import cv2
import numpy as np
import sys
from PIL import Image
 

class encode_data(object):

    def iter_bin(self,s):
        sb = s.encode('ascii')
        return (format(b, '08b') for b in sb)

    def conv_ascii(self,cphr_txt):
        obj=encode_data()
        th=''
        for s in obj.iter_bin(str(cphr_txt)):
            th=th+s+'T'
        tha = list(th)
        tha[-1] = 'F'
        th = str(tha)
        th = th.replace('\'','')
        th = th.replace(',','')
        th = th.replace('[','')
        th = th.replace(']','')
        th = th.replace(' ','')

        return th
    
    def flip(self,v):
        bv=list(bin(v)[2:])
        #print(bv)
        if(bv[7]!='1'):
            bv[7]='1'
        else:
            bv[7]='0'
        #print(bv)
        dec=0
        for dig in bv:
            dec=dec*2 + int(dig)
        #print(dec)
        return int(dec)

        
    def encode(selfc,rgb_list1,rgb_list2,len_counter,th):
        # store_counter=(len(th)//8)
        # print(rgb_list2)
        f_obj=encode_data()

        if len(rgb_list1)==len(rgb_list2):  #if the length of both the list is same then only proceed
            counter=18
            ef = 1
            for i in range(len(rgb_list1)):
                if(ef == 0):
                    break
                for j in range(0,3):
                    if(counter >= len(th)):
                        ef == 0
                        break
                    len_counter+=1
                    d1=rgb_list1[i][j]%10
                    d2=rgb_list2[i][j]%10
                    mod=abs(d1-d2)%2
                    if(mod==0 and (th[counter])== '0'):   #if difference is even and encoding is  0
                    #--------------do nothing---------------
                    # print('Data is 0 and mod is 0')
                        counter+=1
                        continue

                    elif(mod==1 and (th[counter]=='1')): #if difference is odd and encoding is 1
                    #--------------do nothing--------------------
                    #  print('Data is 1 and mod is 1')
                        counter+=1
                        continue
                    
                    elif(mod==0 and th[counter]=='1'):    
                    #-----------flip------------------------
                     # print('Data is 0 and mod is 0')
                        counter+=1
                        rgb_list2[i][j]=f_obj.flip(rgb_list2[i][j])
                        
                    #-----------------------# 
                    elif(mod==1 and th[counter]== '0'):
                    #-------------flip---------------------
                        counter+=1
                        rgb_list2[i][j]=f_obj.flip(rgb_list2[i][j])
                    
                    elif(th[counter] == 'F'):
                        print('no more data')
                        counter+=1
                        if(mod == 0):
                        #flip
                            rgb_list2[i][j]=f_obj.flip(rgb_list2[i][j])
                        else:
                        #do nothing
                            return -1
                            continue
                    elif(th[counter] == 'T'):
                        # print('there is data')
                        counter+=1
                        if(mod == 1):
                        #flip
                        # print('flipped')
                            rgb_list2[i][j]=f_obj.flip(rgb_list2[i][j])
                        else:
                        #do nothing
                            continue
                    
        #print(rgb_list2)
        # print('store_counter:'+str(store_counter))
        return len_counter
 

     
    def extract_image(self,a,b):                 #-----extract image----#
        img_path1='C:/Users/vinee/OneDrive/Documents/Video Steganography/video_steganography/frames/frame'+str(a)+'.png'
        img_file1 = img_path1
        img = cv2.imread(img_file1, cv2.IMREAD_COLOR)  
        img_path2='C:/Users/vinee/OneDrive/Documents/Video Steganography/video_steganography/frames/frame'+str(b)+'.png'
        img_file2=img_path2
        return img_file1,img_file2

    def rgb_of_pixel(self,img_path, x, y):
        im = Image.open(img_path).convert('RGB')
        r, g, b = im.getpixel((x, y))
        a = [r, g, b]
        return a
    

    def get_pixel(self,img_file1,img_file2,cphr_txt):
        r_obj=encode_data()
        #creating list 1 for 1st frame 
        rgb_list1=[]
        
        for i in range(0,3*len(cphr_txt)+3):
            rgb_list1.append(r_obj.rgb_of_pixel(img_file1,i,0))  
        #print(rgb_list1)
        
        #creating list 2 for 2nd frame
        rgb_list2=[]
        for i in range(0,3*len(cphr_txt)+3):
            rgb_list2.append(r_obj.rgb_of_pixel(img_file2,i,0))
        #print(rgb_list2)

        return rgb_list1,rgb_list2
     
    
        
    
    def put_back(self,img2,rgb_list2,cphr_txt):
        im=Image.open(img2) 
        for i in range(0,3*len(cphr_txt)+3):
            im.putpixel((i,0),(tuple(rgb_list2[i])))
        im.save('C:/Users/vinee/OneDrive/Documents/Video Steganography/video_steganography/frames/framenew.png')



