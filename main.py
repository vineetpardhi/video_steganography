
from encrypt import enc_class
from encode import encode_data
from rd_ext import exc_frame
from PIL import Image
from decode import decd_data
from decrypt import decpt_data
import tkinter as tk
from tkinter import messagebox as mb
import os
from functools import partial
from conv_to_vd import cnvt_vdo
import re
from PIL import ImageChops
import math, operator
from math import log10, sqrt




def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*((idx%256)**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms







def encode(e1,e2,e3):
    message_loc=(e1.get())
    url=(e2.get())
    password=(e3.get())





    while True:   
      if (len(password)<8): 
          flag = -1
          break
      elif not re.search("[a-z]", password): 
          flag = -1
          break
      elif not re.search("[A-Z]", password): 
          flag = -1
          break
      elif not re.search("[0-9]", password): 
          flag = -1
          break
      elif not re.search("[_@$]", password): 
          flag = -1
          break
      elif re.search("\s", password): 
          flag = -1
          break
      else: 
          flag = 0
          break
  
    if flag ==-1:
      mb.showwarning("warning","pass word is not valid")
      return 
        
    

    enpt_obj=enc_class()
    enpt_obj.generate_key(password)


    f = open(message_loc, "r")
    hide_message=f.read()
    f.close()

    cphr_text=enpt_obj.encrypt(hide_message)
    # print("the ciphertext is: "+str(cphr_text))
  

    encd_obj=encode_data()
    #print(th)


      #calling the function to extract video
    exc_obj=exc_frame()
    count=exc_obj.ext_frames(url)

    directory="frames"
    head_tail=os.path.split(url)
    mod_url = os.path.join(head_tail[0],directory)

    #calling the main encoding function#
    print('----------------------------encoding starts------------------------------------')                 
    enc_length=0
    frame_count=1
    for i in range(count):
      if(len(cphr_text)>=enc_length):
        img1=mod_url+"\\frame"+str(i)+".png"
        img2=mod_url+"\\frame"+str(i+1)+".png"
        enc_length=encd_obj.encode(img1,img2,cphr_text,enc_length)
        frame_count+=1
        print("storing in the frame"+str(i+1))
      else:
        break
    


      

    
        
    #saving the video
    parent_directory=os.path.split(url)
    pathIn= parent_directory[0]
    pathOut='video.avi'
    fps=0.5
    cn_obj=cnvt_vdo()
    enc_loc=cn_obj.convert_frames_to_video(pathIn,pathOut,fps)

    mb.showinfo('the encoded video is located at',enc_loc)


    #----------------PSNR results-----------------#
    # original = cv2.imread('/content/frame1_original.png') 
    # compressed = cv2.imread('/content/frame1_encoded.png', 1) 
    # value = PSNR(original, compressed) 
    # print(f"PSNR value is {value} dB")
    
    #---------------RMSE results----------------#
    # img1=Image.open('/content/frame1_original.png')
    # img2=Image.open('/content/frame1_encoded.png')
    # rms=rmsdiff(img1,img2)
    # print(f"the RMSE value is{rms}")
    
    
    
    
    
    
def decode(e4,e5):
  d_url=(e4.get())
  d_passwd=(e5.get())


  #-------extracting the frames for decoding---------#

  

  # d_extf=exc_frame()

  # dcount=d_extf.ext_frames(d_url)


  # #-----------decoding function-------------#
  
  dcd_obj=decd_data()
  
  directory="frames"
  head_tail=os.path.split(d_url)
  mod_url = os.path.join(head_tail[0],directory)


  data=str()
  
  count=5
  flag=0
  print('----------------------------decoding starts------------------------------------') 
  for i in range(count):
    if(flag==0):
      img1=mod_url+"\\frame"+str(i)+".png"
      img2=mod_url+"\\frame"+str(i+1)+".png"
      data,flag=dcd_obj.decode(img1,img2,flag)
      # dt_list.append(c_data)
      print('decoding from frame'+str(i+1))
    else:
      print("finished decoding")
      break
      
  
  # data=''.join(dt_list)
  #------decrypting the cphr text to get plain text----#
  decrypt_obj=decpt_data()
  dkey=decrypt_obj.generate_key(d_passwd)
  hid_messg=decrypt_obj.decrypt(str.encode(data),dkey)
  
   
  wr_url=head_tail[0]
  wfile=open(wr_url+"\\hidden_message.txt","w")
  wfile.write(str(bytes.decode(hid_messg)))
  wfile.close()
  mb.showinfo('the video is stored at location:',wr_url+'\\hidden_message.txt')
  



  
  
  

  

    
    
  

  



  

  
#----------------------calling the main function---------------------#
if __name__ == "__main__":
    master = tk.Tk()
    master.title('Video Steganography')
    master.geometry("1000x500")
    tk.Label(master,text="For encryption").place(x = 30,y = 10)
    tk.Label(master,text="Enter the location for text file").place(x = 30,y = 50)
    tk.Label(master,text="Enter the location of the video stored").place(x = 30,y = 100)
    tk.Label(master,text="Enter the password").place(x = 30,y = 150)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    #grid(row=0, column=1)

    
    e1.place(x = 250,y = 50)
    e2.place(x = 250,y = 100)
    e3.place(x = 250,y = 150)

    
    
    encode=partial(encode,e1,e2,e3)
    #.grid(row=3, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Quit', command=master.quit).place(x = 470,y = 400)
    tk.Button(master, text='Encode', command=encode).place(x = 250,y = 190)


    
    
    #---------------------------------------------------------------------------------------
    tk.Label(master,text="For decryption").place(x = 530,y = 10)
    tk.Label(master,text="Enter the location of the video stored").place(x = 530,y = 50)
    tk.Label(master,text="Enter the password").place(x = 530,y = 100)

    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e4.place(x = 750,y = 50)
    e5.place(x = 750,y = 100)


    decode=partial(decode,e4,e5)
    tk.Button(master, text='Decode',command=decode).place(x = 750,y = 190)

    master.mainloop()
    
    
  

    