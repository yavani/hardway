class parent:
	def override(self):
		print("parent override()")
	def implicit(self):
		print("parent implicit()")

	def altered(self):
		print("parent altered()")

class child(parent):
	def override(self):
		print("child override()")
	def altered(self):
		print("child before parent altered")
		super(child,self).altered()
		print("child after parent alterd")

dad = parent()
son= child()

dad.override()
dad.implicit()
dad.altered()

son.override()
son.implicit()
son.altered()




