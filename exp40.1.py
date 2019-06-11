
class ashwini:

    def __init__(self,lyrics):
        self.lyrics= lyrics

    def sing_for_me(self):
        for line in self.lyrics:
            print(line)

aboutme = ashwini(["i ma ashwini","I love python"])

aboutme.sing_for_me()

