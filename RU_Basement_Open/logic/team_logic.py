from data.team_data import Team_data
from model.team import Team
from data.data_wrapper import Data_Wrapper

class Team_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_team(self, team):
        """Takes in a customer object and forwards it to the data layer"""
        pass
        #self.data_wrapper.create_team(team)

    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()