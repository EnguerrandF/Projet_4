from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, first_name, date_of_birth, sex, classification):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.classification = classification
        self.db = TinyDB('./data_base/players.json')

    def add_player_in_data_base(self):
        self.db.insert(
            {"name": self.name, "first_name": self.first_name, "date_of_birth": self.date_of_birth,
             "sex": self.sex, "classification": self.classification}
        )


class DataPlayer():
    def __init__(self):
        self.db = TinyDB('./data_base/players.json')
        self.db_all = self.db.all()

    def return_all_player(self):
        return self.db_all

    def return_db(self):
        return self.db

    def update_parameter_in_data_base(self, value_to_change, parameter_to_change, indice_player):
        if parameter_to_change == 0:
            parameter_to_change = "name"
        elif parameter_to_change == 1:
            parameter_to_change = "first_name"
        elif parameter_to_change == 2:
            parameter_to_change = "date_of_birth"
        elif parameter_to_change == 3:
            parameter_to_change = "sex"
        elif parameter_to_change == 4:
            parameter_to_change = "classification"
        print(parameter_to_change)
        self.db.update({parameter_to_change: value_to_change}, doc_ids=[indice_player])


class Tournament:
    def __init__(self, name_tournament, location, date_start, date_end,
                 list_players, description):
        self.name_tournament = name_tournament
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.turn = 4
        self.round = {}  # in round stock list match
        self.list_players = list_players
        self.time = 1
        self.description = description
        self.status = True
        self.db = TinyDB('./data_base/tournament.json')

    def add_tournament_in_data_base(self):
        self.db.insert({"name": self.name_tournament, "location": self.location, "date_start": self.date_start,
                        "date_end": self.date_end, "turn": self.turn, "round": self.round,
                        "players": self.list_players, "time": self.time, "description": self.description,
                        "status": self.status})


class DataTournament:
    def __init__(self):
        self.db = TinyDB('./data_base/tournament.json')

    def main(self):
        pass

    def return_all_name_tournament(self):
        return self.db.all()

    def return_db(self):
        return self.db

    def update_round(self, parameter_to_change, value_to_change, indice_tournament):
        self.db.update({parameter_to_change: value_to_change}, doc_ids=[indice_tournament])
