from data.player_data import Player_data
from data.team_data import Team_data
from data.association_data import Association_data
from data.tournament_data import Tournament_data


class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_data()
        self.team_data = Team_data()
        self.association_data = Association_data()
        self.tournament_data = Tournament_data()

    def get_all_players(self):
        return self.player_data.get_all_players()
    
    def create_player(self, player):
        return self.player_data.create_player(player)

    def get_all_teams(self):
        return self.team_data.get_all_teams()
    
    def create_team(self, team):
        return self.team_data.create_team(team)

    def get_all_associations(self):
        return self.association_data.get_all_associations()
    
    def get_tournament_info(self):
        return self.tournament_data.get_tournament_info()