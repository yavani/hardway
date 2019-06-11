def add(a,b):
	print(f"adding {a}+{b}")
	return a+b

def substract(a,b):
	print(f"substracting {a}-{b}")
	return a-b

def multiply(a,b):
	print(f"multiply {a}*{b}")
	return a*b

def divide(a,b):
	print(f"deviding {a}/{b}")
	return a/b

print("lets do some maths by function")
a= input("enter the value of a")
b= input("enter the value of b")

a= float(a)
b=float(b)

age= add(a,b)
height=substract(a,b)
weight=multiply(a,b)
iq= divide(a,b)

print(f"age = {age}, height={height}, weight= {weight},iq= {iq}")

# here is puzzle for extra credit
print("here is puzzle")
what = add(age,substract(height,multiply(weight,divide(iq,2))))
print("that becomes", what, "can you do it by hand")


