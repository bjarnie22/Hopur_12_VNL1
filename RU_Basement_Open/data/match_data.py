import csv
from model.match import Match
from datetime import datetime, timedelta
import random

class Match_data:
    """Initializes the Match data class by getting the required file"""
    def __init__(self):
        self.file_name = "files/matches.csv"


    def postpone_match(self, match_id, date):
        """Overwrites the csv file for a chosen match, changes the date:
           postpones the match"""

        update = self.get_all_matches()

        for match in update:
            if match.match_id == match_id:
                match.date = date

        self.create_match(update[0], "w")
        try:
            for match in update[1:]:
                self.create_match(match)
        except ValueError:
            pass
    

    def update_result(self, match_id, result):
        """Overwrites the csv file for a chosen match, changes the final result"""
        match_list = self.get_all_matches()

        for match in match_list:
            if match.match_id == match_id:
                match.result = result

        self.create_match(match_list[0], "w")
        try:
            for match in match_list[1:]:
                self.create_match(match)
        except ValueError:
            pass
    


    def create_match(self, match, append_or_overwrite = "a"):
        """Writes into csv file all required match information"""
        with open(self.file_name, append_or_overwrite, newline='', encoding="utf-8") as csvfile:

            fieldnames = ["date","home_team","away_team","result","winner","match_id","leg1","leg1_home_player",\
            "leg1_away_player","leg2","leg2_home_player","leg2_away_player","leg3","leg3_home_player",\
            "leg3_away_player","leg4","leg4_home_player","leg4_away_player","leg5","leg5_home_player1",\
            "leg5_home_player2","leg5_away_player1","leg5_away_player2","leg6","leg6_home_player1",\
            "leg6_home_player2","leg6_away_player1","leg6_away_player2","leg7","leg7_home_player1",\
            "leg7_home_player2","leg7_home_player3","leg7_home_player4","leg7_away_player1",\
            "leg7_away_player2","leg7_away_player3","leg7_away_player4","qp_player_h_1","qp_player_h_2",\
            "qp_player_h_3","qp_player_h_4","qp_player_a_1","qp_player_a_2","qp_player_a_3",\
            "qp_player_a_4"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if append_or_overwrite == "w":
                writer.writeheader()
            
            writer.writerow({"date": match.date, "home_team": match.home_team, "away_team": match.away_team, "result":match.result,\
            "winner": match.winner, "leg1": match.leg1, "leg1_home_player": match.leg1_home_player,\
            "leg1_away_player": match.leg1_away_player, "leg2": match.leg2, "leg2_home_player": match.leg2_home_player,\
            "leg2_away_player": match.leg2_away_player, "leg3": match.leg3, "leg3_home_player": match.leg3_home_player,\
            "leg3_away_player": match.leg3_away_player, "leg4": match.leg4, "leg4_home_player": match.leg4_home_player,\
            "leg4_away_player": match.leg4_away_player, "leg5": match.leg5,"leg5_home_player1": match.leg5_home_player1,\
            "leg5_home_player2": match.leg5_home_player2, "leg5_away_player1": match.leg5_away_player1,\
            "leg5_away_player2": match.leg5_away_player2, "leg6": match.leg6, "leg6_home_player1": match.leg6_home_player1,\
            "leg6_home_player2": match.leg6_home_player2, "leg6_away_player1": match.leg6_away_player1,\
            "leg6_away_player2": match.leg6_away_player2, "leg7": match.leg7, "leg7_home_player1": match.leg7_home_player1,\
            "leg7_home_player2": match.leg7_home_player2, "leg7_home_player3": match.leg7_home_player3,\
            "leg7_home_player4": match.leg7_home_player4, "leg7_away_player1": match.leg7_away_player1,\
            "leg7_away_player2": match.leg7_away_player2, "leg7_away_player3": match.leg7_away_player3,\
            "leg7_away_player4": match.leg7_away_player4, "qp_player_h_1": match.qp_player_h_1,\
            "qp_player_h_2": match.qp_player_h_2, "qp_player_h_3": match.qp_player_h_3, "qp_player_h_4": match.qp_player_h_4,\
            "qp_player_a_1": match.qp_player_a_1,"qp_player_a_2": match.qp_player_a_2,"qp_player_a_3": match.qp_player_a_3,\
            "qp_player_a_4": match.qp_player_a_4, "match_id": match.match_id})

    
    def get_all_matches(self):
        """Gets all matches and all information and sends it forward to the data wrapper"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                ret_list.append(Match(row["date"],row["home_team"],row["away_team"],row["result"],row["winner"],row["match_id"],\
                row["leg1"],row["leg1_home_player"],row["leg1_away_player"],row["leg2"],row["leg2_home_player"],\
                row["leg2_away_player"],row["leg3"],row["leg3_home_player"],row["leg3_away_player"],row["leg4"],\
                row["leg4_home_player"],row["leg4_away_player"],row["leg5"],row["leg5_home_player1"],\
                row["leg5_home_player2"],row["leg5_away_player1"],row["leg5_away_player2"],row["leg6"],\
                row["leg6_home_player1"],row["leg6_home_player2"],row["leg6_away_player1"],row["leg6_away_player2"],\
                row["leg7"],row["leg7_home_player1"],row["leg7_home_player2"],row["leg7_home_player3"],
                row["leg7_home_player4"],row["leg7_away_player1"],row["leg7_away_player2"],row["leg7_away_player3"],\
                row["leg7_away_player4"],row["qp_player_h_1"],row["qp_player_h_2"],row["qp_player_h_3"],\
                row["qp_player_h_4"],row["qp_player_a_1"],row["qp_player_a_2"],row["qp_player_a_3"],row["qp_player_a_4"]))

        return ret_list

    
    def create_match_schedule(self, start_date, end_date, rounds, team_list):
        """ Create a schedule for all teams in the list"""
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")
        delta = end - start
        days = delta.days
        interval = days/((len(team_list)-1)* int(rounds))
        
        match_list = []

        for i in range(len(team_list)):
            for j in range(i+1, len(team_list)):
                home_team = team_list[i].team_id
                away_team = team_list[j].team_id
                match_list.append(Match("", home_team, away_team))

        random.shuffle(match_list)
        play_date = start    
        for match in match_list:
            self.create_match(Match(play_date, match.home_team, match.away_team,"",len(self.get_all_matches())))
            play_date = play_date + timedelta(days= interval)
        
        previous_list = match_list

        for i in range(int(rounds)-1):
            copy_list = []

            for match in previous_list:
                copy_list.append(Match("", match.away_team, match.home_team))

            random.shuffle(copy_list)

            for match in copy_list:
                self.create_match(Match(play_date, match.home_team, match.away_team,"","",len(self.get_all_matches())))
                play_date = play_date + timedelta(days= interval)

            previous_list = copy_list

    
    def register_result_captain(self, match):
        """"""
        match_list = self.get_all_matches()

        for elem in match_list:
            if elem.match_id == match_id:
                elem.result = result
                elem.winner = winner
                elem.leg1 = match.leg1
                elem.leg1_home_player = match.leg1_home_player
                elem.leg1_away_player = match.leg1_away_player
                elem.leg2 = match.leg2
                elem.leg2_home_player = match.leg2_home_player
                elem.leg2_away_player = match.leg2_away_player
                elem.leg3 = match.leg3
                elem.leg3_home_player = match.leg3_home_player
                elem.leg3_away_player = match.leg3_away_player
                elem.leg4 = match.leg4
                elem.leg4_home_player = match.leg4_home_player
                elem.leg4_away_player = match.leg4_away_player
                elem.leg5 = match.leg5
                elem.leg5_home_player1 = match.leg5_home_player1
                elem.leg5_home_player2 = match.leg5_away_player2
                elem.leg5_away_player1 = match.leg5_away_player1
                elem.leg5_away_player2 = match.leg5_away_player2
                elem.leg6 = match.leg6
                elem.leg6_home_player1 = match.leg6_home_player1
                elem.leg6_home_player2 = match.leg6_home_player2
                elem.leg6_away_player1 = match.leg6_away_player1
                elem.leg6_away_player2 = match.leg6_away_player2
                elem.leg7 = match.leg7
                elem.leg7_home_player1 = match.leg7_home_player1
                elem.leg7_home_player2 = match.leg7_home_player2
                elem.leg7_home_player3 = match.leg7_home_player3
                elem.leg7_home_player4 = match.leg7_home_player4
                elem.leg7_away_player1 = match.leg7_away_player1
                elem.leg7_away_player2 = match.leg7_away_player2
                elem.leg7_away_player3 = match.leg7_away_player3
                elem.leg7_away_player4 = match.leg7_away_player4
                elem.qp_player_h_1 = match.qp_player_h_1
                elem.qp_player_h_2 = match.qp_player_h_2
                elem.qp_player_h_3 = match.qp_player_h_3
                elem.qp_player_h_4 = match.qp_player_h_4
                elem.qp_player_a_1 = match.qp_player_a_1
                elem.qp_player_a_2 = match.qp_player_a_2
                elem.qp_player_a_3 = match.qp_player_a_3
                elem.qp_player_a_4 = match.qp_player_a_4

        self.create_match(match_list[0], "w")
        try:
            for match in match_list[1:]:
                self.create_match(match)
        except ValueError:
            pass