i=0
numbers =[ ]

while i<6:
	print(f" at the top i is {i}")
	numbers.append(i)

	i=i+2
	print("nembers now",numbers)
	
	
	print(f" at the bottom i is now {i}")

print("the numbers ")
for i in numbers:
	print(i)

def function(i):
	if i<6 :
		print(f"value of i is {i}")
		a=i*2
		print(f"the value is {a}")

a=input("enter i value")
a=int(a)

function(a)

