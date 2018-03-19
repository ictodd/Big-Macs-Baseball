import random
import xlwings as xw

class GlobalSwitch:
	DEBUG = False

class Utilities:
	def Pause():
		input('Press any key to continue...')

class Base:
	def __init__(self, name):
		self.Name = name
		self.PlayerHere = None

class Stat:
	def __init__(self, name, range):
		self.Name = name
		self.Value = range

class Team:
	def __init__(self, name):
		self.Name = name
		self.Score = 0
		self.Players = None
		self.AccumulatedOuts = 0
		self.OutCount = 0
		
	def HalfInning(self, bases):
		teamIsIn = True
		while(teamIsIn):
			for player in self.Players:
				player.swing(bases)
				player.PrintBasesStatus(bases)
				self.PrintScore()
				Utilities.Pause()
				if(self.OutCount >= 3):
					ResetBases(bases)
					teamIsIn = False
					return


	def PrintScore(self):
		print('DEBUG: Stats for ' + self.Name + 
					' Score: ' + str(self.Score) + 
					' Outs: ' + str(self.OutCount) + 
					' Total Outs: ' + str(self.AccumulatedOuts))

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
		
		print(self.Name + ' gets swingResult = ' + str(swingResult))
		
		if(swingResult > 0 and swingResult < 4):
			self.AdjustBases(swingResult, allBases) 
			allBases[swingResult].PlayerHere = self
		elif(swingResult == 4):
			self.AdjustBases(swingResult, allBases) 
			self.MyTeam.Score += 1
		elif(swingResult == 0):
			self.MyTeam.OutCount += 1
			self.MyTeam.AccumulatedOuts += 1

	def getSwingResult(self):
		
		result = -1
		
		rnd = random.randint(1,1001)
		#first, determine if assessing on or out ranges
		
		
		if(rnd > self.OBP):
			playerOBPresult = random.randint(1,1001)

			if(playerOBPresult in self.WalkR): 
				result = 1
			elif(playerOBPresult in self.SingleR):
				result = 1
			elif(playerOBPresult in self.HBPR):
				result = 1
			elif(playerOBPresult in self.DoubleR):
				result = 2
			elif(playerOBPresult in self.TripleR):
				result = 3
			elif(playerOBPresult in self.HomeRunR):
				result = 4

		else:
			playerOutResult = random.randint(1,1001)

			if(playerOutResult in self.SOR): 
				result =  0
			elif(playerOutResult in self.FlyGrR):
				result =  0
			elif(playerOutResult in self.DPR):
				result =  0
		if (result < 0):
			Utilities.Pause()

		return result

	def PrintBasesStatus(self, allBases):
		for base in allBases:
			if(base.PlayerHere != None):
				print('Name: ' + base.Name + '\t Player: ' + base.PlayerHere.Name)
			else:
				print('Name: ' + base.Name + '\t Player: None')

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

	#def Pitch(self):
		# TO DO
		# needs to modify the Players OBP value
		# based on the ERA

class PlayerFactory:
	def __init__(self):
		self.PlayerDBPath = './OnBaseRangeCalculator.xlsm'
		self.wb = None
		self.ws = None
		
	def GetPlayer(self, NameToFind, InTeam, Position):
		'''
		Player def __init__(self, name, myTeam, 
								position, OBP, SingleR, 
								DoubleR, TripleR, HomeRunR, 
								WalkR, HBPR, SOR, FlyGrR, DPR):
		'''
		
		
		self.wb = xw.books.open(self.PlayerDBPath)
		self.ws = self.wb.sheets['Results']

		targetRow = self.FindPlayer(NameToFind)

		# start with the ints from the model
		iWalk = self.GetValue("F", targetRow)
		iDouble = self.GetValue("G", targetRow)
		iTriple = self.GetValue("H", targetRow)
		iHomeRun = self.GetValue("I", targetRow)
		iSingle = self.GetValue("J", targetRow)
		iHBP = self.GetValue("K", targetRow)

		iOBP = self.GetValue("L", targetRow)

		iSO = self.GetValue("Q", targetRow)
		iFlyOut = self.GetValue("P", targetRow)
		iDoublePlay = self.GetValue("O", targetRow)

		# convert to ranges
		rWalk = self.GenerateRange(1, iWalk)
		rDouble = self.GenerateRange(iWalk + 1, iDouble)
		rTriple = self.GenerateRange(iDouble + 1, iTriple)
		rHomeRun = self.GenerateRange(iTriple + 1, iHomeRun)
		rSingle = self.GenerateRange(iHomeRun + 1, iSingle)
		rHBP = self.GenerateRange(iSingle + 1, iHBP)

		rDoublePlay = self.GenerateRange(1, iDoublePlay)
		rFlyOut = self.GenerateRange(iDoublePlay + 1, iFlyOut)
		rSO = self.GenerateRange(iFlyOut + 1, iSO)

		tempPlayer = Player(NameToFind, 
							  InTeam, 
							  Position, 
							  iOBP, 
							  rSingle, 
							  rDouble, 
							  rTriple, 
							  rHomeRun, 
							  rWalk, 
							  rHBP,
							  rSO,
							  rFlyOut,
							  rDoublePlay)
		self.DEBUG_PrintNewPlayer(tempPlayer)
		return tempPlayer

	def DEBUG_PrintNewPlayer(self, player: Player):
		if(GlobalSwitch.DEBUG == True):
			print('DEBUG: New player made: ')
			print('DEBUG: Name: \t' + player.Name)
			print('DEBUG: OBP: \t' + str(player.OBP))
			print('DEBUG: Single: \t' + str(player.SingleR))
			print('DEBUG: Double: \t' + str(player.DoubleR))
			print('DEBUG: Triple: \t' + str(player.TripleR))
			print('DEBUG: HR: \t' + str(player.HomeRunR))
			print('DEBUG: Walk: \t' + str(player.WalkR))
			print('DEBUG: HBP: \t' + str(player.HBPR))
			print('DEBUG: SO: \t' + str(player.SOR))
			print('DEBUG: FO: \t' + str(player.FlyGrR))
			print('DEBUG: DP: \t' + str(player.DPR))

	def GenerateRange(self, lower,upper):
		if(lower > upper):
			return range(upper, upper)
		else:
			return range(lower,upper)

	def GetValue(self, column, row):
		return int(self.ws.range(column + str(row)).value)

	def FindPlayer(self, name):
		# get last row of data in column A
		lr = self.ws.range('A65550').end(xw.constants.Direction.xlUp).row
		for r in range(2,lr + 1):
			if(self.ws.range('A' + str(r)).value == name):
				return r


class Game:
	def __init__(self, team1, team2):
		self.Team1 = team1
		self.Team2 = team2
		self.CurrentInning = 0

	def PlayBall(self, bases):
		for i in range(1,28):
			self.CurrentInning = i
			self.Team1.HalfInning(bases)
			self.Team1.OutCount = 0
			self.Team2.HalfInning(bases)
			self.Team2.OutCount = 0
			self.PrintCurrentResults()
			Utilities.Pause()

	def PrintCurrentResults(self):
		print('Inning ' + str(self.CurrentInning) + ': ' 
				+ self.Team1.Name + " " + str(self.Team1.Score)
				+ self.Team2.Name + " " + str(self.Team2.Score))
	
# general utility function
def ResetBases(bases):
	for base in bases:
		base.PlayerHere = None

