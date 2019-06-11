def area(l,b):
	print("function to calculate area")
	area = l*b
	return area
	
l = input("enter the length")
print(f"length  is = {l}")
b= input("enter the breadth")
print(f"breadth is ={b}")

l= float(l)
b=float(b)
area_of_rectangle = area(l,b)
print(f"area = {area_of_rectangle}")
