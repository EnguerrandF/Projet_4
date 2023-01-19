class ViewCreateTournament:
    def __init__(self, list_player_data_base):
        self.name_tournament = ""
        self.location = ""
        self.date_start = ""
        self.date_end = ""
        self.list_players = []
        self.description = ""
        self.list_player_data_base = list_player_data_base

    def main(self):
        self.initialisation_data_tournament()
        self.resum_creation_tournament()
        return (self.name_tournament, self.location, self.date_start,
                self.date_end, self.list_players, self.description)

    def initialisation_data_tournament(self):
        id_max_player = 1
        print()
        print("Nouveau Tournois")
        print()
        self.name_tournament = input("Nom du tournois : ")
        self.location = input("Adresse du tournois : ")
        self.date_start = input("Date du début du tournois : ")
        self.date_end = input("Date de fin du tournois : ")
        self.description = input("Description du tournois : ")
        print("Les joueurs de la base de donnée : ")
        for player in self.list_player_data_base.all():
            print(player.doc_id, player["name"])
            # Retouner id max
            if int(player.doc_id) > int(id_max_player):
                id_max_player = str(player.doc_id)

        print("id max", id_max_player)
        for player in range(1, 9):
            players = input(f"Id du joueur {player} : ")
            if not players.isdigit() or int(players) > int(id_max_player) or players == "0":
                input("L'ID sélectionné n'est pas valide")
                self.list_players = []
                self.initialisation_data_tournament()
                break
            else:
                self.list_players.append(players)

    def resum_creation_tournament(self):
        print()
        print("Récapitulatif info")
        print()
        print("Nom du tournois : ", self.name_tournament)
        print("Adresse du tournois : ", self.location)
        print("Date du début du tournois : ", self.date_start)
        print("Date de fin du tournois : ", self.date_end)
        print("Joueurs du tournois :")
        for player in self.list_players:
            print("- ", self.list_player_data_base.get(doc_id=str(player))["name"])
        print("Description du tournois : ", self.description)
        print()