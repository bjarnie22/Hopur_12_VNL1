from logic.logic_wrapper import Logic_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_logic
from model.player import Player
from model.team import Team

a = Player_logic()
listi = a.get_all_players()

for elem in listi:
    print(f"Name is: {elem.name:<15}, SSN: {elem.social_security_number:<15}, phone number: {elem.phone_number:<15}")

print()
for elem in listi:
    if elem.social_security_number == "0512972122":
        print(elem.name, elem.email, "\n")

for elem in listi:
    if elem.name == "Arnór":
        print(elem.name, elem.email, elem.phone_number, "\n")

for elem in listi:
    if elem.team_id == "01":
        print(elem.name, elem.email)


b = Team_logic()
listi2 = b.get_all_teams()

for elem in listi2:
    if elem.name == "Fálkarnir":
        print(elem.players)