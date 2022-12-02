from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.team import Team
from model.association import Association
from model.tournament import Tournament

a = Logic_Wrapper()
listi = a.get_all_players()

for elem in listi:
    print(f"Name is: {elem.name:<15} SSN: {elem.social_security_number:<15} phone number: {elem.phone_number:<15}")

print()
for elem in listi:
    if elem.social_security_number == "0512972122":
        print(elem.name, elem.email, "\n")

for elem in listi:
    if elem.name == "Arnór":
        print(elem.name, elem.email, elem.phone_number, "\n")

for elem in listi:
    if elem.team_id == "0":
        print(elem.name, elem.email)
print()

listi2 = a.get_all_teams()

for elem in listi2:
    if elem.name == "Fálkarnir":
        True

for elem in listi2:
    if elem.association_id == "0":
        print(elem.name)

listi3 = a.get_all_associations()

print()
for elem in listi3:
    print(elem.name)

print()
print("Tournament information")

listi4 = a.get_tournament_info()

for tou in listi4:
    print(tou.tournament_name)



#name = input("name: ")
#date_of_birth = input("date_of_birth (dd/mm/yyyy) ") # er á réttur formati + ekki fæddur í framtíðinni
#address = input("address: ")
#email = input("email: ") # er @
#phone_number = input("phone_number: ") # er allt tölur
#social_security_number = input("social_security_number: ") # er allt tölur

#for elem in listi2:
#    print(elem.name, elem.team_id)

#team_id = input("team_id: ")

#dúddi = Player(team_id, name, social_security_number, date_of_birth, email, address, phone_number)
#a.create_player(dúddi)

name = input("name: ")

for elem in listi3:
    print(f"name: {elem.name:<5} id: {elem.association_id}")
association_id = input("association_id: ")

new_team = Team(name, association_id)
a.create_team(new_team)

for elem in listi:
    print(f"name:{elem.name:<5} id: {elem.social_security_number}")

captain = input("captains social security number: ")

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