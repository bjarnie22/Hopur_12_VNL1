from data.tournament_data import Tournament_data
from model.tournament import Tournament
from data.data_wrapper import Data_Wrapper

class Tournament_logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()


    def create_tournament(self, tournament):
        """Takes in a tournament object and forwards it to the data layer"""
        if self.get_tournament_info() == []:
            self.data_wrapper.create_tournament(tournament)
            return True # "Tournament succesfully created"
        else:
            return False # "Tournament has already been created"


    def get_tournament_info(self):
        return self.data_wrapper.get_tournament_info()

    
    def league_standings(self, match_list, team_list, association_list):
        """Calculates the league and returns a nested list with [0]: wins, [1]: matches played and
        [2]: team name"""
        league_list = []

        for team, i in zip(team_list, range(len((team_list)))):
            for match in match_list:
                if match.result == "":
                    continue
                else:
                    for association in association_list:
                        if team.association_id == association.association_id:
                            association_name = association.name
                    if match.home_team == team.team_id:
                        try:
                            if team.name in league_list[i]:
                                league_list[i][3] += 1
                                league_list[i][1] += int(match.home_team_legs_won)
                                if team.team_id == match.winner:
                                    league_list[i][0] += 1
                        except:
                                if team.team_id == match.winner:
                                    league_list.append([1,int(match.home_team_legs_won),association_name,1,team.name])
                                else:
                                    league_list.append([0,int(match.home_team_legs_won),association_name,1,team.name])

                    elif match.away_team == team.team_id:
                        try:
                            if team.name in league_list[i]:
                                league_list[i][3] += 1
                                league_list[i][1] += int(match.away_team_legs_won)
                                if team.team_id == match.winner:
                                    league_list[i][0] += 1
                        except:
                                if team.team_id == match.winner:
                                    league_list.append([1,int(away_team_legs_won),association_name,1,team.name])
                                else:
                                    league_list.append([0,int(match.away_team_legs_won),association_name,1,team.name])
        league_list.sort(reverse=True)
        return league_list