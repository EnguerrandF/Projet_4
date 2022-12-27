class ViewMenu:
    def __init__(self):
        self.result_main_page_menu = 0

    def main(self):
        return self.display_page_menu()

    def display_page_menu(self):
        list_menu = ["1 Nouveau Tournois", "2 Les Tournois en cours",
                     "3 Les Joueurs enregistrés", "4 Ajouter un joueur", "5 Quitter"]
        print()
        for menu in list_menu:
            print(menu)
        print()
        valeur_input_menu = input("Veuillez sélectionner un chiffre : ")

        return valeur_input_menu


class ViewCreateTournament:
    def __init__(self):
        self.name_tournament = ""
        self.location = ""
        self.date_start = ""
        self.date_end = ""
        self.list_players = []
        self.description = ""
        self.status = ""

    def main(self):
        self.initialisation_data_tournament()
        self.resum_creation_tournament()
        return [self.name_tournament, self.location, self.date_start, self.date_end,
                self.list_players, self.description]

    def initialisation_data_tournament(self):
        print()
        print("Nouveau Tournois")
        print()
        self.name_tournament = input("Nom du tournois : ")
        self.location = input("Adresse du tournois : ")
        self.date_start = input("Date du début du tournois : ")
        self.date_end = input("Date de fin du tournois : ")
        for player in range(1, 9):
            players = input(f"Joueur {player} du tournois : ")
            self.list_players.append(players)
        self.description = input("Description du tournois : ")

    def resum_creation_tournament(self):
        print()
        print("Récapitulatif info")
        print()
        dict_info_tournament = {"Nom du tournois : ": self.name_tournament,
                                "Adresse du tournois : ": self.location,
                                "Date du début du tournois : ": self.date_start,
                                "Date de fin du tournois : ": self.date_end,
                                "Joueurs du tournois": self.list_players,
                                "Description du tournois : ": self.description}

        for parameter in dict_info_tournament:
            print(parameter, dict_info_tournament[parameter])
        print()


class ViewTournamentInProgress:
    def __init__(self, list_tournement_in_progress):
        self.list_tournement_in_progress = list_tournement_in_progress
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
            self.display_tournament(self.value_input)

        if self.value_input == 1:
            return "Continuer le tournois"
        elif self.value_input == 99:
            self.main()
        elif self.value_input == 999:
            print("Retour au Menu")
        else:
            input("Le chiffre sélectionné n'est pas valide")
            self.main()

    def menu_tournament_in_progress(self):
        print()
        print("Les tournois en cours: ")
        for list in range(len(self.list_tournement_in_progress)):
            print(list, self.list_tournement_in_progress[list][0])

        print("999 Menu principal")
        print()
        input_selection = input("Sélectionner un chiffre : ")
        print()

        self.value_input = self.check_value_input_int(input_selection)

    def display_tournament(self, value_menu_tournament_in_progress):
        dict_info_tournament = {"Nom du tournois : ":
                                self.list_tournement_in_progress[value_menu_tournament_in_progress][0],
                                "Adresse du tournois : ":
                                self.list_tournement_in_progress[value_menu_tournament_in_progress][1],
                                "Date du début du tournois : ":
                                self.list_tournement_in_progress[value_menu_tournament_in_progress][2],
                                "Date de fin du tournois : ":
                                self.list_tournement_in_progress[value_menu_tournament_in_progress][3],
                                "Joueurs du tournois":
                                self.list_tournement_in_progress[value_menu_tournament_in_progress][4],
                                "Description du tournois : ":
                                self.list_tournement_in_progress[value_menu_tournament_in_progress][5]
                                }
        for dict in dict_info_tournament.items():
            print(dict)

        print()
        print("1 Continuer le tournois")
        print("99 Retour")
        print("999 Menu principal")
        print()
        input_selection = input("Sélectionner un chiffre : ")
        self.value_input = self.check_value_input_int(input_selection)

    def check_value_input_int(self, value):
        try:
            int(value)
            return int(value)
        except ValueError:
            return 1000
