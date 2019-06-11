# First class

class song(object):

	def __init__(self,lyrics):
		self.lyrics=lyrics
	
	def sing_me_song(self):
		for line in self.lyrics:
			print(line)

happybday = song(["happy birthday to you ", "may god bless you ","So' I will stop right here"])

happybday.sing_me_song()



