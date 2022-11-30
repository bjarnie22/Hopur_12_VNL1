from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_logic
from logic.association_logic import Association_logic
from logic.tournament_logic import Tournament_logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic()
        self.team_logic = Team_logic()
        self.association_logic = Association_logic()
        self.tournament_logic = Tournament_logic()

    def get_all_players(self):
        return self.player_logic.get_all_players()
    
    def create_player(self, player):
        """Takes in a player object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_all_teams(self):
        return self.team_logic.get_all_teams()
    
    def create_team(self, team):
        """Takes in a player object and forwards it to the data layer"""
        return self.team_logic.create_team(team)

    def get_all_associations(self):
        return self.association_logic.get_all_associations()
    
    def get_tournament_info(self):
        return self.tournament_logic.get_tournament_info()