from sys import exit

def gold_room():
	print("This room is full of gold how much do you take?")

	choice = input("> ")
	if "0" in choice or "1" in choice:
		how_much= int(choice)
	
	else:
		dead("Man learn to type a number")

	if how_much < 50:
		print("nice your are not greedy, you win!")
		exit(0)


def bear_room():
	print("There is abear here")
	print("the bear has a bunch of honey.")
	print("The fat bear is in front of another bear")
	print
	bear_moved= True
	while True:
		choice= input("> ")
		
		if choice=="take honey":
			dead("The bear looks at you then slap on your face off")
		elif choice=="taunt bear" and not bear_moved:
			print("The bear has moved from door")
			print("you can go through it now")
			bear_moved=True
		elif choice=="taunt bear" and bear_moved:
			dead("the bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("i Got no idea what that means.")

def cthulhu_room():
	print("here you see the great evil cthulhu")
	print("he eat whatever stares at you and you go insane.")
	print("do you flee for your life or eat your head?")
	
	choice=input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was tasty!")
	else:
		cthulhu_room()
def dead(why):
	print(why, "Good Job!")
	exit(0)

def start():
	print("you are in the dark room")
	print("there is door to your right and left")
	print("which one do you take")

	choice = input("> ")
	
	if choice =="left":
		bear_room()
	elif choice =="right":
		cthulhu_room()
	else:
		dead("you stubble around the room unil you starve. ")

start()
