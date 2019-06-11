from sys import exit
from random import randint
from textwrap import dedent

class scene(object):
	def enter(self):
		print("This scence is not yet confugered")
		print("subclass it and implement enter().")
		exit(1)


class engine(object):

	def __init__(self,scene_map):
		self.scene_map=scene_map

	def play(self):
		current_scence=self.scene_map.opening_scene()
		last_scene=self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name=current_scene.enter()
			current_scene=self.scene_map.next_scene(next_scene_name)

#be sure to print out the last scene

		current_scene.enter()

class death(scene):

	quips= [" you died. you kine of suck at this .","your mom would be proud...if she where smarte.",
			"such a luiser.",
			"you're worse than your dad's jokes."
		]
	
	def enter(self):
		print(death.quips[radint(0,len(self.quips)-1)])
		exit(1)

class centralcorridor(scene):

	def enter(self):

		print(dedent(""" you are at cenral coridor scene
				its realy awesome scene"""))

		action = input("> ")

		if action == "shoot!":

			print(dedent(""" you are shooting his new costume which makes him fly repeatedly
					 until he dies then he eats you""))
			return 'death'

		elif action == "dodge!":
			print(dedent("""gothon slamp on your head 
					 and eats you ooooo"""))
		        return 'death'

		elif action is == "tell ajoke":
			print(dedent("""you are jumping.
				you are running"""))
		
			return 'laser_weapon_army':
		else:
			print("dose nor copute")
			return 'central_corridor'




