import csv
from model.tournament import Tournament

class Tournament_data:
    def __init__(self):
        self.file_name = "files/tournament.csv"


    def create_tournament(self, tournament):
        """Adds tournament to csv file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:

            fieldnames = ["tournament_name", "admin_name", "admin_phone", "admin_email",\
            "start_date", "end_date", "number_of_rounds"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({"tournament_name": tournament.tournament_name, "admin_name":\
            tournament.admin_name, "admin_phone": tournament.admin_phone, "admin_email":\
            tournament.admin_email, "start_date": tournament.start_date, "end_date": \
            tournament.end_date, "number_of_rounds": tournament.number_of_rounds})

 
    def get_tournament_info(self):
        """Gets all tournament information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tournament(row["tournament_name"], row["admin_name"],\
                row["admin_phone"], row["admin_email"], row["start_date"], row["end_date"],\
                row["number_of_rounds"]))
            
        return ret_list