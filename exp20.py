from sys import argv
script , input_file= argv

def print_all(f):
	print(f.read())
def rewind(f):
	f.seek(0)
def print_a_line(line_count,f):
	print(line_count,f.readline(),)

current_file= open(input_file)
print("first lets print the whole file")

print_all(current_file)

print("now lets rewind kind of tape")
rewind(current_file)

print("now lets print a line")
current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)
