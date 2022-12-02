from data.tournament_data import Tournament_data
from model.tournament import Tournament
from data.data_wrapper import Data_Wrapper

class Tournament_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_tournament(self, tournament):
        """Takes in a tournament object and forwards it to the data layer"""
        if self.get_tournament_info() == []:
            self.data_wrapper.create_tournament(tournament)
            return True # "Tournament succesfully created"
        else:
            return False # "Tournament has already been created"

    def get_tournament_info(self):
        return self.data_wrapper.get_tournament_info()