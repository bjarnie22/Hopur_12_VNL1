from model.team import Team
from data.data_wrapper import Data_Wrapper

class Team_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_team(self, team):
        """Takes in a team object, gives it a team id and forwards it to the data layer"""
        team.team_id = len(self.get_all_teams())
        self.data_wrapper.create_team(team)

    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()
    

    def choose_captain(self, team_id, captain_id):
        teamlist = self.get_all_teams()
        for team in teamlist:
            if team.team_id == team_id:
                if int(team.captain_id) < 0:
                    return self.data_wrapper.choose_captain(team_id, captain_id)
                else:
                    return False