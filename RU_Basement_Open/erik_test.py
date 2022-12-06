#import datetime
"""import datetime ef leyfi gefst( notad til ad checka hvort dagatalid er valid )"""
from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.team import Team
from model.association import Association
from model.tournament import Tournament
from model.match import Match


class Player_info_check:

    def __init__(self):
        self.info = Player()
    #def player(team_id, name, social_security_number, date_of_birth, email)
#gummi = Player("0", "Guðmundur", "0909091212", "09/09/2009", "Gudmundur@mail.com")
    def player_name(self, information):
        #information is the self.info part which imports all the information from the other class
        if len(self.name) > 50:
            return "NameTooLongError"
        else:
            continue


    def social_security_number_check(self, information):
        for i in range(0:len(self.social_security_number)):
            if i > 10:
                return "NotASoSecNumError"
        try:
            sosecnum = int(self.social_security_number)
        except:
            return "NotASoSecNumError"

        if self.social_security_number[0:5]>101222:
            return "NotASoSecNumError"


    def email_check(self, information):
        counter = 0
        for char in information:
            if char == @:
                counter +=1
        if counter != 1:
            return "NotValidEmailError"


class Team_info_check:

    def __init__(self):
        self.teaminfo = Team()


    def team_name(self, information, data):
        #checks if team name is taken
        if information in data:
            return "NameTakenError"


    def association_check(self, information, data):
        #checks if the association is valid
        if information not in data:
            return "AssociationNotFoundError"
