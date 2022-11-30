from data.tournament_data import Tournament_data
from model.tournament import Tournament
from data.data_wrapper import Data_Wrapper

class Tournament_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_team(self, team):
        """Takes in a customer object and forwards it to the data layer"""
        pass
        #self.data_wrapper.create_team(team)

    def get_tournament_info(self):
        return self.data_wrapper.get_tournament_info()