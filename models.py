from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, first_name, date_of_birth, sex, classification):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.classification = classification


class Tournament:
    def __init__(self, name_tournament, location, date_start, date_end,
                 list_players, description):
        self.name_tournament = name_tournament
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.turn = 4
        self.round = []  # in round stock list match
        self.list_players = list_players
        self.time = 1
        self.description = description
        self.status = True
        self.db = TinyDB('./data_base/tournament.json')

    def add_tournament_in_data_base(self):
        self.db.insert({"name": self.name_tournament, "location": self.location, "date_start": self.date_start,
                        "date_end": self.date_end, "turn": self.turn, "round": self.round, "players": self.list_players,
                        "time": self.time, "description": self.description, "status": self.status})


class DataExtractTournament:
    def __init__(self):
        self.db = TinyDB('./data_base/tournament.json')
        self.db_all = self.db.all()

    def main(self):
        pass

    def return_all_name_tournament(self):
        return self.db_all