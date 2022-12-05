import csv
from model.match import Match

class Match_data:
    """Initializes the Match data class by getting the required file"""
    def __init__(self):
        self.file_name = "files/matches.csv"


    def postpone_match(self, match_id, date):
        pass
        """Overwrites the csv file for a chosen match, changes the date:
           postpones the match"""

        update = self.get_all_matches()

        for match in update:
            if match.match_id == match_id:
                match.date = date

        self.create_match(update[0], "w")
        try:
            for match in update[1:]:
                create_match(match)
        except ValueError:
            pass
    

    def update_result(self, match_id, result):
        """Overwrites the csv file for a chosen match, changes the final result"""
        update = self.get_all_matches()

        for match in update:
            if match.match_id == match_id:
                match.result = result

        self.create_match(update[0], "w")
        try:
            for match in update[1:]:
                create_match(match)
        except ValueError:
            pass


    def create_match(self, match, append_or_overwrite = "a"):
        """Writes into csv file all required match information"""
        with open(self.file_name, append_or_overwrite, newline='', encoding="utf-8") as csvfile:

            fieldnames = ["date","home_team","away_team","result","match_id","leg1","leg1_home_player",\
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
            
            writer.writerow({"date": match.date, "home_team": match.home_team, "away_team": match.away_team,\
             "result": match.result, "leg1": match.leg1, "leg1_home_player": match.leg1_home_player,\
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
                ret_list.append(Match(row["date"],row["home_team"],row["away_team"],row["result"],row["match_id"],\
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