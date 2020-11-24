##DONT DELETE THIS
import time, sys, random
if len(sys.argv) - 1:
	random.seed(int(sys.argv[1]))
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def dll(n=1):
	for _ in range(n):
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)


def ws(t=1):
	for _ in range(t):
		time.sleep(1)


#########################################################


class Simulator():
	def __init__(self):
		self.swordtype = ("Gladiator", "Katana", "Scimitar", "Rapier",
		                  "LongSword", "Broadsword", "Cutlass", "ShortSword")
		self.chosensword = random.choice(self.swordtype)
		self.swordmodifier = ("Speed", "Power")
		self.chosenmodifier = random.choice(self.swordmodifier)
		self.swordmagic = ("Fire", "Ice", "Lightning", "Wind", "Dark", "Toxic")
		self.chosenmagic = random.choice(self.swordmagic)
		self.magicpower = 100
		self.swordlevel = 1
		self.swordxp = 0
		self.swordxpneeded = 100
		self.playerhp = 100
		self.playerlevel = 1
		self.playerxp = 0
		self.playerxpneeded = 100
		self.enemy = ("Goblin", "Gladiator", "Vampire", "Zombie",
		              "Clone of Yourself")
		self.chosenenemy = random.choice(self.enemy)
		self.enemyhp = 50

	def showswordstats(self):
		print("Here are your swords stats")
		swordstats = "\t\t\t\t____________________\n"
		swordstats += "\t\t\t\t|Player Sword Stats|\n"
		swordstats += f"Your Sword is: {self.chosensword}\n"
		swordstats += f"Your Sword Modifier is: {self.chosenmodifier}\n"
		swordstats += f"Your Sword Magic is: {self.chosenmagic}\n"
		swordstats += f"Your Sword Skill Level is: {self.swordlevel}\n"
		swordstats += f"Your Sword XP amount is: {self.swordxp}/{self.swordxpneeded}"
		print(swordstats)
		ws(t=4)

	def levelup(self):
		if self.playerxp >= self.playerxpneeded and self.playerlevel != 5:
			print("Your Player Has Leveled up!")
			self.playerlevel += 1
			self.playerxp = 0
			self.playerxpneeded += random.randint(20, 30)
			if self.playerlevel == 2:
				self.playerhp += 20
			elif self.playerlevel == 3:
				self.playerhp += 30
			elif self.playerlevel == 4:
				self.playerhp += 50
			elif self.playerlevel == 5:
				self.playerhp += 100

		if self.swordxp >= self.swordxpneeded and self.swordlevel != 5:
			print("Your Sword Skills Have Leveled up!")
			self.swordlevel += 1
			self.swordxp = 0
			self.swordxpneeded += random.randint(20, 30)

	def battle(self):
		print("You chose to battle")
		print(
		    f"A {self.chosenenemy} Walks into the stadium. You ready your sword"
		)
		while self.enemyhp > 0:
			self.attackorability = input(
			    "Type 1 to attack or 2 to activate your magic ability for 50 Magic Power Points\n"
			)
			if self.attackorability == "1":
				self.enemyhitordodged = random.randint(1, 3)
				if self.enemyhitordodged == 1 or self.enemyhitordodged == 3:
					self.damage = random.randint(10, 20)
					if self.swordlevel == 2:
						self.damage += 10
					elif self.swordlevel == 3:
						self.damage += 20
					elif self.swordlevel == 4:
						self.damage += 30
					elif self.swordlevel == 5:
						self.damage += 40
					print(
					    f"You hit! You did {self.damage} to the {self.chosenenemy}"
					)
					self.enemyhp -= self.damage
				elif self.enemyhitordodged == 2:
					print(f"The {self.chosenenemy} Dodged the attack!")
				self.playerhitordodged = random.randint(1, 3)
				if self.playerhitordodged == 1 or self.playerhitordodged == 3:
					print("You Dodged! You lost 0 hp")
				elif self.playerhitordodged == 2:
					self.damagetoplayer = random.randint(5, 10)
					self.playerhp -= self.damagetoplayer
					print(
					    f"The {self.chosenenemy} did {self.damagetoplayer} to you!"
					)
			elif self.attackorability == "2":
				if self.magicpower == 0:
					print("You Do Not Have Enough MPP!")
				else:
					print(
					    "You Used up 50 MPP to do 30 damage to the enemy and stunned them so they could not attack"
					)
					self.enemyhp -= 30
					self.magicpower -= 50
					if self.magicpower < 0:
						self.magicpower = 0
					print(f"You Have {self.magicpower} MPP left")
			ws(t=2)
			dll(n=3)

		if self.enemyhp < 0:
			if self.playerlevel == 5 and self.swordlevel == 5:
				print(
				    f"You Killed the {self.chosenenemy}! You are max level so you gained 0 XP"
				)
			if self.playerlevel != 5 and self.swordlevel != 5:
				self.playerxpgained = random.randint(37, 50)
				self.swordxpgained = random.randint(60, 70)
				print(
				    f"You Killed the {self.chosenenemy}! You also gained some XP for your player and sword!\n Sword XP gained: {self.swordxpgained}\n Player XP gained: {self.playerxpgained}"
				)
				self.playerxp += self.playerxpgained
				self.swordxp += self.swordxpgained
			if self.playerlevel != 5 and self.swordlevel == 5:
				self.playerxpgained = random.randint(37, 50)
				print(
				    f"You Killed the {self.chosenenemy}! And Gained {self.playerxpgained} player XP!"
				)
				self.playerxp += self.playerxpgained
			if self.swordlevel != 5 and self.playerlevel == 5:
				self.swordxpgained = random.randint(60, 70)
				print(
				    f"You Killed the {self.chosenenemy}! And Gained {self.swordxpgained} sword skill XP!"
				)
				self.swordxp += self.swordxpgained
			ws(t=3)

		if self.playerhp < 0:
			print("You have Died. Please Try again")
			exit()

	def showplayerstats(self):
		print("Here are your player stats")
		playerstats = "\t\t\t\t______________\n"
		playerstats += "\t\t\t\t|Player stats|\n"
		playerstats += f"Player HP left is: {self.playerhp}\n"
		playerstats += f"Player MPP left is: {self.magicpower}\n"
		playerstats += f"Player Level is: {self.playerlevel}\n"
		playerstats += f"Player XP amount is : {self.playerxp}/{self.playerxpneeded}"
		print(playerstats)
		ws(t=4)

	def heal(self):
		if self.playerhp < 100:
			print("You healed your player 40 hp")
			self.playerhp += 40
			if self.playerhp >= 100:
				self.playerhp = 100
		elif self.playerhp >= 100:
			print("You Are at 100 HP. You can't Heal anymore!")

	def magicpowerup(self):
		if self.magicpower < 200:
			print("You charged up your magic power by 30")
			self.magicpower += 30
			if self.magicpower >= 200:
				self.magicpower = 200
		elif self.magicpower >= 200:
			print("You Can't Get Any More MPP. You are at the Max of 200!")

	def xpfarm(self):
		print("You have selected to XP farm for a minute")
		print("WAITING...")
		ws(t=60)
		self.playerxp += self.playerxpneeded
		self.swordxp += self.swordxpneeded
		dll(n=2)
		print("Done!")


print("Your stats have been loaded!")


def main():
	sim = Simulator()
	selection = ""
	menu = '''
1 = Battle
2 = Check Sword Stats
3 = Check Player Stats
4 = Heal
5 = Power up Magic
6 = XP farm
7 = Leave Sim
'''
	while selection != "7":
		print(menu)
		selection = input("What is your selection?\n")
		if selection == "1":
			sim.battle()
			sim.levelup()
			sim.setsave()
		elif selection == "2":
			sim.showswordstats()
			sim.setsave()
		elif selection == "3":
			sim.showplayerstats()
			sim.setsave()
		elif selection == "4":
			sim.heal()
			sim.setsave()
		elif selection == "5":
			sim.magicpowerup()
			sim.setsave()
		elif selection == "6":
			sim.xpfarm()
			sim.levelup()
			sim.setsave()
			ws(t=2)
		elif selection == "7":
			print("POWERING DOWN.")
			ws(t=2)
			print('GOODBYE...')
			exit()
		else:
			print("Invalid Selection. Please Try Again")
		ws(t=2)
		dll(n=25)


if __name__ == '__main__':
	main()
