from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.team import Team
from model.association import Association
from model.tournament import Tournament
from model.match import Match

from UI.match_ui import Match_UI

a = Logic_Wrapper()

listi = a.get_all_players()
listi2 = a.get_all_teams()
listi3 = a.get_all_associations()
listi4 = a.get_tournament_info()

#for elem in listi:
 #   print(f"Name is: {elem.name:<20} SSN: {elem.social_security_number:<20} phone number: {elem.mobile:<13}")

#print()
#for elem in listi:
 #   if elem.social_security_number == "0512972122":
  #      print(elem.name, elem.email, "\n")

#for elem in listi:
 #   if elem.name == "Arnór":
  #      print(elem.name, elem.email, elem.phone_number, "\n")

#for elem in listi:
 #   if elem.team_id == "0":
  #      print(elem.name, elem.email)
#print()


#for elem in listi2:
 #   if elem.name == "Fálkarnir":
  #      True

#for elem in listi2:
 #   if elem.association_id == "0":
  #      print(elem.name)

#print(f"{listi4[0].tournament_name} by {listi4[0].admin_name}")
#print()
#print("All associtaions/teams/players", "\n")
#for elem in listi3:
#    print(f"{elem.name}, {elem.association_id}:")
#    for t in listi2:
#      if t.association_id == elem.association_id:
#        print(f"{t.name:<10}:")
#        for p in listi:
#          if p.team_id == t.team_id:
#            if p.social_security_number == t.captain_id:
#              print(f"{p.name:<25} (C)")
#            else:
#              print(f"{p.name:<25}")

#print()
#print("Tournament information")

#for tou in listi4:
 #   print(tou.tournament_name)

#print()

#name = input("name: ")
#date_of_birth = input("date_of_birth (dd/mm/yyyy) ") # er á réttur formati + ekki fæddur í framtíðinni
#address = input("address: ")
#email = input("email: ") # er @
#phone_number = input("phone_number: ") # er allt tölur
#social_security_number = input("social_security_number: ") # er allt tölur
#mobile = input("mobile number: ")

#for elem in listi2:
#    print(elem.name, elem.team_id)

#team_id = input("team_id: ")

#dúddi = Player(team_id, name, social_security_number, date_of_birth, email, address, phone_number, mobile)
#a.create_player(dúddi)

#name = input("name: ")

#for elem in listi3:
 #   print(f"name: {elem.name:<5} id: {elem.association_id}")
#association_id = input("association_id: ")

#new_team = Team(name, association_id)
#a.create_team(new_team)

#for elem in listi2:
 #   print(elem.name, elem.team_id)

#teamID = input("pick a team to choose a captain for: ")

#for elem in listi:
 #   if elem.team_id == teamID:
 #       print(f"name:{elem.name:<5} id: {elem.social_security_number}")

#captain = input("captains social security number: ")
#a.choose_captain(teamID, captain)

#name = input("name: ")
#address = input("address: ")
#nmr = input("phone number: ")
#assoc = Association(name, address, nmr)

#a.create_association(assoc)

#nafn = input("name of tourament: ")
#name = input("name: ")
#mail = input("mail: ")
#nmr = input("phone number: ")
#start = input("starts: ")
#end = input("ends: ")
#rnds = input("number of rounds: ")
#new_tourny = Tournament(nafn, name, nmr, mail, start, end, rnds)
#a.create_tournament(new_tourny)

#AvB = Match("27/09/2022", "2", "3")

#a.create_match(AvB)

#a.postpone_match("1", "01/12/2022")

#a.update_result("0", "6-1")

#a.create_match_schedule()


#b = Match(date, home_team, away_team)

#a.create_match(match)

match_list = a.get_all_matches()

empty_space = ""
league_list = a.get_league_standings()
print("Leauge Standing:")
print(f"Position{empty_space:>5}Team{empty_space:>8}Matches played{empty_space:>5}Matches won{empty_space:>3}Legs won\n")
for team, i in zip(league_list, range(1,len(league_list)+1)):
  print(f"{i:>4}{empty_space:<5}{team[4]:<23}{team[3]:<12}{team[0]:>5}{team[1]:>14}")