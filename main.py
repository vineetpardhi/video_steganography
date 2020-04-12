
from encrypt import enc_class
from encode import encode_data
from rd_ext import exc_frame
from PIL import Image
from decode import decd_data


 


 #----------------------------main function-------------------------------#
def main():  
  #calling the encrypt function
  password=input("Enter a password: ")

  enpt_obj=enc_class()
  enpt_obj.generate_key(password)

  hide_message=input("Enter the message you want to hide: ")
  cphr_text=enpt_obj.encrypt(hide_message)
  print("the ciphertext is: "+str(cphr_text))


  #calling the encoding functions

  encd_obj=encode_data()
  th=encd_obj.conv_ascii(cphr_text)
  #print(th)

  #calling the function to extract video
  exc_obj=exc_frame()

  url=input("Enter the url for the video: ")
  count=exc_obj.ext_frames(url)



  #calling the main encoding function#
  print('----------------------------encoding starts------------------------------------')                 
  len_counter=0 
  for i in range(count-1):
    img_file1,img_file2=encd_obj.extract_image(i,i+1)
    rgb_list1,rgb_list2=encd_obj.get_pixel(img_file1,img_file2,cphr_text)
    len_counter=encd_obj.encode(rgb_list1,rgb_list2,len_counter,th)
    if(len_counter==-1):
      encd_obj.put_back(img_file2,rgb_list2,cphr_text)
      break
    


  
  # #-----------------decoding part--------------------------#
  new_im1="C:/Users/vinee/OneDrive/Documents/Video Steganography/video_steganography/frames/frame0.png"
  new_im2 ="C:/Users/vinee/OneDrive/Documents/Video Steganography/video_steganography/frames/framenew.png"



  
  
  
  
  decd_obj=decd_data()

  newlist1=decd_obj.getpixel(new_im1,cphr_text)
  newlist2=decd_obj.getpixel(new_im2,cphr_text)
  msg=decd_obj.decode(newlist1,newlist2)
  #print(msg)
  dcphr_text=decd_obj.conv_str(msg)
  print(dcphr_text)

    

  
#----------------------calling the main function---------------------#
if __name__ == "__main__":
  main()

    