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
        self.match_logic = Match_logic()


    def get_all_players(self):
        """Calls on get_all_players in player logic and returns a list of player instances"""
        return self.player_logic.get_all_players()
    
    def create_player(self, player):
        """Takes in a player object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_player_by_name(self, name):
        """Finds a player by given name and returns every possible player with that name"""
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

    def update_end_date(self, end_date):
        """Takes in a new end date and forwards it to the data layer"""
        return self.tournament_logic.update_end_date(end_date)

    def start_tournament(self):
        """Locks creating features and starts tournament, no going back"""
        return self.tournament_logic.start_tournament()
    
    def get_league_standings(self):
        """Calculates the league and returns a nested list with [0]: wins, [1]: matches played and
        [2]: team name"""
        match_list = self.get_all_matches()
        team_list = self.get_all_teams()
        association_list = self.get_all_associations()
        return self.tournament_logic.league_standings(match_list, team_list, association_list)
    

    def get_all_matches(self):
        """Calls on get_all_matches in match logic and returns a list of match instances"""
        return self.match_logic.get_all_matches()
    
    def create_match(self, match):
        """Takes in a match object and forwards it to the data layer"""
        return self.match_logic.create_match(match)

    def postpone_match(self, match_id, date):
        """Calls on postpone_match in match_logic, with a match id and the new date as a parameters
        in postpone_match"""
        return self.match_logic.postpone_match(match_id, date)
    
    def update_result(self, match_id, match):
        """Calls on update_result in match_logic, with a match id and the new result as a parameters"""
        return self.match_logic.update_result(match_id, match)
    
    def create_match_schedule(self):
        """Calls on create_match schedule in match_logic..."""
        return self.match_logic.create_match_schedule()

    def wipe_match_schedule(self):
        """Wipes the match schedule so that create_match_schedule can be used again correctly"""
        return self.match_logic.wipe_match_schedule()

    def register_result_captain(self, match):
        """Registers a new result, takes old match_id and overwrites the match with game information in
        a match instance"""
        return self.match_logic.register_result_captain(match)

    def get_top_qp_scorers(self):
        """Calculates the top quality point scorers and returns them in a list [0]: quality point amount,
        [1]: matches played and [2]: name of player"""
        player_list = self.get_all_players()
        return self.match_logic.highest_quality_points_list(player_list)