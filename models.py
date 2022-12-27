class Player:
    def __init__(self, name, first_name, date_of_birth, sex, classification):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.classification = classification


class Tournament:
    def __init__(self, name_tournament, location, date_start, date_end,
                 list_players, description, status):
        self.name_tournament = name_tournament
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.turn = 4
        self.round = []  # in round stock list match
        self.list_players = list_players
        self.time = 1
        self.description = description
        self.status = status
