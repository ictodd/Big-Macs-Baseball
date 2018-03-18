import random

class Base:
	def __init__(self, name):
		self.Name = name
		self.PlayerHere = None

class Team:
	def __init__(self, name):
		self.Name = name
		self.Score = 0
		self.Players = None
		self.AccumulatedOuts = 0
		self.OutCount = 0
		
	def HalfInning(self, bases):
		for player in self.Players:
			player.swing(bases)
			if(self.OutCount >= 3):
				ResetBases(bases)
				return

class Player:
	def __init__(self, name, myTeam, 
					position, OBP, SingleR, 
					DoubleR, TripleR, HomeRunR, 
					WalkR, HBPR, SOR, FlyGrR, DPR):

		#general stats
		self.Name = name
		self.MyTeam = myTeam
		self.Position = position

		#used to determine if out or not
		self.OBP = OBP

		#stats on
		self.SingleR = SingleR
		self.DoubleR = DoubleR
		self.TripleR = TripleR
		self.HomeRunR = HomeRunR
		self.WalkR = WalkR
		self.HBPR = HBPR

		#stats out		
		self.SOR = SOR
		self.FlyGrR = FlyGrR
		self.DPR = DPR

	def swing(self, allBases):
		swingResult = self.getSwingResult();
		#print(self.Name + ' using swing(), swingResult = ' + str(swingResult))
		
		if(swingResult > 0 and swingResult < 4):
			self.AdjustBases(swingResult, allBases) 
			allBases[swingResult].PlayerHere = self
		elif(swingResult == 4):
			self.AdjustBases(swingResult, allBases) 
			self.MyTeam.Score += 1
		elif(swingResult == 0):
			self.MyTeam.OutCount += 1
			self.MyTeam.AccumulatedOuts += 1

		#self.PrintBasesStatus(allBases)

	def getSwingResult(self):
		rnd = random.randint(1,1001)
		#first, determine if assessing on or out ranges
		if(rnd < self.OBP):
			playerOBPresult = random.randint(1,1001)

			if(playerOBPresult in self.WalkR): 
				return 1
			elif(playerOBPresult in self.SingleR):
				return 1
			elif(playerOBPresult in self.HBPR):
				return 1
			elif(playerOBPresult in self.DoubleR):
				return 2
			elif(playerOBPresult in self.TripleR):
				return 3
			elif(playerOBPresult in self.HomeRunR):
				return 4

		else:
			playerOutResult = random.randint(1,1001)

			if(playerOutResult in self.SOR): 
				return 0
			elif(playerOutResult in self.FlyGrR):
				return 0
			elif(playerOutResult in self.DPR):
				return 0

	def PrintBasesStatus(self, allBases):
		for base in allBases:
			if(base.PlayerHere != None):
				print('Name: ' + base.Name + ' Player: ' + base.PlayerHere.Name)
			else:
				print('Name: ' + base.Name + ' Player: None')

	def AdjustBases(self, swingResult, allBases):
		count = 4
		for base in reversed(allBases):
			if(base.PlayerHere != None and count == 4 and swingResult >= 1):
				count -= 1
				#player is on Base 4 and swingResult is at least 1
				#remove player from bases list and add 1 to teams score
				base.PlayerHere = None
				self.MyTeam.Score += 1
			elif(base.PlayerHere != None and count == 3 and swingResult >= 2):
				count -= 1
				#player is on Base 3 and swingResult is at least 2
				#remove player from bases list and add 1 to teams score
				base.PlayerHere = None
				self.MyTeam.Score += 1
			elif(base.PlayerHere != None and count == 2 and swingResult >=3):
				count -= 1
				#player is on Base 2 and swingResult is at least 3
				#remove player from bases list and add 1 to teams score
				base.PlayerHere = None
				self.MyTeam.Score += 1
			elif(base.PlayerHere != None and count == 1 and swingResult >=4):
				count -= 1
				#player is on Base 1 and swingResult is at least 4
				#remove player from bases list and add 1 to teams score
				base.PlayerHere = None
				self.MyTeam.Score += 1
			elif(base.PlayerHere != None):
				count -= 1
				tempPlayer = base.PlayerHere
				allBases[count + swingResult].PlayerHere = tempPlayer
				base.PlayerHere = None
			else:
				count -=1

class Pitcher:
	def __init__(self, name, era):
		self.Name = name
		self.ERA = era

	def Pitch(self):
		# TO DO
		# needs to modify the Players OBP value
		# based on the ERA

class Game:
	def __init__(self, team1, team2):
		self.Team1 = team1
		self.Team2 = team2
		self.CurrentInning = 0

	def PlayBall(self, bases):
		for i in range(1,28):
			self.CurrentInning = i
			self.Team1.HalfInning(bases)
			self.Team2.HalfInning(bases)
			self.PrintCurrentResults()

	def PrintCurrentResults(self):
		print('Results after inning ' + str(self.CurrentInning) + ':')
		print('\n')
		print('\tName: ' + self.Team1.Name)
		print('\tScore: ' + str(self.Team1.Score))
		print('\n')
		print('\tName: ' + self.Team2.Name)
		print('\tScore: ' + str(self.Team2.Score))
		print('\n')
	
# general utility function
def ResetBases(bases):
	for base in bases:
		base.PlayerHere = None

