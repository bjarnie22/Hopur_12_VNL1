import csv
from model.association import Association

class Association_data:
    def __init__(self):
        self.file_name = "files/associations.csv"

    def update():
        """Updates player information"""
        pass

    def store():
        """Adds player to csv file"""
        pass
        #id == len(self.get_all_ass)+1
    
    def get_all_associations(self):
        """Gets all teams information"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Association(row["name"], row["address"], row["phone_number"], row["association_id"]))
        return ret_list