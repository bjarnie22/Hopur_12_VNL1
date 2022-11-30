import csv
from model.team import Team

class Team_data:
    def __init__(self):
        self.file_name = "files/teams.csv"

    def update():
        """Updates player information"""
        pass
    
    def store():
        """Adds player to csv file"""
        pass

    def get_all_teams(self):
        """Gets all teams information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row["name"], row["players"], row["team_id"], row["association_id"] ))
        return ret_list