class animal(object):
	pass

class dog(animal):
	def __init__(self,name):
		self.name=name
		print(name)

class cat(animal):
	def __init__(self,name):
		self.name=name

class person(object):
	def __init__(self,name):
		self.name=name
		self.pet=None

class employee(person):
	def __init__(self,name,salary):
		super(employee,self).__init__(name)
		self.salary=salary

class fish(object):
	pass

class salmon(fish):
	pass
class halibut(fish):
	pass


rover= dog("Rover")

satan=cat("satan")

mary=person("mary")

mary.pet=satan

frank=employee("Frank",12000)

frank.pet=rover

flipper=fish()

crouse=salmon()
harry=halibut()



		

