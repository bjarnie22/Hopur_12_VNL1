from UI.admin_ui import Admin_UI
from UI.captain_ui import Captain_UI
from UI.tournament_ui import Tournament_UI



class Main_UI:
    def __init__(self):
        print("inside main_UI")

    def menu_output(self):
        '''starting menu'''
        print("********************************************")
        print("*                   Hello!                 *")
        print("*                                          *")
        print("*             (1)   admin?                 *")
        print("*             (2) captain?                 *")
        print("*             (3)   guest?                 *")
        print("*             (q)    quit?                 *")
        print("*                                          *")
        print("********************************************")

    def input_prompt(self):
        while True:
            print ("im in the loop")
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                admin_user = Admin_UI()
                print("You pressed 1")
                admin_user.input_prompt_for_admin_menu()
            elif command == "2":
                captain_user = Captain_UI()
                print("You pressed 2")
                captain_user.input_prompt()
            elif command == "3":
                tournament = Tournament_UI()
                print("You pressed 3")
                tournament.input_prompt_for_view_tournament_main_menu()
            else:
                print("invalid input, try again!")
