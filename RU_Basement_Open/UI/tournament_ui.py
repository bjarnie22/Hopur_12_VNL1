from create_a_tournament_ui import Create_a_tournament
class Tournament_ui(): 

    def __init__(self):
        pass 

    
    def create_a_tournament():
        Name_of_tournament = input("Name of tournament: ")
        Starting_date_of_tournament: input("Name of tournament: ")
        How_many_rounds: input("How many rounds: ")    
        print("********************************************")
        print("*                                          *")
        print("*                                          *")
        print("*       (1)  Create associations           *")
        print("*       (b)  go back?                      *")
        print("*                                          *")
        print("********************************************")
        


    def input_prompt_for_create_a_tournament():
        while True:
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command == "1":
                create_association()
            else:
                print("invalid input, please try again")

 


    def tournament_main_menu(self):
            print("********************************************")
            print("*       Tournament main menu               *")
            print("*                                          *")
            print("*       (1)  Associations?                 *")
            print("*       (2)  View tournament?              *")
            print("*       (3)  Manage tournament?            *")
            print("*                                          *")
            print("*       (b)  go back?                      *")
            print("*       (q)  quit?                         *")
            print("*                                          *")
            print("********************************************")
            input_prompt_for_main_menu()
        # Th    is loop starts if user chooses 1. 

    def input_prompt_for_main_menu(self):

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
                associations_menu()
            elif command == "2":
                print("You pressed 2")
                view_tournament()

                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")
    
    

    def associations_menu(self): 
            print("********************************************")
            print("*              Associations                *")
            print("*                                          *")
            print("*       (1)  Add association               *")
            print("*       (2)  View and or                   *")
            print("*       update association                 *")
            print("*       (b)  go back?                      *")
            print("*       (q)  quit?                         *")
            print("*                                          *")
            print("********************************************")
            input_prompt_for_associations_menu() 

    def input_prompt_for_associations_menu(self):
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
                #create_an_association(): 
            elif command == "2":
                print("You pressed 2")
                # view_association()

                #captain_user.captain_menu1()
            elif command == "3":
                print("You pressed 2")
            else:
                print("invalid input, please try again")

    

    def create_a_teams():
        pass

    def create_a_player(): 
        pass

    def view_association():
        pass

    #Choose number of association to view: 
    #Choose a number of association to update

    def update_association(): 
        pass

    def view_tournament(): 
        print("********************************************")
        print("*               Hello!                     *")
        print("*                                          *")
        print("*       (1)  see teams and players?        *")
        print("*       (2)  see upcoming matches?         *")
        print("*       (3)  see completed matches?        *")
        print("*       (4)  see table?                    *")
        print("*       (5)  view player stats?            *")
        print("*       (6)  Update score for              *")
        print("*            a played game                 *")
        print("*       (b)  go back?                      *")
        print("*       (q)  quit?                         *")
        print("*                                          *")
        print("********************************************")

    def input_prompt_for_view_tournament(self):

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
                # see teams and players() from logic layer  
            elif command == "2":
                print("You pressed 2")
                # see upcoming matches? 
                view_tournament()
            elif command == "3":
                print("You pressed 3")
                # see_completed_matches() from logic layer
                view_tournament()
            elif command == "5":
                print("You pressed 5")
                # view player stats() from logic layer
                view_tournament()
            elif command == "6":
                print("You pressed 5")
                # Update score for a played game() from logic layer
                view_tournament()
            else:
                print("invalid input, please try again")