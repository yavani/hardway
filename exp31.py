print("""you entered a dark room with two doors 
  do you go through door #1 or door #2 ?""")
door=input(">")

if door=="1":
	print("there is gian bear here eating a cheese care.")
	print("ehat do you do?")
	print("1: take the cake")
	print("2: Scream at bear")
	
	bear= input(">")
	if bear=="1":
		print("the bear eat's your face off. Good Job!")
	elif bear=="2":
		print("the bear eats your legs off>Good job")
	else:
		print(f"well doing {bear} is probably better")
		print("bear runs away")

elif door =="2":
	print("you stare ito the endleass abyss at cthulhu's retina.")
	print("1. blue berry.")
	print("2: yellw jackets cloths pin")
	print("3: understanding revolvers yelling melodies.")
	
	insanity = input("> ")
	if insanity =="1" or insanity =="2":
		print("your body servives powerd by a mind of jello.")
		print("good job")
	else:
		print("the insanity rots your eyes into a pool of muck.")
		print("good job")
else:
	print("you stubble around and fall on a knife and die. good Job!")



