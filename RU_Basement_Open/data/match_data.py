import csv
from model.match import Match

class Match_data:
    def __init__(self):
        self.file_name = "files/matches.csv"


    def postpone_match(self, match_id, date):
        pass
        """Updates player information"""

        update = self.get_all_matches()
        clean_csv(self.file_name)

        for match in update:
            if match.match_id == match_id:
                match.date = date

        for match in update:
            create_match(match)
    

    def update_score(self, match_id, score):
        pass
        """Updates player information"""
        update = self.get_all_matches()
        delete_file()

        for match in update:
            if match.match_id == match_id:
                match.score = score

        for match in update:
            create_match(match)


    def create_match(self, match):
        pass
        """Adds match to csv file"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({})

    
    def get_all_matches(self):
        pass
        """Gets all matches and all information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append()
        return ret_list