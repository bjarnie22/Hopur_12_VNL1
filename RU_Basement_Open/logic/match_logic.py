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
    

    def update_result(self, match_id, match):
        """"""
        match_list = self.get_all_matches()
        for elem in match_list:
            if match_id == elem.match_id:
                if elem.result == "":
                    return False
                else:
                    return self.data_wrapper.update_result(match_id, match)


    def create_match_schedule(self):
        """"""
        return self.data_wrapper.create_match_schedule()
    
    
    def wipe_match_schedule(self):
        """Wipes the match schedule so that create_match_schedule can be used again correctly"""
        return self.data_wrapper.wipe_match_schedule()


    def register_result_captain(self, match):
        match_list = self.get_all_matches()
        for elem in match_list:
            if match.match_id == elem.match_id:
                if elem.result != "":
                    return False
                else:
                    return self.data_wrapper.register_result_captain(match)

    
    def highest_quality_points_list(self, player_list):
        match_list = self.get_all_matches()
        qp_list = []

        for player, i in zip(player_list, range(len((player_list)))):
            for match in match_list:
                if match.result == "":
                    continue
                else:
                    if match.round7_away_player1 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_a_1)
                        except:
                            qp_list.append([int(match.qp_player_a_1),1,player.name])
                    elif match.round7_away_player2 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_a_2)
                        except:
                            qp_list.append([int(match.qp_player_a_2),1,player.name])
                    elif match.round7_away_player3 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_a_3)
                        except:
                            qp_list.append([int(match.qp_player_a_3),1,player.name])
                    elif match.round7_away_player4 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_a_4)
                        except:
                            qp_list.append([int(match.qp_player_a_4),1,player.name])
                    elif match.round7_home_player1 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_h_1)
                        except:
                            qp_list.append([int(match.qp_player_h_1),1,player.name])
                    elif match.round7_home_player2 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_h_2)
                        except:
                            qp_list.append([int(match.qp_player_h_2),1,player.name])
                    elif match.round7_home_player3 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_h_3)
                        except:
                            qp_list.append([int(match.qp_player_h_3),1,player.name])
                    elif match.round7_home_player4 == player.social_security_number:
                        try:
                            if player.name in qp_list[i]:
                                qp_list[i][1] += 1
                                qp_list[i][0] += int(match.qp_player_h_4)
                        except:
                            qp_list.append([int(match.qp_player_h_4),1,player.name])
        qp_list.sort(reverse=True)
        return qp_list