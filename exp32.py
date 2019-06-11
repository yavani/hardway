the_count = [1,2,3,4,5,6]
fruits=["apple","orange","banana","watermelon"]
change=[1,"pennies",2,"dimes",3,"Quarters"]
print(the_count)
print(fruits)

for numbers in the_count:
	print(f"this is count : {numbers}")

for fruits in fruits:
	print(f"A fruit type is : {fruits}")

for i in change:
	print(f"i got : {i}")

elements=[ ]

for i in range(0,6):
	print(f"Adding {i} to the list")
	elements.append(i)

for i in elements:
	print(f" elemnts of list was {i}")




