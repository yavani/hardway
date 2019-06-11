from sys import argv
script, user_name, last_name  = argv
prompt = '>>'
print(f"Hello Mr.{user_name} {last_name} ,I'm the {script} script")
print("I'd like to ask you few questions")
print(f"do you like me {user_name}?")
likes=input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have ?")
computer = input(prompt)

print(f"what is your occupation {user_name}")
occupation= input(prompt)

print(f""" Alright so you said {likes} about me. \n you lives in {lives}. Not sure where that is. \n And you have a {computer} computer.your are a {occupation} .\n  Nice Thank you.Bye Bye ;)- """)

