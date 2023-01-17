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
        for player in self.list_player_data_base.all():
            print(player.doc_id, player["name"])

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
            print("- ", self.list_player_data_base.get(doc_id=str(player))["name"])
        print("Description du tournois : ", self.description)
        print()


class ViewTournamentInProgress:
    def __init__(self, list_tournement_in_progress, list_player_data_base,
                 progress_or_finished):
        self.list_tournement_in_progress = list_tournement_in_progress
        self.list_player_data_base = list_player_data_base
        self.progress_or_finished = progress_or_finished
        self.value_input = 99
        self.tournament_selected = None

    def menu_tournament_in_progress(self):
        print()
        if self.progress_or_finished is True:
            print("Les tournois en cours: ")
        else:
            print("Les tournois terminé: ")

        for tournois in self.list_tournement_in_progress.all():
            if tournois["status"] is self.progress_or_finished:
                print(tournois.doc_id, tournois["name"])

        print()
        print("01 Menu principal")
        self.value_input = input("Sélectionner un chiffre : ")
        print()
        return self.value_input

    def display_tournament(self, value_input):
        print("Nom du tournois : ",
              self.list_tournement_in_progress.get(doc_id=str(value_input))["name"])
        print("Adresse du tournois :",
              self.list_tournement_in_progress.get(doc_id=str(value_input))["location"])
        print("Date du début du tournois :",
              self.list_tournement_in_progress.get(doc_id=str(value_input))["date_start"])
        print("Date de fin du tournois :",
              self.list_tournement_in_progress.get(doc_id=str(value_input))["date_end"])
        print("Joueurs du tournois: ")
        for player in self.list_tournement_in_progress.get(doc_id=str(value_input))["players"]:
            print("- ", self.list_player_data_base.get(doc_id=str(player))["name"])
        print("Description du tournois :",
              self.list_tournement_in_progress.get(doc_id=str(value_input))["description"])
        print()
        print("03 Continuer le tournois")
        print("02 Retour")
        print("01 Menu principal")
        print()
        return input("Sélectionner un chiffre : ")

    def display_match_round(self, list_tournament_work, id_round):
        print()
        print("Les Matchs du " + str(id_round))
        print("Date et heure du début du round : ", list_tournament_work["round"]["round_1"][4][0])
        print()
        print("1 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][0][0][0][1]))["name"],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][0][1][0][1]))["name"])
        print("2 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][1][0][0][1]))["name"],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][1][1][0][1]))["name"])
        print("3 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][2][0][0][1]))["name"],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][2][1][0][1]))["name"])
        print("4 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][3][0][0][1]))["name"],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][3][1][0][1]))["name"])

    def edit_result_round(self, id_round):
        print()
        print("03 Entrer le résultat du match 1")
        print("04 Entrer le résultat du match 2")
        print("05 Entrer le résultat du match 3")
        print("06 Entrer le résultat du match 4")
        print("07 Valider le round")
        print("02 Retour")
        print("01 Menu principal")
        valeur_input = input("Sélectionner un chiffre : ")

        if not valeur_input.isdigit() or int(valeur_input) > 7:
            print("Sélection non valide")
            input()
            return self.edit_result_round()
        elif len(valeur_input) == 2:
            if valeur_input == "03":
                return [input("Match 1 joueur 1 : "),
                        input("Match 1 joueur 2 : "),
                        0]
            elif valeur_input == "04":
                return [input("Match 2 joueur 1 :"),
                        input("Match 2 joueur 2 :"),
                        1]
            elif valeur_input == "05":
                return [input("Match 3 joueur 1 :"),
                        input("Match 3 joueur 2 :"),
                        2]
            elif valeur_input == "06":
                return [input("Match 4 joueur 1 :"),
                        input("Match 4 joueur 2 :"),
                        3]
            elif valeur_input == "07":
                value_input_end_round_1 = input("Confimer oui / non : ")
                if value_input_end_round_1 == "oui":
                    return "end"
                else:
                    input("Non validé")
                    return False 
            elif valeur_input == "01":
                return "01"
            elif valeur_input == "02":
                return "02"

    def report_tournament(self, selection_tournament):
        print("Tournois terminé")
        print()
        list_tournament = self.list_tournement_in_progress.get(doc_id=str(selection_tournament))
        print(list_tournament)
        print()
        print("Nom du tournois :", list_tournament["name"])
        print("Date de début :", list_tournament["date_start"])
        print("Date de fin :", list_tournament["date_end"])
        print("Adresse :", list_tournament["location"])
        print("Joueurs du tournois :")
        for player in list_tournament["players"]:
            print(" -", self.list_player_data_base.get(doc_id=str(player))["name"])
        print("Description : ", list_tournament["description"])
        for round in range(4):
            print()
            print("Round " + str(round + 1))
            # print(list_tournament["round"]["round_" + str(round + 1)])
            for match in range(4):
                print(self.list_player_data_base.get(doc_id=list_tournament["round"]["round_" + str(round + 1)][match][0][0][1])["name"],
                      self.list_player_data_base.get(doc_id=list_tournament["round"]["round_" + str(round + 1)][match][0][0][1])["classification"],
                      list_tournament["round"]["round_" + str(round + 1)][match][0][1],
                      "vs ",
                      self.list_player_data_base.get(doc_id=list_tournament["round"]["round_" + str(round + 1)][match][1][0][1])["name"],
                      self.list_player_data_base.get(doc_id=list_tournament["round"]["round_" + str(round + 1)][match][1][0][1])["classification"],
                      list_tournament["round"]["round_" + str(round + 1)][match][1][1]
                      )
            print()
            print("Date et heure de début :", list_tournament["round"]["round_" + str(round + 1)][4][0])
            print("Date et heure de fin du round :", list_tournament["round"]["round_" + str(round + 1)][4][1])
        print()
        input("Menu principal")


class ViewPlayers:
    def __init__(self, list_player):
        self.list_player = list_player
        self.list_tempo = []
        self.value_selection = 999
        self.value_player_selected = 0

    def main(self):
        self.display_players()
        self.main_display_player()
        if self.value_selection is False:
            return False
        else:
            self.main_data_one_player()

        if self.value_selection is False:
            return False
        else:
            return self.value_selection

    def main_display_player(self):
        if not self.value_selection.isdigit() or int(self.value_selection) > len(self.list_player) - 1:
            # si id s'électionné est pas valide et que c'est une chaine de caractere
            input("Le chiffre sélectionné n'est pas valide")
            return self.main_display_player()
        elif len(self.value_selection) == 2 and self.value_selection[0] == "0":
            if self.value_selection[0] == "0" and self.value_selection[1] == "1":
                self.value_selection = False
            elif self.value_selection[0] == "0" and self.value_selection[1] == "2":
                pass
            elif self.value_selection[0] == "0" and self.value_selection[1] == "3":
                self.display_player_order_alphabetical()
                self.main_display_player()
            elif self.value_selection[0] == "0" and self.value_selection[1] == "4":
                self.display_player_order_classification()
                self.main_display_player()
            elif self.value_selection[0] == "0" and self.value_selection[1] == "5":
                self.display_players()
                self.main_display_player()
        else:
            pass

    def display_players(self):
        print()
        print("Les joueurs enregistré: ")
        print()
        for player in self.list_player:
            print(player.doc_id, player["name"], player["classification"])

        print()
        print("03 Trier par ordre alphabétique")
        print("04 Trier par classement")
        print("01 Menu")
        self.value_selection = input("Sélectionner le chiffre: ")

    def display_player_order_alphabetical(self):
        print()
        print("Les joueurs enregistré: ")
        print()
        list_player = []
        i = 0

        for player in self.list_player:
            list_player.append([player["name"], i, player["classification"]])
            i += 1
        list_player.sort()
        for player in list_player:
            print(player[1], player[0], player[2])

        print()
        print("05 Trier par ordre de création")
        print("04 Trier par classement")
        print("01 Menu")
        self.value_selection = input("Sélectionner le chiffre: ")

    def display_player_order_classification(self):
        print()
        print("Les joueurs enregistré: ")
        print()
        list_player = []
        i = 0

        for player in self.list_player:
            list_player.append([int(player["classification"]), player["name"], i, ])
            i += 1
        list_player.sort(reverse=True)
        for player in list_player:
            print(player[2], player[1], player[0])

        print()
        print("05 Trier par ordre de création")
        print("03 Trier par ordre alphabétique")
        print("01 Menu")
        self.value_selection = input("Sélectionner le chiffre: ")

    def main_data_one_player(self):
        self.data_one_player()
        if not self.value_selection.isdigit() or int(self.value_selection) > 4:
            # si id s'électionné est pas valide et que c'est une chaine de caractere
            input("Le chiffre sélectionné n'est pas valide")
            self.main_display_player()
        elif len(self.value_selection) == 2 and self.value_selection[0] == "0":
            if self.value_selection[0] == "0" and self.value_selection[1] == "1":
                self.value_selection = False
            elif self.value_selection[0] == "0" and self.value_selection[1] == "2":
                self.main()
        elif int(self.value_selection) <= 4:
            self.value_selection = [input("Sélectionner la nouvelle Valeur : "), int(self.value_selection),
                                    self.value_player_selected]
        else:
            self.value_selection = False

    def data_one_player(self):
        print()
        self.value_player_selected = int(self.value_selection) + 1
        i = 0
        for description, value in self.list_player[int(self.value_selection)].items():
            print(i, description, ":", value)
            i += 1
        print()
        print("01 Retour au menu")
        print("02 Retour")
        self.value_selection = input("Sélectionner le chiffre : ")


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
