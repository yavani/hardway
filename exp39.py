things = ['a', 'b' ,'c','d']
print(things[1])
print(things[3])

print(things)

stuff= {"name": "Ashwini",'age':30,'height' : 6*12+2}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city']= "Bangalore"
print(stuff['city'])
print(stuff)


stuff[1]='wow'
stuff[2]='netyo'

print(stuff[1])
print(stuff[2])


print(stuff)

del stuff[1]
del stuff['city']

print(stuff)


#create mapping of state to abbriviations
states={'Oregon':'or',
	'florida':'fl',
	'california':'ca',
	'new york':'NY',
	'michigan':'MI'
	}

# Create a basic set of states and some cities in them

cities={
	'ca':'San Francisco',
	'MI':'Detroit',
	'fl':'jacksonville'
	}

#add some more cities

cities['NY']='New York'
cities['or']='Portland'

#print out some cities

print('--'*10)
print("Ny state has", cities['NY'])
print("MI state has",cities['MI'])

print("*"*10)

print ("every state abbrivations")

for state, abbrv in list(states.items()):
	print(f"{state} is abbrivated as {abbrv}")

print("*"*10)

print("Every city in a state")
for abbrv,city in list(cities.items()):
	print(f"{abbrv} has city {city}")


print("*"*50)

print("noe print both at the same time")

for state, abbrv in list(states.items()):
	print(f"{state} is abbrivated as {abbrv}")
	print(f"and has city {cities[abbrv]}")

