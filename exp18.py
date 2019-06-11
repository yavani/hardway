def print_two(*args):
	arg1, arg2 =args
	print(f"arg1: {arg1} , arg2: {arg2}")

def print_two_again(arg1, arg2):
	print(f"arg1: {arg1} , arg2: {arg2}")


def print_one(arg1):
	print(f"i have only one argument : {arg1}")

def print_none():
	print("i dont have any argument")

print_two("Ashwini", "Madhava")
print_two_again("Malhar", "madhava")
print_one("Python")
print_none()


