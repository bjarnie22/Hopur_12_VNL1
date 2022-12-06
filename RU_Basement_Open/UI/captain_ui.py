from UI.tournament_ui import Tournament
from UI.match_ui import Match

class Captain_UI:
    def __init__(self):
        print("inside captain_ui")

    def menu_output(self):
        print("********************************************")
        print("*               Hello Captain!             *")
        print("*                                          *")
        print("*       (1)  View tournament               *")
        print("*       (2)  Add score for played game     *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")

    def input_prompt(self):
        tournament = Tournament()
        match_var= Match()
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                print("You pressed 1")
                tournament.input_prompt_for_view_tournament_main_menu()
            elif command == "2":
                print("You pressed 2")
                match_var.choose_match_id_captain()
            else:
                print("invalid input, please try again")
