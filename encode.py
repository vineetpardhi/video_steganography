import string
import cv2
import numpy as np
import sys
from PIL import Image
import os

class encode_data(object):

    def iter_bin(self,s):
        sb = s.encode('ascii')
        return (format(b, '08b') for b in sb)

    def conv_ascii(self,cphr_txt):
        th=''
        for s in self.iter_bin(str(cphr_txt)):
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

        
    def encode(self,rgb_list1,rgb_list2,len_counter,th):
        # store_counter=(len(th)//8)
        # print(rgb_list2)

        if len(rgb_list1)==len(rgb_list2):  #if the length of both the list is same then only proceed
            counter=0
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
                        rgb_list2[i][j]=self.flip(rgb_list2[i][j])
                        
                    #-----------------------# 
                    elif(mod==1 and th[counter]== '0'):
                    #-------------flip---------------------
                        counter+=1
                        rgb_list2[i][j]=self.flip(rgb_list2[i][j])
                    
                    elif(th[counter] == 'F'):
                        print('no more data')
                        counter+=1
                        if(mod == 0):
                        #flip
                            rgb_list2[i][j]=self.flip(rgb_list2[i][j])
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
                            rgb_list2[i][j]=self.flip(rgb_list2[i][j])
                        else:
                        #do nothing
                            continue
                    
        #print(rgb_list2)
        # print('store_counter:'+str(store_counter))
        return len_counter
 

     
    def extract_image(self,a,b,url):                 #-----extract image----#
        head_tail=os.path.split(url)
        img_path=head_tail[0].replace("\\","/")
        img_path1=img_path+'/frames/frame'+str(a)+'.png'
        img_file1 = img_path1
        img = cv2.imread(img_file1, cv2.IMREAD_COLOR)  
        img_path2=img_path+'/frames/frame'+str(b)+'.png'
        img_file2=img_path2
        return img_file1,img_file2

    def rgb_of_pixel(self,img_path, x, y):
        im = Image.open(img_path)
        r, g, b = im.getpixel((x, y))
        a = [r, g, b]
        return a
    

    def get_pixel(self,img_file1,img_file2,cphr_txt,th):
                #--------------------------creating list 1 for 1st frame----------------------------------------------# 
        rgb_list1=[]
        im1_obj=cv2.imread(img_file1, cv2.IMREAD_COLOR)
        w1, h1, c1 = im1_obj.shape


        if(len(th)<=h1):                #if the length of the data is less than columns in the image
            for i in range(0,(len(th)+24)):
                rgb_list1.append(self.rgb_of_pixel(img_file1,i,0))
        else:
            l1=len(th)
            row_counter1=0
            while(l1>=h1):
                l1-=h1
                for i in range(h1):
                    rgb_list1.append(self.rgb_of_pixel(img_file1,i,row_counter1)) 
                row_counter1+=1
            if(l1>=0 and l1<=h1):
                for i in range(l1):
                    rgb_list1.append(self.rgb_of_pixel(img_file1,i,row_counter1))
            print(row_counter1)
        
        
            #-------------------------creating list 2 for 2nd frame-------------------------------------------------#

        rgb_list2=[]
        im2_obj=cv2.imread(img_file2, cv2.IMREAD_COLOR)
        w2, h2, c2 = im1_obj.shape
        if(len(th)+24<=h2):
            print('1st condition ho rha hai')          #if the length of the data is less than columns in the image
            for i in range(0,(len(th)+24)):
                rgb_list2.append(self.rgb_of_pixel(img_file2,i,0))
        else:
            print('2nd Condition ho rha hai')
            l2=len(th)
            row_counter2=0
            while(l2>=h2):
                l2-=h2
                for i in range(h2):
                    rgb_list2.append(self.rgb_of_pixel(img_file2,i,row_counter2)) 
                row_counter2+=1
            if(l2>=0 and l2<=h2):
                for i in range(l2):
                    rgb_list2.append(self.rgb_of_pixel(img_file2,i,row_counter2))
            print(row_counter2)
        #print(rgb_list2)
        return rgb_list1,rgb_list2 
        
     
    
        
    
    def put_back(self,img2,rgb_list2,cphr_txt,a,th,url):
        img_obj=cv2.imread(img2,cv2.IMREAD_COLOR)
        w,h,c=img_obj.shape
        imp=Image.open(img2)

        if(len(th)<=h):
            for i in range(0,len(th)+24):
                imp.putpixel((i,0),tuple(rgb_list2[i]))
        else:
            l=len(th)
            row_counter=0
            while(l>=h):
                l-=h
                for i in range(h):
                    imp.putpixel((i,row_counter),tuple(rgb_list2[i])) 
                row_counter+=1
            if(l>=0 and l<=h):
                for i in range(l):
                    imp.putpixel((i,row_counter),tuple(rgb_list2[i]))
        
        head_tail=os.path.split(url)
        imp.save(head_tail[0].replace("\\","/")+'/frames/frame'+str(a)+'.png')



