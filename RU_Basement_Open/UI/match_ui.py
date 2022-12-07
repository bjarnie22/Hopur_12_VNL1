# 
# this class would need a instance of captain registere a match.
#  
class Match(): 
    def __init__(self):
        pass

  
    def match_list_to_choose_match_id(self): 
# Case 10 in the wire frame and case 18. Both admin and captain uses this same list. Admin when updating score 
# and captain to add a score for a played match.   
        pass
# Here we need table of mathces
    
    def choose_match_id_admin(self): 
        while True:
            self.match_list_to_choose_match_id()
            command = input("Enter the match id or b to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                self.input_prompt_for_update_score(command) 
                # Sends to match id to input_prompt_for_update_score

    def input_prompt_for_update_score(self,match_id):
# Case 21 
        while True:
            team_win = int(input("Type 1 if home team won, type 2 if away team won: "))
            if team_win == 1:
                print("Home team wins this time! :)")
                break
            elif team_win == 2:
                print("Away team wins this time! :) ")
                break
            else:
                print("invalid input try again")

        while True:
            home_team_legs_won = int(input("How many legs did home team win: "))
        
            if home_team_legs_won >= 0 and home_team_legs_won <= 14:
                print("Home team won {} legs".format(home_team_legs_won))
                break
            else:
                print("invalid input try again")

        while True:
            away_team_legs_won = int(input("How many legs did away team win: "))
            if away_team_legs_won >= 0 and away_team_legs_won <= 14:
                print("Away team won {} legs".format(away_team_legs_won))
                break
                # Here we need to send, match id, the team_win, and home_team_legs_won and away_team_legs_one 
            else:
                print("invalid input try again")


        #B-kröfur
        #Stig fyrir leikmenn
        #QP fyrir leikmenn
        #Inner fyrir leikmenn
        #Outer fyrir leikmenn

        #def player_points:
            #points_for_player = input("how many points did "player" score")
            #quality_points_for_player = input("how many quality points did "player" score")
            #inner_points_for_player = input("How many inner points did player score")
            #outer_points_for_player = input("How many outer points did player score")

    def match_list_to_change_a_date_for_a_match_admin(self): 
# Case 22 in the wire frame
        pass
        
    def choose_match_id_to_change_a_date_for_a_match(self): 
        while True:
            self.match_list_to_change_a_date_for_a_match_admin()
            command = input("Enter the match id or b to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                self.input_prompt_for_update_date(command) 
                # Villu tékka match
                # Sends to match id to input_prompt_for_update_score
 
 
    def input_prompt_for_update_date(self, command):
#Case number 23
        while True:
            command = input("Write the new date or b to go back: ")
            # Here the logic layer needs to check if valid
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                print(" ")
                break
                # Sends to match id to input_prompt_for_update_score
        #only callable by admin
        #would first show all matches and admin would choose corrsponding match id where he would like to cange the date

    def choose_match_id_captain(self): 
        while True:
            self.match_list_to_choose_match_id()
            command = input("Enter the match id or b to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            else:
                self.input_prompt_for_update_score_captain(command) 
                # Sends to match id to input_prompt_for_update_score

    def input_prompt_for_update_score_captain(self,match_id):
# Case 21 
        while True:
            team_win = int(input("Type 1 if home team won, type 2 if away team won: "))
            if team_win == 1:
                print("Home team wins this time! :)")
                break
            elif team_win == 2:
                print("Away team wins this time! :) ")
                break
            else:
                print("invalid input try again")

        while True:
            home_team_legs_won = int(input("How many legs did home team win: "))
        
            if home_team_legs_won >= 0 and home_team_legs_won <= 14:
                print("Home team won {} legs".format(home_team_legs_won))
                break
            else:
                print("invalid input try again")

        while True:
            away_team_legs_won = int(input("How many legs did away team win: "))
            if away_team_legs_won >= 0 and away_team_legs_won <= 14:
                print("Away team won {} legs".format(away_team_legs_won))
                break
                # Here we need to send, match id, the team_win, and home_team_legs_won and away_team_legs_one 
            else:
                print("invalid input try again")


        #B-kröfur
        #Stig fyrir leikmenn
        #QP fyrir leikmenn
        #Inner fyrir leikmenn
        #Outer fyrir leikmenn

        #def player_points:
            #points_for_player = input("how many points did "player" score")
            #quality_points_for_player = input("how many quality points did "player" score")
            #inner_points_for_player = input("How many inner points did player score")
            #outer_points_for_player = input("How many outer points did player score")

  