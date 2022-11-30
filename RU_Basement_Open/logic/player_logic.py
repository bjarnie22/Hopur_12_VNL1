from data.player_data import Player_data
from model.player import Player
from data.data_wrapper import Data_Wrapper

class Player_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_customer(self, customer):
        """Takes in a customer object and forwards it to the data layer"""
        pass
        #self.data_wrapper.create_customer(customer)

    def get_all_players(self):
        return self.data_wrapper.get_all_players()