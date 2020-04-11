import binascii


class decd_data(object):


    def decode(self,rgb_list1,rgb_list2):
        message = ''
        flag = 1
        print(rgb_list1)
        print(rgb_list2)
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
  