

# done some changes like copy one file to another and print also

from sys import argv
from os.path import exists

script, from_file, to_file= argv
print(f"coping {from_file} to {to_file}")

# we culd do this two on one line how?
in_file = open(from_file)
indata= in_file.read()
 
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists ?{exists(to_file)}")
print("ready, hit to Return to  continue or CTRL-C to abort .")

input()

out_file= open(to_file, 'w')
out_file.write(indata)
out_file=open(to_file)
print(out_file.read())

print("All Right , All done")

#new_file = open(to_file)
#print(new_file.read())


out_file.close()
in_file.close()
 
