import csv
from model.team import Team

class Team_data:
    """Initializes the Team data class by getting the required file"""
    def __init__(self):
        self.file_name = "files/teams.csv"

    
    def create_team(self, team, append_or_overwrite = "a"):
        """Writes into csv file all required team information"""
        with open(self.file_name, append_or_overwrite, newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "association_id", "captain_id", "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if append_or_overwrite == "w":
                writer.writeheader()
            writer.writerow({'name': team.name, "association_id": team.association_id,\
            "captain_id": team.captain_id, "team_id": team.team_id})


    def get_all_teams(self):
        """Gets all teams and their information, makes it a team instance
           and sends it forward to the data wrapper"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                ret_list.append(Team(row["name"], row["association_id"], row["captain_id"],\
                row["team_id"]))

        return ret_list


    def choose_captain(self, team_id, captain_id):
        """Overwrites the captain id to a acutall person, their social security number"""
        teamlist = self.get_all_teams()

        for team in teamlist:
            if team.team_id == team_id:
                team.captain_id = captain_id
        
        self.create_team(teamlist[0], "w")
        try:
            for team in teamlist[1:]: # overwrites the file with the updated information
                self.create_team(team, "a")
        except:
            pass