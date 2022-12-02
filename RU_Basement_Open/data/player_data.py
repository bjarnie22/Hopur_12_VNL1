import csv
from model.player import Player

class Player_data:
    def __init__(self):
        self.file_name = "files/players.csv"


    def create_player(self, player):
        """Adds player to csv file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["team_id", "name", "social_security_number", "date_of_birth", "email",\
            "address", "phone_number", "mobile"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"team_id": player.team_id, 'name': player.name, "social_security_number":\
            player.social_security_number, 'date_of_birth': player.date_of_birth, "email": player.email,\
            "address": player.address, "phone_number":player.phone_number, "mobile": player.mobile})


    def get_all_players(self):
        """Gets all players information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                ret_list.append(Player(row["team_id"], row["name"], row["social_security_number"],\
                row["date_of_birth"], row["email"], row["address"], row["phone_number"], row["mobile"]))
        return ret_list