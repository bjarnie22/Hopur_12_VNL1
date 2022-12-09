import csv
from model.tournament import Tournament

class Tournament_data:
    """Initializes the Tournament data class by getting the required file"""
    def __init__(self):
        self.file_name = "files/tournament.csv"


    def create_tournament(self, tournament, append_or_overwrite = "a"):
        """Writes into csv file all required tournament information"""
        with open(self.file_name, append_or_overwrite, newline='', encoding="utf-8") as csvfile:

            fieldnames = ["tournament_name", "admin_name", "admin_phone", "admin_email",\
            "start_date", "end_date", "number_of_rounds", "started"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if append_or_overwrite == "w":
                writer.writeheader()

            writer.writerow({"tournament_name": tournament.tournament_name, "admin_name":\
            tournament.admin_name, "admin_phone": tournament.admin_phone, "admin_email":\
            tournament.admin_email, "start_date": tournament.start_date, "end_date": \
            tournament.end_date, "number_of_rounds": tournament.number_of_rounds, "started": tournament.started})

 
    def get_tournament_info(self):
        """Gets all tournament information, makes it a Tournament instance
           and sends it forward to the data wrapper"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: # Takes all required information and makes it into a tournament instance
                ret_list.append(Tournament(row["tournament_name"], row["admin_name"],\
                row["admin_phone"], row["admin_email"], row["start_date"], row["end_date"],\
                row["number_of_rounds"], row["started"]))
            
        return ret_list

    
    def update_end_date(self, end_date):
        """Overwrites the end date"""
        tournament = self.get_tournament_info()

        tournament.end_date = end_date
        
        self.create_tournament(tournament, "w")


    def start_tournament(self):
        """Starts tournament"""
        tournament_list = self.get_tournament_info()
        tournament = tournament_list[0]

        tournament.started = "Yes"
        
        self.create_tournament(tournament, "w")