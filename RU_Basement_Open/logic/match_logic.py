from model.match import Match
from data.data_wrapper import Data_Wrapper

class Match_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()

    
    def get_all_matches(self):
        """"""
        return self.data_wrapper.get_all_matches()


    def create_match(self, match):
        """"""
        return self.data_wrapper.create_match(match)


    def postpone_match(self, match_id, date):
        """"""
        return self.data_wrapper.postpone_match(match_id, date)
    

    def update_score(self, match_id, score):
        """"""
        return self.data_wrapper.update_score(match_id, score)