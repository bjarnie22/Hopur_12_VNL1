class Tournament:
    def __init__(self, tournament_name, admin_name, admin_phone, admin_email, start_date, end_date, number_of_rounds, started="No"):
        self.tournament_name = tournament_name
        self.admin_name = admin_name
        self.admin_phone = admin_phone
        self.admin_email = admin_email
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.started = started