import csv
from model.association import Association

class Association_data:
    """Initializes the Association data class by getting the required file"""
    def __init__(self):
        self.file_name = "files/associations.csv"


    def create_association(self, association):
        """Writes into csv file all required association information"""
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "address", "phone_number","association_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': association.name, "address": association.address,\
            "phone_number": association.phone_number, "association_id": association.association_id})


    def get_all_associations(self):
        """Gets all associations and their information, makes it a asssociations instances
           and sends it forward to the data wrapper"""
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Association(row["name"], row["address"], row["phone_number"],\
                row["association_id"]))
        return ret_list