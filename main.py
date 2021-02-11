import random
from tkinter import *
leagues = ["Premier League" , "La Liga" , "BundesLiga"]
premierLeague = ["Arsenal" , "Aston Villa" , "Brighton" , "Burnely" , "Chelsea", "Crystal Palace", "Everton", "Fulham" , "Leeds" , "Leicester City" , "Liverpool" , "Manchester City" ,"Manchester United" , "Newcastle" , "Shefield United", "Southampton" ,"Tottenham" ,"West Brom" ,"West Ham","Wolves"]
leagueTable =[]
playerTeam  = None
confirm = False
run = True
version = "Pre Alpha 1.1"
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
    global premierLeague
    with open("league.txt" , "w") as leagueFile:
      leagueFile.write("Premier League")
      leagueFile.close()
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
  with open("leagueTable.txt", "a") as leagueTableFile:
    for i in range(len(premierLeague)):
      leagueTable.append([[premierLeague[i]],[0]])
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
    




print("Python Football Sim")
print("Version - " + version)
print("""
  
""")
#NewOrLoad()
setup()
if playerTeam in premierLeague:
    premierLeagueTableSetup()


