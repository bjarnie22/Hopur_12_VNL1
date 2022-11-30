from tournament_ui import Tournament_ui
from create_a_new_tournament_ui import Create_a_new_tournament

class Admin_UI:
    def __init__(self):
        print("inside admin_ui")   
   
    def admin_menu(self):
        print("***********************************************")
        print("*               Hello Admin!                  *")
        print("*                                             *")
        print("*       (1)  Create a new tournament?         *")
        print("*       (2)  View tournament?*   ")
        print("*       (3)  Update a played match    *") 
        print("*       (b)  go back?                         *")
        print("*       (q)  quit?                            *")
        print("*                                             *")
        print("***********************************************")

    def input_prompt_for_admin_menu(self):
        tournament = Tournament_ui() 
        create_a_new_tournament = Create_a_new_tournament()
        while True:
            self.admin_menu1()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                create_a_new_tournament.input_prompt_for_create_a_tournament() 
                print("You pressed 1")
                
            elif command == "2":
                 print("You pressed 2")
                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")