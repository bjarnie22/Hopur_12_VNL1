class Match:
    def __init__(self,date,home_team,away_team,result="",winner="",match_id=-1,round1="",round1_home_player="",round1_away_player="",round2="",round2_home_player="",round2_away_player="",round3="",round3_home_player="",round3_away_player="",round4="",round4_home_player="",round4_away_player="",round5="",round5_home_player1="",round5_home_player2="",round5_away_player1="",round5_away_player2="",round6="",round6_home_player1="",round6_home_player2="",round6_away_player1="",round6_away_player2="",round7="",round7_home_player1="",round7_home_player2="",round7_home_player3="",round7_home_player4="",round7_away_player1="",round7_away_player2="",round7_away_player3="",round7_away_player4="",qp_player_h_1="",qp_player_h_2="",qp_player_h_3="",qp_player_h_4="",qp_player_a_1="",qp_player_a_2="",qp_player_a_3="",qp_player_a_4=""):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.winner = winner
        self.match_id = match_id
        
        self.round1 = round1
        self.round1_home_player = round1_home_player
        self.round1_away_player = round1_away_player

        self.round2 = round2
        self.round2_home_player = round2_home_player
        self.round2_away_player = round2_away_player

        self.round3 = round3
        self.round3_home_player = round3_home_player
        self.round3_away_player = round3_away_player

        self.round4 = round4
        self.round4_home_player = round4_home_player
        self.round4_away_player = round4_away_player

        self.round5 = round5
        self.round5_home_player1 = round5_home_player1
        self.round5_home_player2 = round5_away_player2
        self.round5_away_player1 = round5_away_player1
        self.round5_away_player2 = round5_away_player2

        self.round6 = round6
        self.round6_home_player1 = round6_home_player1
        self.round6_home_player2 = round6_home_player2
        self.round6_away_player1 = round6_away_player1
        self.round6_away_player2 = round6_away_player2

        self.round7 = round7
        self.round7_home_player1 = round7_home_player1
        self.round7_home_player2 = round7_home_player2
        self.round7_home_player3 = round7_home_player3
        self.round7_home_player4 = round7_home_player4
        self.round7_away_player1 = round7_away_player1
        self.round7_away_player2 = round7_away_player2
        self.round7_away_player3 = round7_away_player3
        self.round7_away_player4 = round7_away_player4

        self.qp_player_h_1 = qp_player_h_1
        self.qp_player_h_2 = qp_player_h_2      
        self.qp_player_h_3 = qp_player_h_3
        self.qp_player_h_4 = qp_player_h_4
        self.qp_player_a_1 = qp_player_a_1
        self.qp_player_a_2 = qp_player_a_2
        self.qp_player_a_3 = qp_player_a_3
        self.qp_player_a_4 = qp_player_a_4