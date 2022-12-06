from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.team import Team
from model.association import Association
from model.tournament import Tournament
from model.match import Match

#Player(team_id, name, social_security_number, date_of_birth, email)
gummi = Player("0", "Guðmundur", "0909091212", "09/09/2009", "Gudmundur@mail.com")

if len(gummi.name) > 50:
    #return "NameTooLongError"

if len(gummi.social_security_number) != 10: