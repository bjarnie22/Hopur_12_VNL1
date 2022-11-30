from tournament_ui import Tournament_ui

class Admin_UI:
    def __init__(self):
        print("inside admin_ui")   
   
    def admin_menu1(self):
        print("********************************************")
        print("*               Hello Admin!               *")
        print("*                                          *")
        print("*       (1)  Create a new tournament?      *")
        print("*       (2)  Continue with your tournament?*")
        print("*       (3)  See current tournament info   *") 
        print("*       (b)  go back?                      *")
        print("*       (q)  quit?                         *")
        print("*                                          *")
        print("********************************************")
        input_prompt_for_admin_menu1()

    def input_prompt_for_admin_menu1(self):
   
        while True:
            print ("im in the loop")
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                print("You pressed 1")
                #admin_user.admin_menu1()
            elif command == "2":
                 print("You pressed 2")
                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")