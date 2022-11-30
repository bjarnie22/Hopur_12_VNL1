import csv
from model.tournament import Tournament

class Tournament_data:
    def __init__(self):
        self.file_name = "files/tournament.csv"

    def update():
        """Updates player information"""
        pass

    def store():
        """Adds player to csv file"""
        pass
    
    def get_tournament_info(self):
        """Gets all tournament information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tournament(row["tournament_name"], row["admin_name"], row["admin_phone"], row["admin_email"]))
        return ret_list