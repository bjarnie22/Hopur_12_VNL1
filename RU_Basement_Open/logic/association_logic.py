from data.data_wrapper import Data_Wrapper

class Association_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_player(self, player):
        """Takes in a association object and forwards it to the data layer"""
        pass
        #self.data_wrapper.create_player(player)

    def get_all_associations(self):
        return self.data_wrapper.get_all_associations()