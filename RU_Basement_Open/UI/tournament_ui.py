from data.association_data import Association_data
from data.team_data import Team_data
from data.player_data import Player_data
from data.tournament_data import Tournament_data

class Tournament():
    def __init__(self):
        pass


############################# Create a tournament case number 8 in the wire frame###############################
#################################################################################################################

    def create_a_tournament_menu(self):
#Case number 8 in the wire frame
        print("****************************************************")
        print("*                                                  *")
        print("*       (1)  Add an association                    *")
        print("*       (b)  go back?                              *")
        print("*                                                  *")
        print("****************************************************")

    def input_prompt_for_create_a_tournament_menu(self):
        admin_name = input("Your Name: ")
        admin_email = input("Your email: ")
        admin_mobile = input("Your mobile phone: ")
        admin_social_security_number = input("Your social security number: ")
        name_of_tournament = input("Name of tournament: ")
        starting_date_of_tournament = input("Starting date of tournament: ")
        end_date_of_tournament = input("Ending date of tournament: ")
        how_many_rounds = input("How many rounds are in the tournament: ")
        while True:
            self.create_a_tournament_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                name_of_a_association = input("Name of the association: ")
                address_of_association = input("Address of association: ")
                phone_number_of_association = input("Phone number of the association: ")
                number_of_teams = input("How many teams are in the association: ")
                self.input_prompt_for_add_association()
            else:
                print("invalid input, please try again")


    def add_association_menu(self):
# Case number 11 in the wire frame
        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add team                      *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        # Here this function will return the(Name_of_tournament  Starting_date_of_tournament, How_many_rounds)


    def input_prompt_for_add_association (self):

        while True:
            self.add_association_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                name_of_team = input("Name of team: ")
                while True:
                    try:
                        number_of_players = int(input("How many players are in this team: "))
                        break
                    except:
                        print("invalid input, please try again")
                self.input_prompt_for_add_a_player(number_of_players)
            else:
                print("invalid input, please try again")

    def add_player_menu(self):
# Case number 12 in the wire frame

        print("********************************************")
        print("*                                          *")
        print("*       (1)  Add a player                  *")
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
                self.input_prompt_for_list_of_associations_and_their_teams()
            elif command == "2":
                self.input_prompt_for_list_of_upcoming_and_played_matches(id)
            elif command == "3":
                self.input_prompt_for_list_of_current_standing(id)
            else:
                print("invalid input, please try again")


    def list_of_associations_and_their_teams(self):
# Case 3 in the wire frame
            # Here we would need a list of teams, to which association they belong to
            # and list of players.
            counter = 1
            association_list = Association_data()
            association_rows = association_list.get_all_associations()
            for element in association_rows:
                print(counter, element)
                counter += 1
            which_association = input("which association would you like to check out? To go back press b ")
            if which_association == "b":
                self.input_prompt_for_view_tournament_main_menu()
            team_list = Team_data()
            all_teams = team_list.get_all_teams()
            team_array = []
            for i in range(0, counter):
                if which_association == "i":
                    for element in all_teams:
                        if element == "associiation_id":
                            team_array.append(element)
            print(team_array.merged())
            """!!!kodinn her fyrir ofan tharf ad vera vel skodadur bara ovirk
            beinagrind af thvi veit ekki hvernig a ad prufa hann vegna gagnaleysis!!!"""


    def input_prompt_for_list_of_associations_and_their_teams(self):
        while True:
            self.list_of_associations_and_their_teams()
            command = input("Enter the id of the team you would like to view and b if you would like to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                self.input_prompt_for_list_of_players(command)
                # Here we need to check if the id is valid or not.

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
            command = input("Enter the id of the player you would like to view and q if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print("invalid input, please try again")

    def list_of_current_standing():
# Case 6 in the wire frame
        pass

    def input_prompt_for_list_of_current_standing(self,id):
        while True:
            self.list_of_current_standing()
            command = input("Enter the id of the player you would like to view and q if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print("invalid input, please try again")




########################################################################################################

########################################################################################################
