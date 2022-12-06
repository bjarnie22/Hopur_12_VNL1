from UI.tournament_ui import Tournament


#Create a tournament
# View tournament
# update a match

#Update information in system """
#
#
class Admin_UI:
    def __init__(self):
        print("inside admin_ui")

    def admin_menu(self):
        print("***********************************************")
        print("*               Hello Admin!                  *")
        print("*                                             *")
        print("*       (1)  Create a new tournament?         *")
        print("*       (2)  Start a tournament               *")
        print("*       (3)  View a tournament                *")
        print("*       (4)  Edit matches                     *")
        print("*       (b)  go back?                         *")
        print("*                                             *")
        print("***********************************************")

    def input_prompt_for_admin_menu(self):
        while True:
            self.admin_menu()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                create_a_new_tournament = Tournament()
                create_a_new_tournament.input_prompt_for_create_a_tournament_menu()
                print("You pressed 1")

            elif command == "2":
                 print("You pressed 2")
                #captain_user.captain_menu1()
            elif command == "3":
                view_tournament = Tournament()
                print("You pressed 3")
                view_tournament.input_prompt_for_view_tournament_main_menu()
            elif command == "4":
                print("You pressed 4")
            elif command == "b":
                print("You are going back")
                break
            else:
                print("invalid input, please try again")
