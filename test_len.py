file = open("C:/Users/vinee/OneDrive/Documents/Video Steganography/video_steganography/test_data.txt", "r")

#read the content of file
data = file.read()

#get the length of the data
number_of_characters = len(data)
print(number_of_characters)
