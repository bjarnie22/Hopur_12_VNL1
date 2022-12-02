from data.player_data import Player_data
from model.player import Player
from data.data_wrapper import Data_Wrapper

class Player_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_player(self, player):
        """Takes in a player object and forwards it to the data layer"""
        self.data_wrapper.create_player(player)

    def get_all_players(self):
        return self.data_wrapper.get_all_players()

    def get_player_by_name(self, name):
        all_players = self.get_all_players()
        for elem in all_players:
            if elem.name == name:
                return elem