class Captain_UI:
    def __init__(self):
        print("inside captain_ui")

    def menu_output(self):
            print("********************************************")
            print("*               Hello Guest!               *")
            print("*                                          *")
            print("*       (1)  see teams and players?        *")
            print("*       (2)  see upcoming matches?         *")
            print("*       (3)  see completed matches?        *")
            print("*       (4)  see table?                    *")
            print("*       (5)  view player stats?            *")
            print("*       (6)  add score for played game     *")
            print("*                                          *")
            print("*       (b)  go back?                      *")
            print("*       (q)  quit?                         *")
            print("*                                          *")
            print("********************************************")

    def input_prompt(self):
        while True:
            print ("im in the captain loop")
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("you are quitting the program")
                return "q"

            elif command == "b":
                print("you are going back")
                return "b"

            elif command == "1":
                print("You pressed 1")
                #myndi prenta alla öll lið eftir team ID
                #myndi prenta leikmenn með sama ID
            
            elif command == "2":
                print("You pressed 2")
                #myndi prenta viðureignir liðana

            elif command == "3":
                print("you pressed 3")
                #myndi prenta niðurstöður fyrverandi viðureigna
            
            elif command == "4":
                print("You pressed 4")
                #myndi prenta stöðu mótsins

            #elif command == "5": = B krafa
                #print("you pressed 5")
                #myndi prenta stöðuna í mótinu

            elif command == 6:
                print("you pressed 6")
                #myndi koma input

                #A-Kröfur:
                #stig fyrir liðin sem voru að spila

                #B-kröfur
                #Stig fyrir leikmenn
                #QP fyrir leikmenn
                #Inner fyrir leikmenn
                #Outer fyrir leikmenn

            else:
                print("invalid input, please try again")
