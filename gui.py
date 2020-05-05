#GUI is ready with the password
#This code will work in your jupyter notebooks offline @vineet and @kewal
#C:\Users\tejas\Downloads\SampleVideo_1280x720_1mb.mp4
import tkinter as tk
from functools import partial

class gui_class(object):

  
  

 


  
  def __init__(self):
    
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

    encode=partial(self.encode,e1,e2,e3)
    #.grid(row=3, column=0, sticky=tk.W, pady=4)
    #tk.Button(master, text='Quit', command=master.quit).place(x = 30,y = 170)
    tk.Button(master, text='Encode', command=encode).place(x = 250,y = 170)
    ##---------------------------------------------------------------------------------------
    # tk.Label(master,text="For decryption").place(x = 530,y = 10)
    # tk.Label(master,text="Enter the location of the video stored").place(x = 530,y = 50)
    # tk.Label(master,text="Enter the password").place(x = 530,y = 100)

    # e4 = tk.Entry(master)
    # e5 = tk.Entry(master)
    # e4.place(x = 750,y = 50)
    # e5.place(x = 750,y = 100)
    # tk.Button(master, text='Decrypt', command=decrypt).place(x = 630,y = 170)

    master.mainloop()
    