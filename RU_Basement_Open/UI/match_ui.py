from logic.logic_wrapper import Logic_Wrapper
from model.match import Match
from model.team import Team
from datetime import date


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
        possible_match_ids = []
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
                possible_match_ids.append(match.match_id)
        return possible_match_ids

    
    def choose_match_id_admin(self): 
        while True:
            poosible_ids = self.match_list_to_choose_match_id_result()
            if len(poosible_ids) == 0:
                print("No match(es) played, going back...")
                break
            else:
                command = input("Enter the match id or b to go back: ")
                command = command.lower()
                if command in poosible_ids:
                    self.input_prompt_for_update_score(command)
                elif command == "b":
                    print("you are going back")
                    break

    def input_prompt_for_update_score(self,match_id):
# Case 21 
        match_list = self.logic.get_all_matches()
        for elem in match_list:
            if elem.match_id == match_id:
                the_match = Match(elem.date, elem.home_team, elem.away_team)
    

        while True:
            possible_results = ["4-3", "5-2", "6-1", "7-0", "3-4", "2-5", "1-6", "0-7"]

            result = input("Please input the result fx (4-3): ")
            while result not in possible_results:
                result = input("Please input the result fx (4-3): ")

            the_match.result = result

            if result in possible_results[0:4]:
                print("Home team won that time, right? :)")
                the_match.winner = the_match.home_team
            else:
                print("Away team won that time, right? :) ")
                the_match.winner = the_match.away_team
            player_list = []
            

            rounds = self.input_for_rounds()

            home_team_legs_win = 0
            away_team_legs_win = 0

            for round in rounds:
                a, b = round.split("-")
                home_team_legs_win += int(a)
                away_team_legs_win += int(b)

            the_match.home_team_legs_won = home_team_legs_win
            the_match.away_team_legs_won = away_team_legs_win
            the_match.round1 = rounds[0]
            the_match.round2 = rounds[1]
            the_match.round3 = rounds[2]
            the_match.round4 = rounds[3]
            the_match.round5 = rounds[4]
            the_match.round6 = rounds[5]
            the_match.round7 = rounds[6]

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

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")

        possible_match_ids = []
        print("All match(es) today:")
        print(f"{empty_space}match id{empty_space:>12}home team{empty_space:>4}away team\n")
        for match in match_list:
            for team in team_list:
                if team.team_id == match.home_team:
                    home = team.name
                if team.team_id == match.away_team:
                    away = team.name
            if match.result == "" and match.date == d1:
                print(f"{match.match_id:>4}{home:>25} vs {away:<15}{empty_space:>2}")
                possible_match_ids.append(match.match_id)
        return possible_match_ids


    def choose_match_id_captain(self): 
        while True:
            possible_match_ids = self.match_list_to_choose_match_id_date()
            command = input("Enter the match id or b to go back: ")
            command = command.lower()
            if command == "b":
                print("you are going back")
                break
            elif command in possible_match_ids:
                self.input_prompt_for_update_score_captain(command) 
                break
            elif len(possible_match_ids) == 0:
                print("No matches today, going back...")
                break
            else:
                print("Invalid input, please try again")

                
    def input_prompt_for_update_score_captain(self,match_id):
# Case 21 
        match_list = self.logic.get_all_matches()
        for elem in match_list:
            if elem.match_id == match_id:
                the_match = Match(elem.date, elem.home_team, elem.away_team,"","",match_id)
    

        while True:
            self.players_who_played(the_match)

            possible_results = ["4-3", "5-2", "6-1", "7-0", "3-4", "2-5", "1-6", "0-7"]

            result = input("Please input the result fx (4-3): ")
            while result not in possible_results:
                result = input("Please input the result fx (4-3): ")

            the_match.result = result

            if result in possible_results[0:4]:
                print("Home team wins this time! :)")
                the_match.winner = the_match.home_team
            else:
                print("Away team wins this time! :) ")
                the_match.winner = the_match.away_team
            player_list = []
            

            rounds = self.input_for_rounds()

            self.add_quality_points(the_match)

            home_team_legs_win = 0
            away_team_legs_win = 0

            for round in rounds:
                a, b = round.split("-")
                home_team_legs_win += int(a)
                away_team_legs_win += int(b)

            the_match.home_team_legs_won = home_team_legs_win
            the_match.away_team_legs_won = away_team_legs_win
            the_match.round1 = rounds[0]
            the_match.round2 = rounds[1]
            the_match.round3 = rounds[2]
            the_match.round4 = rounds[3]
            the_match.round5 = rounds[4]
            the_match.round6 = rounds[5]
            the_match.round7 = rounds[6]

            self.logic.register_result_captain(the_match)

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
        
    def input_for_rounds(self):
        """Checks on input for each round and returns a list of all round results"""
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
            
        rounds = [round1,round2,round3,round4,round5,round6,round7]

        return rounds
    

    def players_who_played(self, match):
        """Checks input for players who played and returns a list of player id to 
        update the match with"""
        team_list = self.logic.get_all_teams()
        player_list = self.logic.get_all_players()
        player_id_list = []

        home_pl = []
        away_pl = []
        for player in player_list:
            if player.team_id == match.away_team:
                away_pl.append(player.social_security_number)
            if player.team_id == match.home_team:
                home_pl.append(player.social_security_number)
        
        for team in team_list:
            if match.home_team == team.team_id:
                for i in range(4):
                    print("Home team:")
                    for player, j in zip(player_list, range(len(home_pl))):
                        if player.team_id == team.team_id:
                            if player.social_security_number not in player_id_list:
                                print(f"({j}), {player.name}")
                    number = int(input("Choose the number beside the player of your choice: "))
                    player_id_list.append(home_pl[number])
        
        for team in team_list:
            if match.away_team == team.team_id:
                for m in range(4):
                    print("Away team:")
                    for player, n in zip(player_list, range(len(away_pl))):
                        if player.team_id == team.team_id:
                            if player.social_security_number not in player_id_list:
                                print(f"({n}), {player.name}")
                    number = int(input("Choose the number beside the player of your choice: "))
                    player_id_list.append(away_pl[number])
        
        match.round1_home_player = player_id_list[0]
        match.round1_away_player = player_id_list[4]
        match.round2_home_player = player_id_list[1]
        match.round2_away_player = player_id_list[5]
        match.round3_home_player = player_id_list[2]
        match.round3_away_player = player_id_list[6]
        match.round4_home_player = player_id_list[3]
        match.round4_away_player = player_id_list[7]
        match.round5_home_player1 = player_id_list[0]
        match.round5_away_player2 = player_id_list[1]
        match.round5_away_player1 = player_id_list[4]
        match.round5_away_player2 = player_id_list[5]
        match.round6_home_player1 = player_id_list[2]
        match.round6_home_player2 = player_id_list[3]
        match.round6_away_player1 = player_id_list[6]
        match.round6_away_player2 = player_id_list[7]
        match.round7_home_player1 = player_id_list[0]
        match.round7_home_player2 = player_id_list[1]
        match.round7_home_player3 = player_id_list[2]
        match.round7_home_player4 = player_id_list[3]
        match.round7_away_player1 = player_id_list[4]
        match.round7_away_player2 = player_id_list[5]
        match.round7_away_player3 = player_id_list[6]
        match.round7_away_player4 = player_id_list[7]

    
    def add_quality_points(self, match):
        """"""
        player_list = self.logic.get_all_players()

        for player in player_list:
            if player.social_security_number == match.round7_home_player1:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_h_1 = qp

        for player in player_list:
            if player.social_security_number == match.round7_home_player2:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_h_2 = qp

        for player in player_list:
            if player.social_security_number == match.round7_home_player3:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_h_3 = qp

        for player in player_list:
            if player.social_security_number == match.round7_home_player4:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_h_4 = qp

        for player in player_list:
            if player.social_security_number == match.round7_away_player1:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_a_1 = qp

        for player in player_list:
            if player.social_security_number == match.round7_away_player2:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_a_2 = qp

        for player in player_list:
            if player.social_security_number == match.round7_away_player3:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_a_3 = qp

        for player in player_list:
            if player.social_security_number == match.round7_away_player4:
                while True:
                    try:
                        qp = int(input(f"How many quality points did {player.name}? "))
                        while qp not in range(0,100):
                            print("Please input logical amount of quality points")
                            qp = int(input(f"How many quality points did {player.name}? "))
                        break
                    except:
                        print("Please input a number")
                        continue
        match.qp_player_a_4 = qp