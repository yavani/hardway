#class thing(object):
#	def test(message):
#		print(message)

#a= thing()
#a.test("helloe")

ten_things="Apples oranges crows telephone light sugar"

print("wait there are not 10 things in that list . lets fix that.")

stuff = ten_things.split(' ')
more_stuff=["day", "Night","song","Frisbee","corn","banana","girl","Boy"]

while len(stuff)!=10:
	next_one=more_stuff.pop()
	print("adding", next_one)
	stuff.append(next_one)
	print(f"there are {len(stuff)} item now.")
print("there we go : ",stuff)

print("lets do somethings with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
