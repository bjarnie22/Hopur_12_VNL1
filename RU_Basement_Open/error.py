from datetime import datetime
from datetime import date
import string
from logic.logic_wrapper import Logic_Wrapper

class Error:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    
    def CheckTeamOrAssociationNameError(self, name):
        if self.NameCheckError(name) != True:
            return self.NameCheckError(name)
        else:
            team_list = self.logic_wrapper.get_all_teams()
            association_list = self.logic_wrapper.get_all_associations()
            for team in team_list:
                if team.name == name:
                    return "A team has already taken this name"
            for associtaion in association_list:
                if associtaion.name == name:
                    return "An association has already taken this name"
        return True



    def NameCheckError(self, name):
        """Checks if the name is too long (35 char) or if the name has illegal charchater fx numbers"""
        icelandic_char = ["á", "ö", "é", "í", "ý", "æ", "ó", "ð", "þ", "ú"]
        legal_letter_list = list(string.ascii_letters)
        legal_letter_list.append(" ")
        for i in icelandic_char:
            legal_letter_list.append(i)
            legal_letter_list.append(i.upper())

        if len(name) > 35:
            return "Name too long"
        elif len(name) < 2:
            return "Name too short"
        for letter in name:
            if letter not in legal_letter_list:
                return "No special charachters or numbers"
        return True


    def Date_Format_Error(self, date):
        """Checks if date is valid (dd/mm/yyyy), if the date is valid it returns True,
        else it returns a string error message"""
        if len(date) == 10:
            try:
                day = int(date[0:2])
                month = int(date[3:5])
                year = int(date[6:])
            except:
                return "Please use numbers in this format: dd/mm/yyyy"
            day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year%4==0 and (year%100 != 0 or year%400==0):
                day_count_for_month[2] = 29
            validity = (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
            if validity != True:
                return "Please use a real date"
        elif len(date) != 10:
            return "Please use this format: dd/mm/yyyy"

        return True

    def BirthDateError(self, birthdate):
        """Checks if birthdate is valid, returns True if it's valid,
        else it returns a string error message"""
        if len(birthdate) == 10:
            try:
                day = int(birthdate[0:2])
                month = int(birthdate[3:5])
                year = int(birthdate[6:])
            except:
                return "Please use a social security number with a real birthdate"
            day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year%4==0 and (year%100 != 0 or year%400==0):
                day_count_for_month[2] = 29
            validity = (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
            if validity != True:
                return "Please use a real date as the birthdate part of the social security number"
        
        today = date.today()
        today = today.strftime("%d/%m/%Y")

        birthday = datetime.strptime(birthdate, "%d/%m/%Y")

        if datetime.strptime(birthdate, "%d/%m/%Y") > datetime.strptime(today, "%d/%m/%Y"):
            return "No time travelers allowed, please use a birthdate from the past"
        
        return True

    
    def CheckSSNValidity(self, social_security_number):
        """Checks if social security number is valid, if that and the birthdate is valid, returns the birthdate
        in (dd/mm/yyyy), else it returns a string error message"""
        birthdate = social_security_number[0:2] + "/" + social_security_number[2:4] + "/" + social_security_number[4:6]
        if birthdate[6:] > str(date.today().year)[3:]:
            birthdate = birthdate[0:6] + "19" + birthdate[6:]
        else:
            birthdate = birthdate[0:6] + "20" + birthdate[6:]

        if len(social_security_number) == 10:
            for number in social_security_number:
                if number.isnumeric() == False:
                    return "Please use a valid social security number (xxxxxxxxxx or xxxxxx-xxxx)"
        elif len(social_security_number) == 11:
            if social_security_number[6] != "-":
                return "Please input valid social security number (xxxxxxxxxx or xxxxxx-xxxx)"
            else:
                for number in social_security_number[0:6]:
                    if number.isnumeric() == False:
                        return "Please use a valid social security number (xxxxxxxxxx or xxxxxx-xxxx)"
                for number in social_security_number[7:]:
                    if number.isnumeric() == False:
                        return "Please use a valid social security number (xxxxxxxxxx or xxxxxx-xxxx)"
        else:
            return "Please input valid social security number (xxxxxxxxxx or xxxxxx-xxxx)"
        
        if self.BirthDateError(birthdate) != True:
            return self.BirthDateError(birthdate)
        else:
            return birthdate
    

    def NotIcelandicNumberError(self, number):
        if number == "":
            return True      
        elif len(number) == 7:
            for digit in number:
                if digit.isnumeric() == False:
                    return "Please use a valid phone number with digits fx (6667887 or 666-7887)"
            return True
        elif len(number) == 8:
            if number[3] != "-":
                return "Please input a valid phone number fx (6667887 or 666-7887)"
            else:
                for number in number[0:3]:
                    if number.isnumeric() == False:
                        return "Please use a valid phone number with digits fx (6667887 or 666-7887)"
                for number in number[4:]:
                    if number.isnumeric() == False:
                        return "Please use a valid phone number with digits fx (6667887 or 666-7887)"
            return True
        else:
            return "Please put in an Icelandic number"


    def check_start_and_end_date(self, start, end):
        
        today = date.today()
        today = today.strftime("%d/%m/%Y")

        if datetime.strptime(start, "%d/%m/%Y") < datetime.strptime(today, "%d/%m/%Y"):
            return "I missed it!? Please enter a date that hasn't passed"

        if datetime.strptime(end, "%d/%m/%Y") < datetime.strptime(start, "%d/%m/%Y"):
            return "Ending before you even begin? Try again"
        else:
            return True
    

    def check_tournament_dates(self, starting_date_of_tournament, end_date_of_tournament):
        if self.Date_Format_Error(starting_date_of_tournament) != True:
            return str(self.Date_Format_Error(starting_date_of_tournament))
        if self.Date_Format_Error(end_date_of_tournament) != True:
            return str(self.Date_Format_Error(end_date_of_tournament))
        if self.Date_Format_Error(starting_date_of_tournament) == True and\
            self.Date_Format_Error(end_date_of_tournament) == True:
            if self.check_start_and_end_date(starting_date_of_tournament, end_date_of_tournament) != True:
                return str(self.check_start_and_end_date(starting_date_of_tournament, end_date_of_tournament))
        
        return True