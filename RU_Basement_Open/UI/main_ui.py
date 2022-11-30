from ui.admin_ui import Admin_UI
from ui.captain_ui import Captain_UI

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
        admin_user = Admin_UI()
        captain_user = Captain_UI()

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
                #admin_user.admin_menu1()   /// Óli is currently working on this whole path
                admin_user.input_prompt()
            elif command == "2":
                 print("You pressed 2")
                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")