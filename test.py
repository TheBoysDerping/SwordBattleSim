import pickle, random, sys
if len(sys.argv) - 1:
    random.seed(int(sys.argv[1]))



class test():
	def __init__(self):
		self.swordtype=("Gladiator", "Katana", "Scimitar", "Rapier", "LongSword", "Broadsword", "Cutlass", "ShortSword")
		self.chosensword=random.choice(self.swordtype)
		self.swordmodifier=("Speed", "Power")
		self.chosenmodifier=random.choice(self.swordmodifier)
		self.swordmagic=("Fire", "Ice", "Lightning", "Wind", "Dark", "Toxic")
		self.chosenmagic=random.choice(self.swordmagic)
		self.magicpower=100
		self.swordlevel=1
		self.swordxp=0
		self.swordxpneeded=100
		self.playerhp=100
		self.playerlevel=1
		self.playerxp=0
		self.playerxpneeded=100
		self.enemy=("Goblin", "Gladiator", "Vampire", "Zombie", "Clone of Yourself")
		self.chosenenemy=random.choice(self.enemy)
		self.enemyhp=50
		statsdictionary={"chosensword": self.chosensword, "chosenmodifier": self.chosenmodifier, "chosenmagic": self.chosenmagic, "magicpower": self.magicpower, "swordlevel": self.swordlevel, "swordxp": self.swordxp, "swordxpneeded": self.swordxpneeded, "playerhp": self.playerhp, "playerlevel": self.playerlevel, "playerxp": self.playerxp, "playerxpneeded": self.playerxpneeded, "chosenenemy": self.chosenenemy, }
		pickle.dump(statsdictionary, open( "savestatstest.p", "wb" ) )
		print(statsdictionary)