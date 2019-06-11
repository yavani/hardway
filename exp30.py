people=50
cars=40
trucks=15

if cars > people and  cars > trucks:
	print("we should take the cars.")
elif cars<people:
	print("we should not take the cars")
else:
	print("we can't decide")

if trucks>cars:
	print("thats too many trucks.")
elif trucks<cars:
	print("may be we could take trucks.")
else:
	print("we still cant decide")

if people>trucks:
	print("al,right, lets just take the trucks.")
else:
	print("Fine, lets stay home then.")

