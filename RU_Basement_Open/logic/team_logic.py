from data.team_data import Team_data
from model.team import Team
from data.data_wrapper import Data_Wrapper

class Team_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_team(self, team):
        """Takes in a team object, gives it a team id and forwards it to the data layer"""
        list_of_teams = self.get_all_teams()
        team.team_id = len(list_of_teams)
        self.data_wrapper.create_team(team)

    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()