import random
from tkinter import *
import os
from csv import reader
#Veriables
leagues = ["Premier League" , "La Liga" , "BundesLiga"]
premierLeague = ["Arsenal" , "Aston Villa" , "Brighton" , "Burnely" , "Chelsea", "Crystal Palace", "Everton", "Fulham" , "Leeds" , "Leicester City" , "Liverpool" , "Manchester City" ,"Manchester United" , "Newcastle" , "Shefield United", "Southampton" ,"Tottenham" ,"West Brom" ,"West Ham","Wolves"]
leagueTable =[]
fixturesList = []
playerTeam  = None
confirm = False
run = True
matchday = 1
leagueCode = None 
version = "Pre Alpha 1.1"
playerFixture = None

#Algorithims
def NewOrLoad():
  global load
  global new
  choice = input("Would you like to load your old or start new       ")
  if choice.lower == "load":
    with open("team.txt", "r") as teamFile:
      team = teamFile.read()
      global playerTeam
      playerTeam = team
      return playerTeam
      teamFile.close()
    print("Loading " + playerTeam + "Save")
    global leagueTable
    with open("leagueTable.txt","r") as LeagueTableFile:
      contents = LeagueTableFile.read()
      leagueTable.clear()
      leagueTable.append(contents)
      LeagueTableFile.close()
    return leagueTable
    print(leagueTable)



def setup():
  global confirm
  confirm = False
  league = input(""" What League do you want to pick a club from to take charge of?
  1. Premier League
  2. La Liga
  3. Bundesliga
  Enter The Number Below
  """)
  if league == "1":
    global leagueCode
    leagueCode = "PL"
    global premierLeague
    with open("league.txt" , "w") as leagueFile:
      leagueFile.write("Premier League")
      leagueFile.close()
      os.system('clear')
    print("Which Team?")
    for i in range(len(premierLeague)):
      print(str(i) + " " + premierLeague[i])
    team = input()
    global playerTeam
    playerTeam = premierLeague[int(team)]
    print("You are about to control " + playerTeam)
    confirmYOrN()
    with open("team.txt" ,"w") as teamFile:
      teamFile.write(playerTeam)
      teamFile.close()
    return playerTeam
    
  elif league == "2" or "3":
    print("Set Up coming soon. Read the list of planned leagues in the read me file for what will be coming soon")
  else:
    print("Please enter a valid league number")
    
def confirmYOrN():
  responseValid = False
  response = input("Do you want to confirm this? Type Y or N")
  while responseValid == False:
    if response == "Y" or response == "y":
      print("Confirmed")
      confirm = True
      responseValid = True
    elif response == "N" or "n":
      print("Cancelled")
      confirm = False
      responseValid = True
    else:
      print("Please Enter a Valid Response")

def premierLeagueTableSetup():
  global premierLeague
  with open("leagueTable.txt", "w") as leagueTableFile:
    for i in range(len(premierLeague)):
      leagueTable.append([premierLeague[i],0])
    leagueTableFile.write(str(leagueTable))
    print("League Table Setup Sucessfull")
    leagueTableFile.close()

  
'''def fixtureSetup():
  Games
  for i in range (0,38):
   with open("MD"+i ,"w") as fixtureFile:
     homeorAway = random.randint(0,1)
     if homeorAway == 0:
       location = "home"
      else:
        location = aw'''''
#random fixture generation coming Soon
    
def loadFixtures():
  global matchday
  global leagueCode
  with open (str(leagueCode) + "matchday"+str(matchday)+".txt" , "r") as fixtureFile:
    global fixturesList
    for line in fixtureFile:
      stripedLine = line.strip()
      lineList = stripedLine.split()
      fixturesList.append(lineList)   
    fixtureFile.close()
  print("Fixtures Loaded")

def matchdayPage():
  global matchday
  global fixturesList
  global playerTeam
  global leagueTable
  global playerFixture
  correctInput = False
  saveLoction = None
  otherFixtures = []
  counted = 0
  playerFixture = []
  postion = 1
  print("Matchday" + str(matchday))
  print("Your Next Game is:")
  if len(playerTeam) == 1:
    for i in fixturesList:
      for y in i:
        if y == playerTeam:
          playerFixture = i
          print(*i)
        elif i not in otherFixtures:
          if i not in playerFixture:
            otherFixtures.append(i)
  else:
    firstWord = playerTeam.split()[0]
    for i in fixturesList:
      for y in i:
        if y == firstWord:
          playerFixture = i
          print(*i)
        elif i not in otherFixtures:
          if i not in playerFixture:
            otherFixtures.append(i)
  print('     ')
  print('The Other Fixtures')
  for i in otherFixtures:
    print(*i)
  print("Premier League")
  print("Team          Pts")
  leagueTable.sort()
  for i in leagueTable:
    print(*i)
  while correctInput == False:
    inputKey = input('Type a to Sim')
    if inputKey == 'a':
      correctInput = True
    else:
      print('Please type a and press enter')
  

def clear():
  os.system('clear')

def matchEngine():
  global playerTeam
  global playerFixture
  global matchday
  homeTeam = playerFixture[0]
  if playerFixture[2] != "v":
    awayTeam = playerFixture[2]
  else:
    awayTeam = playerFixture[3]
  

#Logic
clear()
print("Python Football Sim")
print("Version - " + version)
print("""
  
""")
#NewOrLoad()
setup()
clear()
if playerTeam in premierLeague:
    premierLeagueTableSetup()
    loadFixtures()
    clear()
    matchdayPage()
    clear()


