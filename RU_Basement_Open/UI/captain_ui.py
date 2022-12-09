from UI.tournament_ui import Tournament_UI
from UI.match_ui import Match_UI

class Captain_UI:
    def __init__(self):
        pass

    def menu_output(self):
        print("********************************************")
        print("*              Hello Captain!              *")
        print("*                                          *")
        print("*       (1)  View tournament               *")
        print("*       (2)  Add score for played game     *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")

    def input_prompt(self):
        tournament = Tournament_UI()
        match_var= Match_UI()
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
