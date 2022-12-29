class ViewMenu:
    def __init__(self):
        self.result_main_page_menu = 0

    def main(self):
        return self.display_page_menu()

    def display_page_menu(self):
        list_menu = ["1 Nouveau Tournois", "2 Les Tournois en cours",
                     "3 Les Joueurs enregistrés", "4 Ajouter un joueur", "5 Les tournois terminés",  "6 Quitter"]
        print()
        for menu in list_menu:
            print(menu)
        print()
        valeur_input_menu = input("Veuillez sélectionner un chiffre : ")

        return valeur_input_menu


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
        print()
        print("Nouveau Tournois")
        print()
        self.name_tournament = input("Nom du tournois : ")
        self.location = input("Adresse du tournois : ")
        self.date_start = input("Date du début du tournois : ")
        self.date_end = input("Date de fin du tournois : ")
        print("Les joeurs de la base de donnée : ")
        i = 0
        for player in self.list_player_data_base:
            print(i, player["name"])
            i += 1
        for player in range(1, 9):
            players = input(f"Id du joueur {player} : ")
            self.list_players.append(players)
        self.description = input("Description du tournois : ")

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
            print("- ", self.list_player_data_base[int(player)]["name"])
        print("Description du tournois : ", self.description)
        print()


class ViewTournamentInProgress:
    def __init__(self, list_tournement_in_progress, list_player_data_base, progress_or_finished):
        self.list_tournement_in_progress = list_tournement_in_progress
        self.list_player_data_base = list_player_data_base
        self.progress_or_finished = progress_or_finished
        self.value_input = 99

    def main(self):
        self.menu_tournament_in_progress()

        if self.value_input == 999:
            print("Retour au Menu")
        elif self.value_input == 99:
            self.main()
        elif self.value_input > len(self.list_tournement_in_progress):
            input("Le chiffre n'est pas valide")
            self.main()
        else:
            number_the_tournament = self.display_tournament(self.value_input)

        if self.value_input == 1:
            return number_the_tournament
        elif self.value_input == 99:
            self.main()
        elif self.value_input == 999:
            print("Retour au Menu")
        else:
            input("Le chiffre sélectionné n'est pas valide")
            self.main()

    def menu_tournament_in_progress(self):
        print()
        if self.progress_or_finished is True:
            print("Les tournois en cours: ")
        else:
            print("Les tournois terminé: ")
        i = 0
        for tournois in self.list_tournement_in_progress:
            if tournois["status"] is self.progress_or_finished:
                print(i, tournois["name"])
            i += 1

        print("999 Menu principal")
        print()
        input_selection = input("Sélectionner un chiffre : ")
        print()

        self.value_input = self.check_value_input_int(input_selection)

    def display_tournament(self, value_menu_tournament_in_progress):
        print("Nom du tournois : ",
              self.list_tournement_in_progress[value_menu_tournament_in_progress]["name"])
        print("Adresse du tournois :",
              self.list_tournement_in_progress[value_menu_tournament_in_progress]["location"])
        print("Date du début du tournois :",
              self.list_tournement_in_progress[value_menu_tournament_in_progress]["date_start"])
        print("Date de fin du tournois :",
              self.list_tournement_in_progress[value_menu_tournament_in_progress]["date_end"])
        print("Joueurs du tournois: ")
        for player in self.list_tournement_in_progress[value_menu_tournament_in_progress]["players"]:
            print("- ", self.list_player_data_base[int(player)]["name"])
        print("Description du tournois :",
              self.list_tournement_in_progress[value_menu_tournament_in_progress]["description"])
        print()
        print("1 Continuer le tournois")
        print("99 Retour")
        print("999 Menu principal")
        print()
        number_the_tournament = self.value_input
        input_selection = input("Sélectionner un chiffre : ")
        self.value_input = self.check_value_input_int(input_selection)
        return number_the_tournament

    def check_value_input_int(self, value):
        try:
            int(value)
            return int(value)
        except ValueError:
            return 1000


class ViewPlayers:
    def __init__(self, list_player):
        self.list_player = list_player
        self.list_tempo = []
        self.value_selection = 999
        self.value_player_selected = 0

    def main(self):
        self.display_players()
        if self.value_selection == 999:
            return False
        elif self.value_selection == 99:
            return self.main()
        elif self.value_selection == 1000 or self.value_selection > len(self.list_player) - 1:
            input("Le chiffre sélectionné n'est pas valide")
            return self.main()
        elif self.value_selection < len(self.list_player):
            self.data_one_player()
            if self.value_selection == 999:
                print("truc")
                return False
            elif self.value_selection == 99:
                print("retour au menu")
                return self.main()
            elif self.value_selection == 1000 or self.value_selection > 4:
                input("Le chiffre sélectionné n'est pas valide")
                return self.main()
            elif self.value_selection <= 4:
                return [input("Sélectionner la nouvelle Valeur : "), self.value_selection, self.value_player_selected]
            else:
                return False
        else:
            return False

    def display_players(self):
        print()
        print("Les joueurs enregistré: ")
        print()
        i = 0
        for player in self.list_player:
            
            print(i, player["name"], player["classification"])
            i += 1

        print()
        print("999 Menu")
        self.value_selection = self.check_value_input_int(input("Sélectionner le chiffre: "))

    def data_one_player(self):
        print()
        self.value_player_selected = self.value_selection + 1
        i = 0
        for description, value in self.list_player[int(self.value_selection)].items():
            print(i, description, ":", value)
            i += 1
        print()
        print("999 Retour au menu")
        print("99 Retour")
        self.value_selection = self.check_value_input_int(input("Sélectionner le chiffre : "))

    def check_value_input_int(self, value):
        try:
            int(value)
            return int(value)
        except ValueError:
            return 1000


class ViewCreatePlayer:
    def add_player(self):
        print("Nouveau Joueur")
        print()
        name = input("Prénon : ")
        first_name = input("Nom de famille : ")
        date_of_birth = input("Date d'anniversaire : ")
        sex = input("Femme/Homme : ")
        classification = input("Point de classement : ")

        return [name, first_name, date_of_birth, sex, classification]
