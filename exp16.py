from sys import argv
script, filename = argv
print(f"we are going to erase {filename}")
print(f"if you dont want that , hit CTRL-C(^C).")
print("if you do want that , hit RETURN.")
input("?")

print("opening the file .........")
target= open(filename, 'w')

print("Truncating the file . GOODBYE!")
target.truncate()

print("I am going to ask you to write three lines.")

line1=input("Line1 :-")
line2=input("Line2 :-")
line3=input("Line3 :-")

print("I am going to write this to file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it once writing is done")
target.close()

print("\n")
print("here below are  the content of my file ") 
txt= open(filename)
print(txt.read())


