import random
import os
import csv


#Veriables
leagues = ["Premier League" , "La Liga" , "BundesLiga"]
premierLeague = ["Arsenal" , "Aston Villa" ,"Brentford", "Brighton" , "Burnely" , "Chelsea", "Crystal Palace", "Everton", "Leeds" , "Leicester" , "Liverpool" , "ManchesterC" ,"ManchesterU" , "Newcastle" , "Norwich", "Southampton" ,"Tottenham", "Watford" ,"West Ham","Wolves"]
leagueTable =[] #stores league table values
fixturesList = [] # stores that weeks fixtures
playerTeam  = None 
confirm = False
run = True
matchday = 1
leagueCode = None 
version = "Pre Alpha 1.2"
playerFixture = None
playerLeague = ""



#Algorithims
def NewOrLoad(): # not in use
  global load
  global new
  validinput = False
  while validinput == True:
    choice = input("Would you like to load your old or start new\n")
    if choice.lower == "load":
      validinput = True
      load()
    elif choice.lower == "new":
      setup()

def load(): # not currentlu in use
  with open("team.txt", "r") as teamFile:
    team = teamFile.read() # Makes the team in the file the player team 
    global playerTeam
    playerTeam = team
    return playerTeam
    teamFile.close()
  print("Loading " + playerTeam + "Save")
  global leagueTable
  with open("leagueTable.txt","r") as LeagueTableFile:  # Imports the table from the save file
    contents = LeagueTableFile.read()
    leagueTable.clear()
    leagueTable.append(contents)
    LeagueTableFile.close()
  return leagueTable
  print(leagueTable)


def setup():
  complete = False
  confirm = False
  while confirm == False:
    league = input(""" What League do you want to pick a club from to take charge of?
    1. Premier League
    2. La Liga
    3. Bundesliga
    Enter The Number Below
    """)
    if league == "1": 
      global playerLeague
      playerLeague = "Premier League"
      global premierLeague
      with open("league.txt" , "w") as leagueFile:
        leagueFile.write("Premier League") # saves the league in the league file
        leagueFile.close()
        os.system('clear')
      print("Which Team?")
      for i in range(len(premierLeague)):
        print(str(i) + " " + premierLeague[i]) #prints out all of the team options with a corresonding number
      team = input()
      global playerTeam
      playerTeam = premierLeague[int(team)]
      print("You are about to control " + playerTeam)
      confirmYOrN() 
      with open("team.txt" ,"w") as teamFile: #saves the player team to the team txt file
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
  global playerLeague
  with open ("fixtures/"+ playerLeague + "/" + str(matchday) +".txt", "r") as fixtureFile:
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
  for i in leagueTable:
    print(*i)
  while correctInput == False:
    inputKey = input('Type a to Sim\n')
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
  global leagueTable

  homeTeam = playerFixture[0]
  if playerFixture[2] != "v":
    awayTeam = playerFixture[2]
  else:
    awayTeam = playerFixture[3]

  with open("Probablities/PLproablites.csv" , "r") as probsfile: #Loads csv probs file and saves it to probs array
    probs = list(csv.reader(probsfile))
    probsfile.close()

  for i in probs:#Loads the probs for each team
    if i[0] == homeTeam:
      homeProb = int(i[1])
    elif i[0] == awayTeam:
      awayProb = int(i[1])

  homeScore = random.randint(0, homeProb)#Generates scoreline
  awayScore = random.randint(0, awayProb)
  print(homeTeam + " " + str(homeScore) + " - " + str(awayScore) + " " + awayTeam)
  
  if homeScore >= awayScore: # Updates the league table
    for i in leagueTable:
      if i[0] == homeTeam:
        i[1] += 3
  if awayScore >= homeScore:
    for i in leagueTable:
      if i[0] == awayTeam:
        i[1] += 3
  if homeScore == awayScore :
    for i in leagueTable:
      if i[0] == awayTeam or homeTeam:
        i[1] += 1

def aiMatchEngine():
  global fixturesList
  global matchday
  global leagueTable
  for i in fixturesList:
    homeTeam = i[0]
    if i[2] != "v":
      awayTeam = i[2]
    else:
      awayTeam = i[3]

    with open("Probablities/PLproablites.csv" , "r") as probsfile: #Loads csv probs file and saves it to probs array
      probs = list(csv.reader(probsfile))
      probsfile.close()

    for i in probs:#Loads the probs for each team
      if i[0] == homeTeam:
        homeProb = int(i[1])
      elif i[0] == awayTeam:
        awayProb = int(i[1])

    homeScore = random.randint(0, homeProb)#Generates scoreline
    awayScore = random.randint(0, awayProb)
    print(homeTeam + " " + str(homeScore) + " - " + str(awayScore) + " " + awayTeam)
  
    if homeScore >= awayScore: # Updates the league table
      for i in leagueTable:
        if i[0] == homeTeam:
          i[1] += 3
    elif awayScore >= homeScore:
      for i in leagueTable:
        if i[0] == awayTeam:
          i[1] += 3
    elif homeScore == awayScore :
      for i in leagueTable:
        if i[0] == awayTeam or homeTeam:
          i[1] += 1
  leagueTable = (sorted(leagueTable, key=lambda x: x[1], reverse=True))
  print("")
  print("")
  for i in leagueTable:
    print(*i)
  moveScreen = False
  while moveScreen == False:
    Continue = input("Type a to move to next Matchday\n")
    if Continue.lower() =="a":
      Continue = True
      matchday = 2
      break


  

  




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
  #while matchday <= 38:
  matchdayPage()
  clear()
  matchEngine()
  aiMatchEngine()
    

