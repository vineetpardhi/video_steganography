import binascii

from PIL import Image
class decd_data(object):


    def decode(self,rgb_list1,rgb_list2):
        message = ''
        flag = 1
        # print(rgb_list1)
        # print(rgb_list2)
        if len(rgb_list1)==len(rgb_list2):  #if the length of both the list is same then only proceed
            counter=-1
            for i in range(len(rgb_list1)):
                if flag == 0:
                    break
                for j in range(0,3):
                    d1 = rgb_list1[i][j]%10
                    d2 = rgb_list2[i][j]%10
                    mod=abs(d1-d2)%2
                    counter+=1
                    if(mod == 0 and not((i+1)%3==0 and j==2 and i!=0)):
                    #print((i+1)%3==0 and j==2 and i!=0)
                        message = message + '0'
                    elif(mod == 1 and not((i+1)%3==0 and j==2 and i!=0)):
                    #print((i+1)%3==0 and j==2 and i!=0)
                        message = message + '1'
                    elif(mod == 0 and ((i+1)%3==0 and j==2 and i!=0)):
                    #print((i+1)%3==0 and j==2 and i!=0)
                        continue
                    elif(mod == 1 and ((i+1)%3==0 and j==2 and i!=0)):
                    #print((i+1)%3==0 and j==2 and i!=0)
                        flag = 0
                    break

        return message


    def conv_str(self,msg):
        message=decode(test_list1,test_list2)

        mess=[message[i:i+8] for i in range(0, len(message), 8)]
        m=''
        for i in range(len(mess)):
            m+=chr(int(mess[i],2))
        
        recvd_text = m
        recvd_text = recvd_text[:-1]
        
        return recvd_text
  
    def getnewp(self,img_path,cphr_text):
        img_obj=cv2.imread(img_path,cv2.IMREAD_COLOR)
        w,h,c=img_obj.shape
        new_im =Image.open(img_path)
        nl=[]

        if(len(th)<=h):
            for i in range(0,len(th)+24):
                r,g,b=new_im.getpixel((i, 0))
                vl=[r,g,b]
                nl.append(vl)
        else:
            for i in range(h):
                for j in range(w):
                    r,g,b=new_im.getpixel((i, j))
                    vl=[r,g,b]
                    nl.append(vl)
                    
        return nl
        