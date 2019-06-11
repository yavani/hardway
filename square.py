

def square(n):
	for i in range(1,n):
		sq= i**2
		print(f"square of {i} is {sq}")

n= input("any value")
n= int(n)
square(n)
