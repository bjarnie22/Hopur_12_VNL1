from data.player_data import Player_data
from data.team_data import Team_data

class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_data()
        self.team_data = Team_data()

    def get_all_players(self):
        return self.player_data.get_all_players()

    def get_all_teams(self):
        return self.team_data.get_all_teams()