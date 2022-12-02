class Tournament():
    def __init__(self):
        pass 
    
    # Here for c demand we can check if there is a ongoing tournament, then the user will get: 
    # "Sorry there can only be one tournament going on at time"
    def create_a_tournament_menu(self):
        print("****************************************************")
        print("*                                                  *")
        print("*       (1)  Add a association                     *")
        print("*       (b)  go back?                              *")
        print("*                                                  *")
        print("****************************************************")
   
    def input_prompt_for_create_a_tournament_menu(self): 
        name_of_tournament = input("Name of tournament: ")
        starting_date_of_tournament: input("Starting date of tournament: ")
        end_date_of_tournament: input("Ending date of tournament: ")
        how_many_rounds: input("How many rounds are in the tournament: ")    
        while True:
            self.tournament_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_association()
            else:
                print("invalid input, please try again")


    def add_association_menu(self):
    # Here we need to send the info about how many teams are in that association    
        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add team                      *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)  

    def input_prompt_for_add_association (self):
        name_of_a_association = input("Name of the association: ")
        address_of_association= input("Address of association: ")
        phone_number_of_association: input("Phone number of the association: ")
        number_of_teams: input("How many teams are in the association: ")
        while True:
            self.add_association_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_team()
            else:
                print("invalid input, please try again")

    def add_team_menu(self):
    # Here we need to send the info about how many teams are in that association    

        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add a player                  *")
        print("* If you have added all the associations,  *")
        print("* teams and players.                        *") 
        print(" You should now schedule matches            *") 
        print("*       (2)  Schedule matches              *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)
        # More simple solution would be to just trust the user that he is putting the right amount of teams. 
        # C-demand would be that the system would ask the user to put (x number of teams). For a demand we just 
        # trust the user.   
    
    def input_prompt_for_add_team (self):
        name_of_team = input("Name of team: ")
        number_of_players: input("How many players are in this teams: ")
        while True:
            self.add_team_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_a_player()
            else:
                print("invalid input, please try again")
    
    def input_prompt_for_add_a_player (self):
        name_of_player = input("Name of the player: ")
        social_security_number: input("Players social security number: ")
        date_of_birth = input("Date of birth: ")
        address_of_player = input("Home address of player: ") 
        home_phone_of_player = input("Home phone of player: ")
        mobile_phone_of_player = input("Mobile phone of player: ")
        is_this_player_the_captain = input("""This is player the captain? 
        Write "yes" if this player is the captain. Please leave empty if this player is not the captain: """)

        while True:
            self.add_team_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_add_teams()
            else:
                print("invalid input, please try again")
    

    def input_prompt_for_schedule_matches(self):
        # Here we need to get a function that calculates the number of teams and number of rounds. And also 
        # Here we would need to error check that all teams are playing equally. 
        # Each match would need an id name? For the match class to function. 
        pass

########################################################################################################

    def view_tournament_main_menu(self):
            print("*************************************************************")
            print("*                   View tournament                         *")
            print("*                                                           *")
            print("*       (1)  List of teams, their players info and stat     *")
            print("*       (2)  List of upcoming and played matches            *")
            print("*       (2)  List of current standing                       *")
            print("*       (b)  go back?                                       *")
            print("*                                                           *")
            print("*                                                           *")
            print("*************************************************************")
    
    def input_prompt_for_view_tournament_main_menu(self):
        while True:
            self.view_tournament_main_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.input_prompt_for_list_of_teams()
            else:
                print("invalid input, please try again")
    
                
    def list_of_teams(self):
            # Here we would need a list of teams, to which association they belong to 
            # and list of players. 
            pass
    
    def input_prompt_for_list_of_teams(self):
        while True:
            self.list_of_teams()
            command = input("Enter the id of the team you would like to view and b if you would like to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                self.input_prompt_for_list_of_players(command)
                # Here we need to check if the id is valid or not. 

    def list_of_players(self):
            # Here we would need a list of players for a choosen team. 
            pass
    
    def input_prompt_for_list_of_players(self,id):
        while True:
            self.list_of_players()
            command = input("Enter the id of the player you would like to view and q if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                self.input_prompt_for_a_single_player_and_info(command)
                # Here we need to check if the id is valid or not. 
                print("invalid input, please try again")
                print("invalid input, please try again")

    def a_single_player_info_and_stats(self):
        # Here we would need public information of a player for a chosen team. 
        pass
    
    
    def input_prompt_for_a_single_player_and_info(self):
        while True:
            self.a_single_player_info_and_stats()
            command = input("Enter any key to back: ")
            command = command.lower()
            if command:
                break

########################################################################################################    
    def input_prompt_for_main_menu(self):

        while True:
            self.tournament_main_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                print("You pressed 1")
                self.input_prompt_for_associations_menu()
            elif command == "2":
                print("You pressed 2")
                view_tournament()

                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")
    
    
    def associations_menu(self): 
            print("********************************************")
            print("*              Associations                *")
            print("*                                          *")
            print("*       (1)  Add association               *")
            print("*       (2)  View and or                   *")
            print("*       update association                 *")
            print("*       (b)  go back?                      *")
            print("*                                          *")
            print("********************************************")
            input_prompt_for_associations_menu() 

    def input_prompt_for_associations_menu(self):
        add_association = Create_a_new_tournament()
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                add_association.input_prompt_for_add_association()
            elif command == "2":
                print("You pressed 2")
                # view_association()

                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")

    

    def create_a_teams():
        pass

    def create_a_player(): 
        pass

    def view_association():
        pass

    #Choose number of association to view: 
    #Choose a number of association to update

    def update_association(): 
        pass

    def view_tournament(): 
        print("********************************************")
        print("*               Hello!                     *")
        print("*                                          *")
        print("*       (1)  see teams and players?        *")
        print("*       (2)  see upcoming matches?         *")
        print("*       (3)  see completed matches?        *")
        print("*       (4)  see table?                    *")
        print("*       (5)  view player stats?            *")
        print("*       (b)  go back?                      *")
        print("*       (q)  quit?                         *")
        print("*                                          *")
        print("********************************************")

    def input_prompt_for_view_tournament(self):

        while True:
            print ("im in the loop")
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                print("You pressed 1")
                # see teams and players() from logic layer  
            elif command == "2":
                print("You pressed 2")
                # see upcoming matches? 
                view_tournament()
            elif command == "3":
                print("You pressed 3")
                # see_completed_matches() from logic layer
                view_tournament()
            elif command == "5":
                print("You pressed 5")
                # view player stats() from logic layer
                view_tournament()
            elif command == "6":
                print("You pressed 5")
                # Update score for a played game() from logic layer
                view_tournament()
            else:
                print("invalid input, please try again")
