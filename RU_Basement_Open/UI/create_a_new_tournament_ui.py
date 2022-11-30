class Create_a_new_tournament():
    def __init__(self):
        pass 
    
    # Here for c demand we can check if there is a ongoing tournament, then the user will get: 
    # "Sorry there can only be one tournament going on at time"

    def create_a_new_tournament_menu(self):
        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add a associations            *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)  

# Note to self, user needs to get back to create a new tournament menu when finished with one 
    def input_prompt_for_create_a_tournament(self):
        Name_of_tournament = input("Name of tournament: ")
        Starting_date_of_tournament: input("Staring date of tournament: ")
        How_many_rounds: input("How many rounds are in the tournament: ")    

        while True:
            self.create_a_new_tournament_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_associations()
            else:
                print("invalid input, please try again")


    def add_associations_menu(self):
    # Here we need to send the info about how many teams are in that association    
        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add teams                     *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)  

    def input_prompt_for_add_associations (self):
        name_of_a_association = input("Name of association: ")
        address_of_association= input("Address of {name_of_association}: ")
        phone_number_of_association: input("Phone number of {name_of_association}: ")
        number_of_teams: input("How many teams are in {}: ")
        while True:
            self.add_associations_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_teams()
            else:
                print("invalid input, please try again")

    def add_team_menu(self):
        name_of_a_association = input("Name of association: ")
        address_of_association= input("Address of {name_of_association}: ")
        phone_number_of_association: input("Phone number of {name_of_association}: ")
        number_of_teams: input("How many teams are in {}: ")
    # Here we need to send the info about how many teams are in that association    

        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add a team                    *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)
        # More simple solution would be to just trust the user that he is putting the right amount of teams. 
        # C-demand would be that the system would ask the user to put (x number of teams). For a demand we just 
        # trust the user.   
    
    def input_prompt_for_add_team (self):
        name_of_team = input("Name of team: ")
        number_of_players: input("How many players are in {name_of_team}: ")
        while True:
            self.add_a_team_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_teams()
            else:
                print("invalid input, please try again")