import csv
from model.player import Player

class Player_data:
    def __init__(self):
        self.file_name = "files/players.csv"


    def update():
        """Updates player information"""
        pass
    

    def create_player(self, player):
        """Adds player to csv file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "date_of_birth","address", "email", "phone_number", "social_security_number", "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': player.name, 'date_of_birth': player.date_of_birth, "address": player.address, "email": player.email, "phone_number":player.phone_number, "social_security_number": player.social_security_number, "team_id": player.team_id})


    def get_all_players(self):
        """Gets all players information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row["name"], row["date_of_birth"], row["address"], row["email"], row["phone_number"], row["social_security_number"], row["team_id"]))
        return ret_list