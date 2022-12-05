from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_logic
from logic.association_logic import Association_logic
from logic.tournament_logic import Tournament_logic
from logic.match_logic import Match_logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic()
        self.team_logic = Team_logic()
        self.association_logic = Association_logic()
        self.tournament_logic = Tournament_logic()


    def get_all_players(self):
        """Takes in a"""
        return self.player_logic.get_all_players()
    
    def create_player(self, player):
        """Takes in a player object and forwards it to the data layer"""
        return self.player_logic.create_player(player)


    def get_all_teams(self):
        return self.team_logic.get_all_teams()
    
    def create_team(self, team):
        """Takes in a team object and forwards it to the data layer"""
        return self.team_logic.create_team(team)

    def choose_captain(self, team_id, captain_id):
        return self.team_logic.choose_captain(team_id, captain_id)


    def get_all_associations(self):
        
        return self.association_logic.get_all_associations()

    def create_association(self, association):
        """Takes in a association object and forwards it to the data layer"""
        return self.association_logic.create_association(association)
    

    def get_tournament_info(self):
        return self.tournament_logic.get_tournament_info()
    
    def create_tournament(self, tournament):
        """Takes in a tournament object and forwards it to the data layer"""
        return self.tournament_logic.create_tournament(tournament)
    

    def get_all_matches(self):
        return self.match_logic.get_all_matches()
    
    def create_tournament(self, match):
        """Takes in a match object and forwards it to the data layer"""
        return self.match_logic.create_match(match)