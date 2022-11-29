from admin_ui import Admin_UI

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
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                break
            elif command == "1":
                admin_menu1()
            elif command == "2":
                pass
            elif command == "3":
                pass
            else:
                print("invalid input, please try again")

