from data.player_data import Player_data
from data.team_data import Team_data
from data.association_data import Association_data
from data.tournament_data import Tournament_data
from data.match_data import Match_data


class Data_Wrapper:
    """Initializes the Data wrapper class by getting the required classes"""
    def __init__(self):
        self.player_data = Player_data()
        self.team_data = Team_data()
        self.association_data = Association_data()
        self.tournament_data = Tournament_data()

    def get_all_players(self):
        """Calls on get_all_player function in player_data and forwards
           it to the logic wrapper"""
        return self.player_data.get_all_players()
    
    def create_player(self, player):
        """Calls on get create_player, with a player instance as a paramater 
        in player_data and forwards it to the logic wrapper"""
        return self.player_data.create_player(player)


    def get_all_teams(self):
        """Calls on get_all_teams function in team_data and forwards
           it to the logic wrapper"""
        return self.team_data.get_all_teams()
    
    def create_team(self, team):
        """Calls on get create_team, with a team instance as a paramater 
        in team_data and forwards it to the logic wrapper"""
        return self.team_data.create_team(team)
    
    def choose_captain(self, team_id, captain_id):
        """Calls on get choose_captain in team_data and forwards
           it to the logic wrapper"""
        return self.team_data.choose_captain(team_id, captain_id)


    def get_all_associations(self):
        """Calls on get_all_association function in association_data and forwards
           it to the logic wrapper"""
        return self.association_data.get_all_associations()

    def create_association(self, association):
        """Calls on get create_association, with a association instance as a paramater 
        in association_data and forwards it to the logic wrapper"""
        return self.association_data.create_association(association)
    
    
    def get_tournament_info(self):
        """Calls on get get_tournament_info in tournament_data and forwards
           it to the logic wrapper"""
        return self.tournament_data.get_tournament_info()
    
    def create_tournament(self, tournament):
        """Calls on get create_tournament, with a tournament instance as a paramater 
        in tournament_data and forwards it to the logic wrapper"""
        return self.tournament_data.create_tournament(tournament)
    

    def get_all_matches(self):
        """Calls on get get_all_matches in matches_data and forwards
           it to the logic wrapper"""
        return self.match_data.get_all_matches()

    def create_match(self, match):
        """Calls on get create_match, with a match instance as a paramater 
        in match_data and forwards it to the logic wrapper"""
        return self.match_data.create_match(match)