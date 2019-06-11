print("Let's practice everything .")
print("you\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs. ")

poem=""" 
\t the lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t where there is none.
"""

print("-------------------------")
print(poem)
print("------------------------")

five = 10-2+3-6
print(f"this should be five: {five}")


def secrete_formula(started):
	jelly_beans= started*500
	jars= jelly_beans/1000
	crates=jars/100
	return jelly_beans, jars,crates


start_point=input("enter start point")
start_point= float(start_point)
beans,jars,crates= secrete_formula(start_point)

#remember that this is another way to format string
print("with a starting point of :{}".format(start_point))

#it is just like f" " string
print(f"we'd have {beans} beans, {jars} jars,{crates} crates.")

start_point= start_point/10

print("we can also do that this way :")
formula= secrete_formula(start_point)
#this is an easy way to apply a list to a format string
print(f"we'd have {beans} beans, {jars} jars,{crates} crates.".format(*formula))
 # (*formula here means you can pass any number of arguments here 3 jellybeans,jars,crates as function returns those arg"

