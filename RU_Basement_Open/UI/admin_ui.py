from UI.tournament_ui import Tournament_UI
from UI.match_ui import Match


#Create a tournament
# View tournament
# update a match

#Update information in system """
#
#
class Admin_UI:
    def __init__(self):
        pass

    def admin_menu(self):
        print("***********************************************")
        print("*               Hello Admin!                  *")
        print("*                                             *")
        print("*       (1)  Create a new tournament?         *")
        print("*       (2)  Start a tournament               *")
        print("*       (3)  View a tournament                *")
        print("*       (4)  Update a score for a  matches    *")
        print("*       (5)  Change date for a  match         *")
        print("*       (b)  go back?                         *")
        print("*                                             *")
        print("***********************************************")


    def input_prompt_for_admin_menu(self):
        tournament = Tournament_UI()
        match_var= Match_UI()
        while True:
            self.admin_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                print("You pressed 1")
                tournament.input_prompt_for_create_a_tournament_menu()
            elif command == "2":
                 print("You pressed 2")
                 tournament.input_prompt_for_the_calculated_schedule_of_the_matches()
            elif command == "3":
                print("You pressed 3")
                tournament.input_prompt_for_view_tournament_main_menu()
            elif command == "4":
                print("You pressed 4")
                match_var.choose_match_id()
            elif command == "5":
                print("You pressed 5")
                match_var.choose_match_id_to_change_a_date_for_a_match()
            elif command == "b":
                print("You are going back")
                break
            else:
                print("invalid input, please try again")
