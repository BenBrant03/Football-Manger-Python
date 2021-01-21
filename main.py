leagues = ["Premier League" , "La Liga" , "BundesLiga"]
premierLeague = ["Arsenal" , "Aston Villa" , "Brighton" , "Burnely" , "Chelsea", "Crystal Palace", "Everton", "Fulham" , "Leeds" , "Leicester City" , "Liverpool" , "Manchester City" ,"Manchester United" , "Newcastle" , "Shefield United", "Southampton" ,"Tottenham" ,"West Brom" ,"West Ham","Wolves"]
leagueTable =[]
playerTeam  = "blank"
confirm = False
run = True
version = "Pre Alpha 1.0"

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
    print("Which Team?")
    for i in range(len(premierLeague)):
      print(str(i) + " " + premierLeague[i])
    team = input()
    global playerTeam
    playerTeam = premierLeague[int(team)]
    print("You are about to control " + playerTeam)
    return playerTeam
    confirmYOrN()
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
  for i in range(len(premierLeague)):
    leagueTable.append(premierLeague[i] , 0)


  


print("Python Football Sim")
print("Version - " + version)
print("""
  
""")
setup()
if playerTeam in premierLeague:
    premierLeagueTableSetup()


