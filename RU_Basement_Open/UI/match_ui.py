from logic.logic_wrapper import Logic_Wrapper
from model.match import Match
from model.team import Team


# 
# this class would need a instance of captain registere a match.
#  
class Match_UI(): 
    def __init__(self):
        self.logic = Logic_Wrapper()

  
    def match_list_to_choose_match_id_result(self): 
# Case 10 in the wire frame and case 18. Both admin and captain uses this same list. Admin when updating score 
# and captain to add a score for a played match.   
        match_list = self.logic.get_all_matches()
        team_list = self.logic.get_all_teams()
        empty_space = ""
# Here we need table of mathces
        print("All played matches:")
        print(f"{empty_space}match id{empty_space:>12}home team{empty_space:>4}away team{empty_space:>6}result\n")
        for match in match_list:
            for team in team_list:
                if team.team_id == match.home_team:
                    home = team.name
                if team.team_id == match.away_team:
                    away = team.name
            if match.result != "":
                print(f"{match.match_id:>4}{home:>25} vs {away:<15}{empty_space:>2}{match.result}")

    
    def choose_match_id_admin(self): 
        while True:
            self.match_list_to_choose_match_id_result()
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
        match_list = self.logic.get_all_matches()
        for elem in match_list:
            if elem.match_id == match_id:
                the_match = Match(elem.date, elem.home_team, elem.away_team)
    

        while True:
            possible_results = ["4-3", "5-2", "6-1", "7-0", "3-4", "2-5", "1-6", "0-7"]

            result = input("Please input the updated result for example (4-3): ")
            while result not in possible_results:
                result = input("Please input the updated result for example (4-3): ")

            if result in possible_results[0:4]:
                print("Home team wins this time! :)")
                the_match.winner = the_match.home_team
                break
            else:
                print("Away team wins this time! :) ")
                the_match.winner = the_match.away_team
                break

        while True:
            possible_results = ["2-1", "2-0", "1-2", "0-2"]
            print("Input the result of each round","\n")
            round1 = input("Round 1 [1x501] for example (2-1): ")
            while round1 not in possible_results:
                print("invalid input, try again")
                round1 = input("Round 1 [1x501] for example (2-1): ")

            round2 = input("Round 2 [1x501] for example (2-1): ")
            while round2 not in possible_results:
                print("invalid input, try again")
                round2 = input("Round 2 [1x501] for example (2-1): ")
            
            round3 = input("Round 3 [1x501] for example (2-1): ")
            while round3 not in possible_results:
                print("invalid input, try again")
                round3 = input("Round 3 [1x501] for example (2-1): ")

            round4 = input("Round 4 [1x501] for example (2-1): ")
            while round4 not in possible_results:
                print("invalid input, try again")
                round4 = input("Round 4 [1x501] for example (2-1): ")
            
            round5 = input("Round 5 [2x301] for example (2-1): ")
            while round5 not in possible_results:
                print("invalid input, try again")
                round5 = input("Round 5 [2x301] for example (2-1): ")
            
            round6 = input("Round 6 [2xCricket] for example (2-1): ")
            while round6 not in possible_results:
                print("invalid input, try again")
                round6 = input("Round 6 [2xCricket] for example (2-1): ")
            
            round7 = input("Round 7 [4x501] for example (2-1): ")
            while round7 not in possible_results:
                print("invalid input, try again")
                round7 = input("Round 7 [4x501] for example (2-1): ")

            the_match.round1 = round1
            the_match.round2 = round2
            the_match.round3 = round3
            the_match.round4 = round4
            the_match.round5 = round5
            the_match.round6 = round6
            the_match.round7 = round7

            self.logic.update_result(match_id, the_match)

            break

            

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


    def choose_match_id_to_change_a_date_for_a_match(self): 
        while True:
            self.match_list_to_choose_match_id_date()
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
            print("\n","press b to go back")
            date = input("Write the new date (dd/mm/yyyy): ")
            date = date.lower()
            if date == "b":
                print("you are going back")
                break
            else:
                date_change = self.logic.postpone_match(command, date)
                while date_change == False:
                    print("Invalid date, please try again")
                    date = input("Write the new date (dd/mm/yyyy): ")
                    date_change = self.logic.postpone_match(command, date)
                break

                # Sends to match id to input_prompt_for_update_score
        #only callable by admin
        #would first show all matches and admin would choose corrsponding match id where he would like to cange the date


    def match_list_to_choose_match_id_date(self): 
# Case 10 in the wire frame and case 18. Both admin and captain uses this same list. Admin when updating score 
# and captain to add a score for a played match.   
        match_list = self.logic.get_all_matches()
        team_list = self.logic.get_all_teams()
        empty_space = ""
# Here we need table of mathces
        print("All played matches:")
        print(f"{empty_space}match id{empty_space:>12}home team{empty_space:>4}away team{empty_space:>8}date\n")
        for match in match_list:
            for team in team_list:
                if team.team_id == match.home_team:
                    home = team.name
                if team.team_id == match.away_team:
                    away = team.name
            if match.result == "":
                print(f"{match.match_id:>4}{home:>25} vs {away:<15}{empty_space:>2}{match.date}")


    def choose_match_id_captain(self): 
        while True:
            self.match_list_to_choose_match_id_date()
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
        match_list = self.logic.get_all_matches()
        for elem in match_list:
            if elem.match_id == match_id:
                the_match = Match(elem.date, elem.home_team, elem.away_team)
    

        while True:
            possible_results = ["4-3", "5-2", "6-1", "7-0", "3-4", "2-5", "1-6", "0-7"]

            result = input("Please input the updated result fx (4-3): ")
            while result not in possible_results:
                result = input("Please input the updated result fx (4-3): ")

            if result in possible_results[0:4]:
                print("Home team wins this time! :)")
                the_match.winner = the_match.home_team
                break
            else:
                print("Away team wins this time! :) ")
                the_match.winner = the_match.away_team
                break

        while True:
            possible_results = ["2-1", "2-0", "1-2", "0-2"]
            print("Input the result of each round","\n")
            round1 = input("Round 1 [1x501] fx (2-1): ")
            while round1 not in possible_results:
                print("invalid input, try again")
                round1 = input("Round 1 [1x501] fx (2-1): ")

            round2 = input("Round 2 [1x501] fx (2-1): ")
            while round2 not in possible_results:
                print("invalid input, try again")
                round2 = input("Round 2 [1x501] fx (2-1): ")
            
            round3 = input("Round 3 [1x501] fx (2-1): ")
            while round3 not in possible_results:
                print("invalid input, try again")
                round3 = input("Round 3 [1x501] fx (2-1): ")

            round4 = input("Round 4 [1x501] fx (2-1): ")
            while round4 not in possible_results:
                print("invalid input, try again")
                round4 = input("Round 4 [1x501] fx (2-1): ")
            
            round5 = input("Round 5 [2x301] fx (2-1): ")
            while round5 not in possible_results:
                print("invalid input, try again")
                round5 = input("Round 5 [2x301] fx (2-1): ")
            
            round6 = input("Round 6 [2xCricket] fx (2-1): ")
            while round6 not in possible_results:
                print("invalid input, try again")
                round6 = input("Round 6 [2xCricket] fx (2-1): ")
            
            round7 = input("Round 7 [4x501] fx (2-1): ")
            while round7 not in possible_results:
                print("invalid input, try again")
                round7 = input("Round 7 [4x501] fx (2-1): ")

            the_match.round1 = round1
            the_match.round2 = round2
            the_match.round3 = round3
            the_match.round4 = round4
            the_match.round5 = round5
            the_match.round6 = round6
            the_match.round7 = round7

            self.logic.update_result(match_id, the_match)

            break

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

  