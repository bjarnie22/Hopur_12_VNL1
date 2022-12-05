from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_logic
from logic.association_logic import Association_logic
from logic.tournament_logic import Tournament_logic
from logic.match_logic import Match_logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic()
        self.team_logic = Team_logic()
        self.association_logic = Association_logic()
        self.tournament_logic = Tournament_logic()


    def get_all_players(self):
        """Calls on get_all_players in player logic and returns a list of player instances"""
        return self.player_logic.get_all_players()
    
    def create_player(self, player):
        """Takes in a player object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_player_by_name(self, name):
        """Finds a player by given name and returns every possible player"""
        return self.player_logic.get_player_by_name(name)


    def get_all_teams(self):
        """Calls on get_all_teams in team logic and returns a list of team instances"""
        return self.team_logic.get_all_teams()
    
    def create_team(self, team):
        """Takes in a team object, calls on create team in team logic and forwards it to the data layer"""
        return self.team_logic.create_team(team)

    def choose_captain(self, team_id, captain_id):
        """Takes in a team_id and captain_id and calls on choose captain in team logic"""
        return self.team_logic.choose_captain(team_id, captain_id)


    def get_all_associations(self):
        """Calls on get_all_associations in association logic and returns a list of association instances"""
        return self.association_logic.get_all_associations()

    def create_association(self, association):
        """Takes in a association object and forwards it to the data layer"""
        return self.association_logic.create_association(association)
    

    def get_tournament_info(self):
        """Calls on get_tournament_info in tournament logic and returns a instance of tournament information"""
        return self.tournament_logic.get_tournament_info()
    
    def create_tournament(self, tournament):
        """Takes in a tournament object and forwards it to the data layer"""
        return self.tournament_logic.create_tournament(tournament)
    

    def get_all_matches(self):
        """Calls on get_all_matches in match logic and returns a list of match instances"""
        return self.match_logic.get_all_matches()
    
    def create_match(self, match):
        """Takes in a match object and forwards it to the data layer"""
        return self.match_logic.create_match(match)

    def postpone_match(self, match_id, date):
        """Calls on postpone_match in the data wrapper, with a match id and the new date as a parameters
        in postpone_match"""
        return self.match_logic.postpone_match(match_id, date)
    
    def update_score(self, match_id, score):
        """Calls on update_score in the data wrapper, with a match id and the new score as a parameters
        in update_score"""
        return self.match_logic.update_score(match_id, score)