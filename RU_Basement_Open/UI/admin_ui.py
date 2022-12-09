from UI.tournament_ui import Tournament_UI
from UI.match_ui import Match_UI
from logic.logic_wrapper import Logic_Wrapper


#Create a tournament
# View tournament
# update a match

#Update information in system """
#
#
class Admin_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()
        tournament = self.logic_wrapper.get_tournament_info()
        if len(tournament) == 0:
            self.started = "No tournament created"
        else:
            self.started = tournament[0].started

    def admin_menu(self):
        print("***********************************************")
        print("*               Hello Admin!                  *")
        print("*                                             *")
        if self.started == "No tournament created":
            print("*       (1)  Create a new tournament          *")
        if self.started == "No":
            print("*       (1)  Manage tournament                *")
            print("*       (2)  Start a tournament               *")
        if self.started == "Yes":
            print("*       (1)  View a tournament                *")
            print("*       (2)  Update a score for a match       *")
            print("*       (3)  Change date for a match          *")
        print("*       (b)  go back?                         *")
        print("*                                             *")
        print("***********************************************")


    def input_prompt_for_admin_menu(self):
        tournament = Tournament_UI()
        match_var = Match_UI()
        while True:
            self.admin_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            if self.started == "No tournament created":
                if command == "1":
                    print("You pressed 1")
                    tournament.input_prompt_for_create_a_tournament_menu()
                    break
                elif command == "b":
                    print("you are going back")
                    break
                else:
                    print("invalid input, please try again")
            elif self.started == "No":
                if command == "1":
                    print("You pressed 1")
                    tournament.input_prompt_for_manage_tournament_main_menu()
                elif command == "2":
                    print("You pressed 2")
                    tournament.input_prompt_for_the_calculated_schedule_of_the_matches()
                    break
                elif command == "b":
                    print("you are going back")
                    break
                else:
                    print("invalid input, please try again")
            elif self.started == "Yes":
                if command == "1":
                    print("You pressed 1")
                    tournament.input_prompt_for_view_tournament_main_menu()
                elif command == "2":
                    print("You pressed 2")
                    match_var.choose_match_id_admin()
                elif command == "3":
                    print("You pressed 3")
                    match_var.choose_match_id_to_change_a_date_for_a_match()
                elif command == "b":
                    print("you are going back")
                    break
                else:
                    print("invalid input, please try again")
