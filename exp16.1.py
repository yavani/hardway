from sys import argv
script, filename= argv
print("i am reading the file test .txt  which i have created just now")
text= open(filename)
print(text.read())

