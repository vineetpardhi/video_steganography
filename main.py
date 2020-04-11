
from encrypt import enc_class
from encode import encode_data
from rd_ext import exc_frame




 #----------------------------main function-------------------------------#
def main():  
  #calling the encrypt function
  password=input("Enter a password: ")

  enpt_obj=enc_class()
  enpt_obj.generate_key(password)

  hide_message=input("Enter the message you want to hide: ")
  cphr_text=enpt_obj.encrypt(hide_message)
  print(cphr_text)


  #calling the encoding functions

  encd_obj=encode_data()
  th=encd_obj.conv_ascii()
  # print(th)

  #calling the function to extract video
  exc_obj=exc_frame()

  url=input("Enter the url for the video: ")
  count=exc_obj.ext_frames(url)



  #calling the main encoding function#
                     
  len_counter=0 
  for i in range(count-1):
    img_file1,img_file2=encd_obj.extract_image(i,i+1)
    rgb_list1,rgb_list2=encd_obj.get_pixel(img_file1,img_file2,cphr_text)
    len_counter=encd_obj.encode(rgb_list1,rgb_list2,len_counter,th)
    if(len_counter>=len(th)-1):
      encd_obj.put_back(img_file2,rgb_list2)
      break


  
  




if __name__ == "__main__":
  main()

    