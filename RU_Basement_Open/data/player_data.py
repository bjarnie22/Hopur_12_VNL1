import os
import csv
from model.player import Player

class Player_data:
    def __init__(self):
        self.file_name = "RU_Basement_Open/files/players.csv"

    def update():
        """Updates player information"""
        pass
    
    def store():
        """Adds player to csv file"""
        pass

    def read_all_player():
        """Gets all players information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row["name"], row["date_of_birth"], row["address"], row["email"], row["phone_number"], row["social_security_number"], row["team_id"]))
        return ret_list