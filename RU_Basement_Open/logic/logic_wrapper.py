from data.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def get_all_teams(self):
        return self.Team_logic.get_all_teams()