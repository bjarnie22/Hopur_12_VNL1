class Match:
    def __init__(self,date,home_team,away_team,result="",match_id=-1,leg1="",leg1_home_player="",leg1_away_player="",leg2="",leg2_home_player="",leg2_away_player="",leg3="",leg3_home_player="",leg3_away_player="",leg4="",leg4_home_player="",leg4_away_player="",leg5="",leg5_home_player1="",leg5_home_player2="",leg5_away_player1="",leg5_away_player2="",leg6="",leg6_home_player1="",leg6_home_player2="",leg6_away_player1="",leg6_away_player2="",leg7="",leg7_home_player1="",leg7_home_player2="",leg7_home_player3="",leg7_home_player4="",leg7_away_player1="",leg7_away_player2="",leg7_away_player3="",leg7_away_player4="",qp_player_h_1="",qp_player_h_2="",qp_player_h_3="",qp_player_h_4="",qp_player_a_1="",qp_player_a_2="",qp_player_a_3="",qp_player_a_4=""):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.match_id = match_id
        
        self.leg1 = leg1
        self.leg1_home_player = leg1_home_player
        self.leg1_away_player = leg1_away_player

        self.leg2 = leg2
        self.leg2_home_player = leg2_home_player
        self.leg2_away_player = leg2_away_player

        self.leg3 = leg3
        self.leg3_home_player = leg3_home_player
        self.leg3_away_player = leg3_away_player
        self.leg4 = leg4

        self.leg4_home_player = leg4_home_player
        self.leg4_away_player = leg4_away_player
        
        self.leg5 = leg5
        self.leg5_home_player1 = leg5_home_player1
        self.leg5_home_player2 = leg5_home_player2
        self.leg5_away_player1 = leg5_away_player1
        self.leg5_away_player2 = leg5_away_player2
        
        self.leg6 = leg6
        self.leg6_home_player1 = leg6_home_player1
        self.leg6_home_player2 = leg6_home_player2
        self.leg6_away_player1 = leg6_away_player1
        self.leg6_away_player2 = leg6_away_player2
        
        self.leg7 = leg7
        self.leg7_home_player1 = leg7_home_player1
        self.leg7_home_player2 = leg7_home_player2
        self.leg7_home_player3 = leg7_home_player3
        self.leg7_home_player4 = leg7_home_player4
        self.leg7_away_player1 = leg7_away_player1
        self.leg7_away_player2 = leg7_away_player2
        self.leg7_away_player3 = leg7_away_player3
        self.leg7_away_player4 = leg7_away_player4

        self.qp_player_h_1 = qp_player_h_1
        self.qp_player_h_2 = qp_player_h_2      
        self.qp_player_h_3 = qp_player_h_3
        self.qp_player_h_4 = qp_player_h_4
        self.qp_player_a_1 = qp_player_a_1
        self.qp_player_a_2 = qp_player_a_2
        self.qp_player_a_3 = qp_player_a_3
        self.qp_player_a_4 = qp_player_a_4