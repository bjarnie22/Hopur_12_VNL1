import csv
from model.match import Match
from datetime import datetime, timedelta
import random
import math

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
        if len(update) > 1:
            for elem in update[1:]:
                self.create_match(elem)
    

    def update_result(self, match_id, match):
        """Overwrites the csv file for a chosen match, changes the final result"""
        match_list = self.get_all_matches()
    
        for elem in match_list:
            if elem.match_id == match_id:
                elem.result = match.result
                elem.winner = match.winner
                elem.home_team_legs_won = match.home_team_legs_won
                elem.away_team_legs_won = match.away_team_legs_won
                elem.round1 = match.round1
                elem.round1_home_player = match.round1_home_player
                elem.round1_away_player = match.round1_away_player
                elem.round2 = match.round2
                elem.round2_home_player = match.round2_home_player
                elem.round2_away_player = match.round2_away_player
                elem.round3 = match.round3
                elem.round3_home_player = match.round3_home_player
                elem.round3_away_player = match.round3_away_player
                elem.round4 = match.round4
                elem.round4_home_player = match.round4_home_player
                elem.round4_away_player = match.round4_away_player
                elem.round5 = match.round5
                elem.round5_home_player1 = match.round5_home_player1
                elem.round5_home_player2 = match.round5_away_player2
                elem.round5_away_player1 = match.round5_away_player1
                elem.round5_away_player2 = match.round5_away_player2
                elem.round6 = match.round6
                elem.round6_home_player1 = match.round6_home_player1
                elem.round6_home_player2 = match.round6_home_player2
                elem.round6_away_player1 = match.round6_away_player1
                elem.round6_away_player2 = match.round6_away_player2
                elem.round7 = match.round7
                elem.round7_home_player1 = match.round7_home_player1
                elem.round7_home_player2 = match.round7_home_player2
                elem.round7_home_player3 = match.round7_home_player3
                elem.round7_home_player4 = match.round7_home_player4
                elem.round7_away_player1 = match.round7_away_player1
                elem.round7_away_player2 = match.round7_away_player2
                elem.round7_away_player3 = match.round7_away_player3
                elem.round7_away_player4 = match.round7_away_player4
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
    


    def create_match(self, match, append_or_overwrite = "a"):
        """Writes into csv file all required match information"""
        match.match_id = len(self.get_all_matches())

        with open(self.file_name, append_or_overwrite, newline='', encoding="utf-8") as csvfile:

            fieldnames = ["date","home_team","away_team","result","winner","match_id","home_team_legs_won","away_team_legs_won",\
            "round1","round1_home_player","round1_away_player","round2","round2_home_player","round2_away_player","round3","round3_home_player",\
            "round3_away_player","round4","round4_home_player","round4_away_player","round5","round5_home_player1",\
            "round5_home_player2","round5_away_player1","round5_away_player2","round6","round6_home_player1",\
            "round6_home_player2","round6_away_player1","round6_away_player2","round7","round7_home_player1",\
            "round7_home_player2","round7_home_player3","round7_home_player4","round7_away_player1",\
            "round7_away_player2","round7_away_player3","round7_away_player4","qp_player_h_1","qp_player_h_2",\
            "qp_player_h_3","qp_player_h_4","qp_player_a_1","qp_player_a_2","qp_player_a_3",\
            "qp_player_a_4"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if append_or_overwrite == "w":
                writer.writeheader()
            
            writer.writerow({"date": match.date, "home_team": match.home_team, "away_team": match.away_team, "result":match.result,\
            "winner": match.winner, "match_id": match.match_id, "round1": match.round1, "round1_home_player": match.round1_home_player,\
            "home_team_legs_won": match.home_team_legs_won,"away_team_legs_won": match.away_team_legs_won,\
            "round1_away_player": match.round1_away_player, "round2": match.round2, "round2_home_player": match.round2_home_player,\
            "round2_away_player": match.round2_away_player, "round3": match.round3, "round3_home_player": match.round3_home_player,\
            "round3_away_player": match.round3_away_player, "round4": match.round4, "round4_home_player": match.round4_home_player,\
            "round4_away_player": match.round4_away_player, "round5": match.round5,"round5_home_player1": match.round5_home_player1,\
            "round5_home_player2": match.round5_home_player2, "round5_away_player1": match.round5_away_player1,\
            "round5_away_player2": match.round5_away_player2, "round6": match.round6, "round6_home_player1": match.round6_home_player1,\
            "round6_home_player2": match.round6_home_player2, "round6_away_player1": match.round6_away_player1,\
            "round6_away_player2": match.round6_away_player2, "round7": match.round7, "round7_home_player1": match.round7_home_player1,\
            "round7_home_player2": match.round7_home_player2, "round7_home_player3": match.round7_home_player3,\
            "round7_home_player4": match.round7_home_player4, "round7_away_player1": match.round7_away_player1,\
            "round7_away_player2": match.round7_away_player2, "round7_away_player3": match.round7_away_player3,\
            "round7_away_player4": match.round7_away_player4, "qp_player_h_1": match.qp_player_h_1,\
            "qp_player_h_2": match.qp_player_h_2, "qp_player_h_3": match.qp_player_h_3, "qp_player_h_4": match.qp_player_h_4,\
            "qp_player_a_1": match.qp_player_a_1,"qp_player_a_2": match.qp_player_a_2,"qp_player_a_3": match.qp_player_a_3,\
            "qp_player_a_4": match.qp_player_a_4})

    
    def get_all_matches(self):
        """Gets all matches and all information and sends it forward to the data wrapper"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                ret_list.append(Match(row["date"],row["home_team"],row["away_team"],row["result"],row["winner"],row["match_id"],\
                row["home_team_legs_won"], row["away_team_legs_won"],row["round1"],row["round1_home_player"],row["round1_away_player"],\
                row["round2"],row["round2_home_player"],row["round2_away_player"],row["round3"],row["round3_home_player"],\
                row["round3_away_player"],row["round4"],row["round4_home_player"],row["round4_away_player"],row["round5"],row["round5_home_player1"],\
                row["round5_home_player2"],row["round5_away_player1"],row["round5_away_player2"],row["round6"],\
                row["round6_home_player1"],row["round6_home_player2"],row["round6_away_player1"],row["round6_away_player2"],\
                row["round7"],row["round7_home_player1"],row["round7_home_player2"],row["round7_home_player3"],
                row["round7_home_player4"],row["round7_away_player1"],row["round7_away_player2"],row["round7_away_player3"],\
                row["round7_away_player4"],row["qp_player_h_1"],row["qp_player_h_2"],row["qp_player_h_3"],\
                row["qp_player_h_4"],row["qp_player_a_1"],row["qp_player_a_2"],row["qp_player_a_3"],row["qp_player_a_4"]))

        return ret_list

    
    def create_match_schedule(self, start_date, end_date, rounds, team_list):
        """ Create a schedule for all teams in the list"""
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")
        delta = end - start
        days = delta.days
        interval = days/(int(rounds)*(len(team_list)*(len(team_list)-1))/2)
        interval = math.ceil(interval)
        
        match_list = []

        for i in range(len(team_list)):
            for j in range(i+1, len(team_list)):
                home_team = team_list[i].team_id
                away_team = team_list[j].team_id
                match_list.append(Match("", home_team, away_team))

        random.shuffle(match_list)
        play_date = start    
        for match in match_list:
            self.create_match(Match(play_date.strftime("%d/%m/%Y"), match.home_team, match.away_team,"","",len(self.get_all_matches())))
            play_date = play_date + timedelta(days= interval)
        
        previous_list = match_list

        for i in range(int(rounds)-1):
            copy_list = []

            for match in previous_list:
                copy_list.append(Match("", match.away_team, match.home_team))

            random.shuffle(copy_list)

            for match in copy_list:
                self.create_match(Match(play_date.strftime("%d/%m/%Y"), match.home_team, match.away_team,"","",len(self.get_all_matches())))
                play_date = play_date + timedelta(days= interval)

            previous_list = copy_list


    def wipe_match_schedule(self):
        """Wipes the match schedule so that create_match_schedule can be used again correctly"""
        with open(self.file_name, "w", newline='', encoding="utf-8") as csvfile:

            fieldnames = ["date","home_team","away_team","result","winner","match_id","home_team_legs_won","away_team_legs_won",\
            "round1","round1_home_player","round1_away_player","round2","round2_home_player","round2_away_player","round3","round3_home_player",\
            "round3_away_player","round4","round4_home_player","round4_away_player","round5","round5_home_player1",\
            "round5_home_player2","round5_away_player1","round5_away_player2","round6","round6_home_player1",\
            "round6_home_player2","round6_away_player1","round6_away_player2","round7","round7_home_player1",\
            "round7_home_player2","round7_home_player3","round7_home_player4","round7_away_player1",\
            "round7_away_player2","round7_away_player3","round7_away_player4","qp_player_h_1","qp_player_h_2",\
            "qp_player_h_3","qp_player_h_4","qp_player_a_1","qp_player_a_2","qp_player_a_3",\
            "qp_player_a_4"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    
    def register_result_captain(self, match):
        """"""
        match_list = self.get_all_matches()

        for elem in match_list:
            if elem.match_id == match.match_id:
                elem.result = match.result
                elem.winner = match.winner
                elem.home_team_legs_won = match.home_team_legs_won
                elem.away_team_legs_won = match.away_team_legs_won
                elem.round1 = match.round1
                elem.round1_home_player = match.round1_home_player
                elem.round1_away_player = match.round1_away_player
                elem.round2 = match.round2
                elem.round2_home_player = match.round2_home_player
                elem.round2_away_player = match.round2_away_player
                elem.round3 = match.round3
                elem.round3_home_player = match.round3_home_player
                elem.round3_away_player = match.round3_away_player
                elem.round4 = match.round4
                elem.round4_home_player = match.round4_home_player
                elem.round4_away_player = match.round4_away_player
                elem.round5 = match.round5
                elem.round5_home_player1 = match.round5_home_player1
                elem.round5_home_player2 = match.round5_away_player2
                elem.round5_away_player1 = match.round5_away_player1
                elem.round5_away_player2 = match.round5_away_player2
                elem.round6 = match.round6
                elem.round6_home_player1 = match.round6_home_player1
                elem.round6_home_player2 = match.round6_home_player2
                elem.round6_away_player1 = match.round6_away_player1
                elem.round6_away_player2 = match.round6_away_player2
                elem.round7 = match.round7
                elem.round7_home_player1 = match.round7_home_player1
                elem.round7_home_player2 = match.round7_home_player2
                elem.round7_home_player3 = match.round7_home_player3
                elem.round7_home_player4 = match.round7_home_player4
                elem.round7_away_player1 = match.round7_away_player1
                elem.round7_away_player2 = match.round7_away_player2
                elem.round7_away_player3 = match.round7_away_player3
                elem.round7_away_player4 = match.round7_away_player4
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