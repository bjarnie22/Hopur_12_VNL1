from data.association_data import Association_data
from data.team_data import Team_data
from data.player_data import Player_data
from data.tournament_data import Tournament_data
from logic.logic_wrapper import Logic_Wrapper
from model.player import Player
from model.team import Team
from model.association import Association
from model.tournament import Tournament
from model.match import Match

class Tournament_UI():
    def __init__(self):
        self.logic_wrapper_instance = Logic_Wrapper()


############################# Create a tournament case number 8 in the wire frame###############################
#################################################################################################################

  
    def create_a_tournament_menu(self, admin_name):
#Case number 8 in the wire frame
        print("************** **************************************")
        print(f"*               Welcome {admin_name}              *")
        print("*       First you should add all associations      *") 
        print("*       then you should add teams and players      *")
        print("*       (1)  To add the first association          *")                         
        print("*                                                  *")
        print("*       (b)  go back?                              *")
        print("*                                                  *")
        print("****************************************************")

    def input_prompt_for_create_a_tournament_menu(self):
        admin_name = input("Your Name: ")
        admin_email = input("Your email: ")
        admin_mobile = input("Your mobile phone: ")
      #  admin_social_security_number = input("Your social security number: ")
        name_of_tournament = input("Name of tournament: ")
        starting_date_of_tournament = input("Starting date of tournament: ")
        end_date_of_tournament = input("Ending date of tournament: ")
        how_many_rounds = input("How many rounds are in the tournament: ")
        new_tournament = Tournament(name_of_tournament, admin_name, admin_mobile,admin_email,starting_date_of_tournament,end_date_of_tournament,how_many_rounds)
        self.logic_wrapper_instance.create_tournament(new_tournament) 
        new_tournament.admin_name
        while True:
            self.create_a_tournament_menu(new_tournament.admin_name)
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
# Case number 11 in the wire frame
        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add another association       *")
        print("*       (2)  Start add the first team      *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)

    def input_prompt_for_add_association (self):
        name_of_a_association = input("Name of the association: ")
        address_of_association = input("Address of association: ")
        phone_number_of_association = input("Phone number of the association: ")
#        number_of_teams = input("How many teams are in the association: ")
        new_association = Association(name_of_a_association, address_of_association, phone_number_of_association)
        self.logic_wrapper_instance.create_association(new_association)
        while True:
            self.add_association_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.add_association_menu
            elif command == "2":
                self.input_prompt_to_add_a_team ()
            else:
                print("invalid input, please try again")
 
    def print_list_of_associations(self): 
            all_lists = Logic_Wrapper()
            association_rows = all_lists.get_all_associations()
            team_rows = all_lists.get_all_teams()
            player_rows = all_lists.get_all_players()
            tournament_info_rows = all_lists.get_tournament_info()
            associations = []
            ass_pointer = []
            print()
            print(f"{tournament_info_rows[0].tournament_name} by {tournament_info_rows[0].admin_name}")
            print()
            print("All associations:")
            print()
            for i in range(35):
                print("-",end='')
            print()
            counter = 1

            for element in association_rows:
                print(f"{element.association_id}   {element.name}:")
                counter += 1
                associations.append(element.name)
                ass_pointer.append(element)
            for i in range(35):
                print("-",end='')
           
            print()

    def input_prompt_to_add_a_team (self):
        while True:
            name_of_team = input("Name of team: ")
            self.print_list_of_associations()
            association_id = input("Choose the association id that this teams belongs to: ")
            number_of_players= int(input("How many players are in this team: "))    
            self.logic_wrapper_instance.create_team(name_of_team, association_id)
            self.input_prompt_for_add_a_player(number_of_players)
            self.add_team_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.add_team_menu()
                
            #else:
             #   print("invalid input, please try again")"""
    def add_team_menu(self):
# Case number 12 in the wire frame
        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add another team             *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)
        # More simple solution would be to just trust the user that he is putting the right amount of teams.
        # C-demand would be that the system would ask the user to put (x number of teams). For a demand we just
        # trust the user.



    def input_prompt_for_add_a_player (self, number):
# Case number 13 in the wire frame
        self.add_player_menu()
        command = input("Enter your command: ")
        command = command.lower()
        if command == "b":
            print("you are going back")
            self.input_prompt_for_add_association()
        elif command == "1":
            counter = 1
            for i in range(0, number):
                print("Information for Player", counter, ":")
                name_of_player = input("Name of the player: ")
                email_of_the_player = input("email of the player: ")
                social_security_number = input("Players social security number: ")
                date_of_birth = input("Date of birth: ")
                address_of_player = input("Home address of player: ")
                home_phone_of_player = input("Home phone of player: ")
                mobile_phone_of_player = input("Mobile phone of player: ")
                is_this_player_the_captain = input("""Is this player the captain?
                Write "yes" if this player is the captain. Please leave empty if this player is not the captain: """)
                counter += 1
            self.input_prompt_for_add_association()
        else:
            print("invalid input, please try again")

############################## View tournament case 2 in the wire frame#############################################
# ###################################################################################################################

    def view_tournament_main_menu(self):
# Case number 2 in the wire frame
            print("*************************************************************")
            print("*                   View tournament                         *")
            print("*                                                           *")
            print("*       (1)  List of associations and their teams.          *")
            print("*       (2)  List of upcoming and played matches            *")
            print("*       (3)  List of current standing                       *")
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
                self.list_of_associations_and_their_teams()
            elif command == "2":
                self.input_prompt_for_list_of_upcoming_and_played_matches(id)
            elif command == "3":
                self.input_prompt_for_list_of_current_standing(id)
            else:
                print("invalid input, please try again")


    def list_of_associations_and_their_teams(self):
# Case 3 in the wire frame
            # Here we would need a list of teams, to which association they belong to
            # and list of players
        while True:
            all_lists = Logic_Wrapper()
            association_rows = all_lists.get_all_associations()
            team_rows = all_lists.get_all_teams()
            player_rows = all_lists.get_all_players()
            tournament_info_rows = all_lists.get_tournament_info()
            associations = []
            ass_pointer = []


            print()
            print(f"{tournament_info_rows[0].tournament_name} by {tournament_info_rows[0].admin_name}")
            print()
            print("All associtaions:")
            print()
            for i in range(35):
                print("-",end='')
            print()
            counter = 1

            for element in association_rows:
                print(counter, f"{element.name}:")
                counter += 1
                associations.append(element.name)
                ass_pointer.append(element)
            for i in range(35):
                print("-",end='')
            print()

            while True:
                which_association = input("which association would you like to check out? To go back press b ")
                if which_association == "1":
                    print()
                    break
                elif which_association == "2":
                    print()
                    break
                elif which_association == "3":
                    print()
                    break
                if which_association == "b":
                    print()
                    break
                else:
                    print("Invalid input!")

            if which_association == "b":
                break
            self.output_for_associations_and_their_teams(int(which_association), associations, ass_pointer)




    def output_for_associations_and_their_teams(self,option,list,pointer):
        while True:
            all_lists = Logic_Wrapper()
            association_rows = all_lists.get_all_associations()
            team_rows = all_lists.get_all_teams()
            player_rows = all_lists.get_all_players()
            tournament_info_rows = all_lists.get_tournament_info()
            team_array = []
            teamcounter = 1
            print(list[option -1],":")
            self.information_output(pointer[option -1])
            for t in team_rows:
                if int(t.association_id) == option -1:
                    print(teamcounter, f"{t.name}:")
                    teamcounter += 1
                    team_array.append(t.name)
                    self.information_output(t)
                    for p in player_rows:
                        if p.team_id == t.team_id:
                            if p.social_security_number == t.captain_id:
                                print(f"{p.name:<25} (C)",end="\n")
                                self.information_output(p)
                            else:
                                print(f"{p.name:<25}",end="\n")
                                self.information_output(p)
            input("Press enter to go back ")
            break


    def information_output(self, pointer):
        print()
        try:
            print("{:<25}".format("Address:"), f"{pointer.address}")
            print("{:<25}".format("Phone number:"), f"{pointer.phone_number}")
        except:
            print("{:<25}".format("Captain ID:"), f"{pointer.captain_id}", "\n")

        try:
            print("{:<25}".format("Date of birth:"), f"{pointer.date_of_birth}")
            print("{:<25}".format("SSN:"), f"{pointer.social_security_number}")
            print("{:<25}".format("Email:"), f"{pointer.email}")
            print("{:<25}".format("Mobile:"), f"{pointer.mobile}")
            print()
            print()
        except:
            print('')


    def list_of_players_for_a_chosen_team(self):
        pass
# Case 4 in the wire frame
            # Here we would need a list of players for a choosen team.


    def input_prompt_for_list_of_players(self,id):
        while True:
            self.list_of_players_for_a_choose_team()
            command = input("Enter the id of the player you would like to view and q if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print("invalid input, please try again")

    def list_of_upcoming_and_played_matches(self):
# Case 5 in the wire frame
        pass

    def input_prompt_for_list_of_upcoming_and_played_matches(self,id):
        while True:
            self.list_of_upcoming_and_played_matches()
            command = input("Enter the id of the player you would like to view and b if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print("invalid input, please try again")

    def list_of_current_standing(self):
# Case 6 in the wire frame
        pass

    def input_prompt_for_list_of_current_standing(self,id):
        while True:
            self.list_of_current_standing()
            command = input("Enter the id of the player you would like to view and b if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print("invalid input, please try again")


#################################Start a tournament case 9 in the wire frame##########################################
########################################################################################################

    def the_calculated_schedule_of_the_matches(self):
# Case 9 in the wire frame
        # Here should come calculated schedule of the mathces.
        pass

    def input_prompt_for_the_calculated_schedule_of_the_matches(self):
        while True:
            self.the_calculated_schedule_of_the_matches()
            command = input("Enter the 1 if you want shorten or lengthen the match or press 'b' to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.change_date_of_tournament()
            else:
                print("invalid input, please try again")

    def change_date_of_tournament(self):
        while True:
            new_starting_date = input("Enter the new starting date or 'b' to go back, if you press b no changes will be made: ")
            new_starting_date = new_starting_date.lower()
            if new_starting_date == "b":
                print("you are going back")
                break
            else:
                # updates the new starting date
                 print ("Here we will check the input")
                 break

        while True:
            new_ending_date = input("Enter the new ending date or 'b' to go back if you press b no changes will be made: ")
            new_ending_date = new_ending_date.lower()
            if new_ending_date == "b":
                print("you are going back")
                break
            else:
                 print ("Here we will check the input")
                 break
