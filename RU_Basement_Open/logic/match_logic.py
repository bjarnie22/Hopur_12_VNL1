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
        match_list = self.get_all_matches()
        for elem in match_list:
            if match_id == elem.match_id:
                if elem.result != "":
                    return False
                else:
                    return self.data_wrapper.postpone_match(match_id, date)
    

    def update_result(self, match_id, result):
        """"""
        match_list = self.get_all_matches()
        for elem in match_list:
            if match_id == elem.match_id:
                if elem.result == "":
                    return False
                else:
                    return self.data_wrapper.update_result(match_id, result)


    def create_match_schedule(self):
        """"""
        return self.data_wrapper.create_match_schedule()


    def register_result_captain(self, match):
        return self.data_wrapper.register_result_captain(match)