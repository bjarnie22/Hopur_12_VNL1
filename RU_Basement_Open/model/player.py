class Player:
    def __init__(self, team_id, name, social_security_number, date_of_birth, email, address="", phone_number="", mobile=""):
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.mobile = mobile
        self.social_security_number = social_security_number
        self.team_id = team_id