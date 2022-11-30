import csv
from model.team import Team

class Team_data:
    def __init__(self):
        self.file_name = "files/teams.csv"

    def update():
        """Updates player information"""
        pass
    
    def create_team(self, team):
        """Adds team to csv file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "association_id", "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': team.name, "association_id": team.association_id, "team_id": team.team_id})


    def get_all_teams(self):
        """Gets all teams information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row["name"], row["association_id"], row["team_id"]))
        return ret_list