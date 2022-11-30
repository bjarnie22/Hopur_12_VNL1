from ui.admin_ui import Admin_UI
from ui.captain_ui import Captain_UI
from ui.guest_ui import Guest_UI

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
                #admin_user = Admin_UI()
                print("You pressed 1")
                #admin_user.admin_menu1()   /// Óli is currently working on this whole path
            elif command == "2":
                captain_user = Captain_UI()
                print("You pressed 2")
                captain_user.input_prompt()()
            elif command == "3":
                guest_user = Guest_UI()
                print("You pressed 3")
                guest_user.input_prompt()
            else: