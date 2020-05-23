file_t = open("C:/Users/vinee/OneDrive/Desktop/mp2_project/video_steganography/test_data.txt", "r")

#read the content of file
data=str()
for x in file_t:
  data+=x
#get the length of the data
number_of_characters = len(data)
print(number_of_characters)
