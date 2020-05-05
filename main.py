
from encrypt import enc_class
from encode import encode_data
from rd_ext import exc_frame
from PIL import Image
from decode import decd_data
import tkinter as tk
import os
from functools import partial
from conv_to_vd import cnvt_vdo

def encode(e1,e2,e3):
    hide_message=(e1.get())
    url=(e2.get())
    password=(e3.get())
    

    enpt_obj=enc_class()
    enpt_obj.generate_key(password)

    cphr_text=enpt_obj.encrypt(hide_message)
    print("the ciphertext is: "+str(cphr_text))
  

    encd_obj=encode_data()
    th=encd_obj.conv_ascii(cphr_text)
    #print(th)


      #calling the function to extract video
    exc_obj=exc_frame()
    count=exc_obj.ext_frames(url)



    #calling the main encoding function#
    print('----------------------------encoding starts------------------------------------')                 
    len_counter=0 
    for i in range(count-1):
      img_file1,img_file2=encd_obj.extract_image(i,i+1,url)
      rgb_list1,rgb_list2=encd_obj.get_pixel(img_file1,img_file2,cphr_text,th)
      len_counter=encd_obj.encode(rgb_list1,rgb_list2,len_counter,th)
      if(len_counter==-1):
        encd_obj.put_back(img_file2,rgb_list2,cphr_text,i+1,th,url)
        print("ho gaya encoding")
        break

    
        
    #saving the video
    parent_directory=os.path.split(url)
    pathIn= parent_directory[0]
    pathOut='video.avi'
    fps=25
    cn_obj=cnvt_vdo()
    enc_loc=cn_obj.convert_frames_to_video(pathIn,pathOut,fps)

    loc.set("the encoded video is stored at location"+str(enc_loc))
    
    
    
    
    
    
    
def decode(e4,e5):
  return


  



  

  
#----------------------calling the main function---------------------#
if __name__ == "__main__":
    master = tk.Tk()
    master.title('Video Steganography')
    master.geometry("1000x500")
    tk.Label(master,text="For encryption").place(x = 30,y = 10)
    tk.Label(master,text="Enter your secret text").place(x = 30,y = 50)
    tk.Label(master,text="Enter the location of the video stored").place(x = 30,y = 100)
    tk.Label(master,text="Enter the password").place(x = 30,y = 150)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    #grid(row=0, column=1)

    
    e1.place(x = 250,y = 50)
    e2.place(x = 250,y = 100)
    e3.place(x = 250,y = 150)

    loc=tk.StringVar()

    video_loc =tk.Label(master,text="",textvariable=loc).place(x = 200,y = 250)
    
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


    decode=partial(decode)
    tk.Button(master, text='Decode').place(x = 750,y = 190)

    master.mainloop()
    
    
  

    