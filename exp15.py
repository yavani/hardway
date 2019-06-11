from sys import argv
script , filename = argv
txt = open(filename) # open the file and store it in txt variable it just opens the file

print(f"Here's your file {filename}") # print the msg
print(txt.read()) # it will read the file as well as print function print the content of file

print("Type the file name again") # Type file name again
file_again= input("> ") # it just take > prompt as input and store it in file_again

text_again=open(file_again) # it opens the file_again
print(text_again.read()) # it read and print file
# text_again.close() # to close the file
