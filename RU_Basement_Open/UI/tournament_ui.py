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
        print("****************************************************")
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
        if admin_name.isalpha() == False: 
            print("You name can only contain letters try again") 
            admin_name = input("Your Name: ")  
        admin_email = input("Your email: ")
        if ("@" in admin_email) == False: 
            print("Every email needs @ please try again")
            admin_email = input("Your email: ")
        admin_mobile = input("Your mobile phone: ")
        if admin_mobile.isnumeric() == False:
                print("Mobile phone can only contain numbers and should be at least 7 letters so try again") 
                admin_mobile = input("Your mobile phone: ")
      #  admin_social_security_number = input("Your social security number: ")
        name_of_tournament = input("Name of tournament: ")
        starting_date_of_tournament = input("Write starting date of tournament in the format dd/mm/yyyy like '12/10/2022':")
        while True: 
            if (("/" in starting_date_of_tournament) == False) or (len(starting_date_of_tournament) < 9):
                print("That was not in the format dd/mm/yyyy")
                starting_date_of_tournament = input("Write starting date of tournament in the format dd/mm/yyyy like '12/10/2022':")
                continue
            list_of_dates = starting_date_of_tournament.split("/")
            for num in list_of_dates: 
                while True:
                    try:
                        int(num)
                        break
                    except:
                        print("Dates can only be integers")
                        starting_date_of_tournament = input("Write starting date of tournament in the format dd/mm/yyyy like '12/10/2022':")
                        break
            break
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
                break
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
        while True:
            name_of_a_association = input("Name of the association: ")
            address_of_association = input("Address of association: ")
            phone_number_of_association = input("Phone number of the association: ")
#           number_of_teams = input("How many teams are in the association: ")
            new_association = Association(name_of_a_association, address_of_association, phone_number_of_association)
            self.logic_wrapper_instance.create_association(new_association)
            self.add_association_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                continue
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

            empty_space = ""
            print(f"Association id{empty_space:>10}Association name")
            for element in association_rows:
                print(f"{element.association_id:>6}{empty_space:>15}{element.name}:")
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
            number_of_players= int(input("How many players are in this team (minimun 4 players): "))    
            if number_of_players < 4: 
                print("Minimum players in a team are 4")
                number_of_players= int(input("How many players are in this team: "))    
            new_team = Team(name_of_team, association_id)
            self.logic_wrapper_instance.create_team(new_team)
            list_of_teams = self.logic_wrapper_instance.get_all_teams()
            for team in list_of_teams: 
                if team.name == new_team.name:
                    new_team.team_id = team.team_id
            for i in range(number_of_players): 
                self.input_prompt_for_add_a_player(i,new_team.team_id)
            self.add_team_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                self.add_team_menu()
            else: 
                print("Invalid input")
                
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



    def input_prompt_for_add_a_player (self, number, team_id):
# Case number 13 in the wire frame
        counter = 1
        while True:
            print("Information for Player", number, ":")
            name_of_player = input("Name of the player: ")
            email_of_the_player = input("email of the player: ")
            social_security_number = input("Players social security number: ")
            date_of_birth = input("Date of birth: ")
            address_of_player = input("Home address of player: ")
            home_phone_of_player = input("Home phone of player: ")
            mobile_phone_of_player = input("Mobile phone of player: ")
            is_this_player_the_captain = input("Write 1 if this player is the captain and 0 is this player is not the captain")
            new_player= Player(team_id,name_of_player, social_security_number, date_of_birth, email_of_the_player,address_of_player, \
            home_phone_of_player, mobile_phone_of_player)
            self.logic_wrapper_instance.create_player(new_player)
            if is_this_player_the_captain == "1":
                self.logic_wrapper_instance.choose_captain(team_id, social_security_number)
                print(f"Player {name_of_player} is now the captain")
            break
        
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
            print(f"{tournament_info_rows[0].tournament_name} by {tournament_info_rows[0].admin_name}") #prints tournament info above the associations 
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
            for t in team_rows:                         #this for loop prints out the team name and the format in which the information of the team is displayed
                if int(t.association_id) == option -1:
                    print("\n", teamcounter, f"{t.name}:","\n")
                    teamcounter += 1
                    team_array.append(t.name)
                    self.information_output(t)
                    print("{:<25}".format("Name:"),end="")
                    print("{:<20}".format("Date of birth:"),end="")
                    print("{:<20}".format("SSN:"),end="")
                    print("{:<20}".format("Email:"),end="")
                    print("{:<20}".format("Mobile:"),end="")
                    print("{:<25}".format("Address:"),end="")
                    print()
                    for p in player_rows:       #this for loop prints out each player and their information in columns
                        if p.team_id == t.team_id:
                            if p.social_security_number == t.captain_id:
                                print("{:<25}".format(f"{p.name} (C)"),end="")      #to find the captain of each team 
                                print(f"{p.date_of_birth:<20}",end="")
                                print(f"{p.social_security_number:<20}",end="")
                                print(f"{p.email:<20}",end="")
                                print(f"{p.mobile:<20}",end="")
                                print(f"{p.address:<25}",end="")
                                print()
                                #self.information_output(p)
                            else:
                                print(f"{p.name:<25}",end="")
                                print(f"{p.date_of_birth:<20}",end="")
                                print(f"{p.social_security_number:<20}",end="")
                                print(f"{p.email:<20}",end="")
                                print(f"{p.mobile:<20}",end="")
                                print(f"{p.address:<25}",end="")
                                print()
                    print()
                                #self.information_output(p)
            input("Press enter to go back ")
            break


    def information_output(self, pointer): #used for association and team information 
        print()
        try:
            print("{:<24}".format("Address:"), f"{pointer.address}")
            print("{:<24}".format("Phone number:"), f"{pointer.phone_number}")
        except:
            pass
        
    

    def list_of_upcoming_and_played_matches(self):
# Case 5 in the wire frame
        match_list = self.logic_wrapper_instance.get_all_matches()
        team_list = self.logic_wrapper_instance.get_all_teams()
        empty_space = ""
        print("All played matches:")
        print(f"{empty_space}match id{empty_space:>12}home team{empty_space:>4}away team{empty_space:>6}result\n")
        for match in match_list:
            for team in team_list:
                if team.team_id == match.home_team:
                    home = team.name
                if team.team_id == match.away_team:
                    away = team.name
            if match.result != "":
                print(f"{match.match_id:>4}{home:>25} vs {away:<15}{empty_space:>2}{match.result}")
        print()
        print("All unplayed matches:")
        print(f"{empty_space}match id{empty_space:>12}home team{empty_space:>4}away team{empty_space:>4}date\n")
        for match in match_list:
            for team in team_list:
                if team.team_id == match.home_team:
                    home = team.name
                if team.team_id == match.away_team:
                    away = team.name
            if match.result == "":
                print(f"{match.match_id:>4}{home:>25} vs {away:<15}{empty_space:>2}{match.date}")


    def input_prompt_for_list_of_upcoming_and_played_matches(self,id):
        while True:
            self.list_of_upcoming_and_played_matches()
            command = input("Press b if you would like to go back: ")

            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print("invalid input, please try again")

    def list_of_current_standing(self):
# Case 6 in the wire frame
        league_list = self.logic_wrapper_instance.get_league_standings()
        match_list = self.logic_wrapper_instance.get_all_matches()
        empty_space = ""

        print("League Standing:")
        print(f"Position{empty_space:>5}Team{empty_space:>8}Matches played{empty_space:>5}Matches won{empty_space:>3}Legs won\n")
        for team, i in zip(league_list, range(1,len(league_list)+1)):
            print(f"{i:>4}{empty_space:<5}{team[4]:<23}{team[3]:<12}{team[0]:>5}{team[1]:>14}")

    def input_prompt_for_list_of_current_standing(self,id):
        while True:
            self.list_of_current_standing()
            command = input("Enter b if you would like to go back: ")

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
