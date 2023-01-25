from termcolor import colored


class ViewTournamentInProgress:
    def __init__(self, list_tournement_in_progress, list_player_data_base,
                 progress_or_finished):
        self.list_tournement_in_progress = list_tournement_in_progress
        self.list_player_data_base = list_player_data_base
        self.progress_or_finished = progress_or_finished

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
              list_tournament_work["round"][id_round][0][0][1],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][0][1][0][1]))["name"],
              list_tournament_work["round"][id_round][0][1][1])
        print("2 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][1][0][0][1]))["name"],
              list_tournament_work["round"][id_round][1][0][1],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][1][1][0][1]))["name"],
              list_tournament_work["round"][id_round][1][1][1])
        print("3 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][2][0][0][1]))["name"],
              list_tournament_work["round"][id_round][2][0][1],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][2][1][0][1]))["name"],
              list_tournament_work["round"][id_round][2][1][1])
        print("4 ",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][3][0][0][1]))["name"],
              list_tournament_work["round"][id_round][3][0][1],
              "vs",
              self.list_player_data_base.get(doc_id=str(list_tournament_work["round"][id_round][3][1][0][1]))["name"],
              list_tournament_work["round"][id_round][3][1][1])

    def edit_result_round(self):
        print()
        print("03 Entrer le résultat du match 1")
        print("04 Entrer le résultat du match 2")
        print("05 Entrer le résultat du match 3")
        print("06 Entrer le résultat du match 4")
        print("07 Valider le round")
        print("02 Retour")
        print("01 Menu principal")
        valeur_input = input("Sélectionner un chiffre : ")
        if not valeur_input.isdigit() or int(valeur_input) > 7 or valeur_input == "0":
            print("Sélection non valide")
            input()
            return self.edit_result_round()
        elif len(valeur_input) == 2:
            if valeur_input == "03":
                return [input("Match 1 joueur 1 :"),
                        input("Match 1 joueur 2 :"),
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

    def report_tournament(self, selection_tournament, list_player_and_score):
        print("Tournois terminé")
        list_tournament = self.list_tournement_in_progress.get(doc_id=str(selection_tournament))
        # print(list_tournament)
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
                print(self.color_text(list_tournament["round"]["round_" + str(round + 1)][match][0][1]),
                      self.list_player_data_base.get(doc_id=list_tournament["round"]  
                                                     ["round_" + str(round + 1)][match][0][0][1])["name"],
                      # self.list_player_data_base.get(
                      #                   doc_id=list_tournament["round"]["round_" + str(round + 1)]
                      #                   [match][0][0][1])["classification"],
                      "vs ",
                      self.color_text(list_tournament["round"]["round_" + str(round + 1)][match][1][1]),
                      self.list_player_data_base.get(doc_id=list_tournament["round"]["round_" + str(round + 1)]
                                                     [match][1][0][1])["name"],
                      # self.list_player_data_base.get(doc_id=list_tournament["round"]["round_" + str(round + 1)]
                      #                                [match][1][0][1])["classification"],
                      )
            print()
            print("Date et heure de début :", list_tournament["round"]["round_" + str(round + 1)][4][0])
            print("Date et heure de fin du round :", list_tournament["round"]["round_" + str(round + 1)][4][1])
        print()
        print("Classement du tournois :")
        list_player_and_score.sort(reverse=True)
        # print(list_player_and_score)
        i = 1
        for data in list_player_and_score:
            print(i,
                  self.list_player_data_base.get(doc_id=data[1])["name"],
                  data[0],
                  "points")
            i += 1
        print()
        print("01 Menu principal")
        print("02 Retour")
        return input("Sélectionner un chiffre")

    def color_text(self, point):
        if point == 1.0:
            return colored("Victoire", 'green')
        elif point == 0.0:
            return colored("Défaite", 'red')
        elif point == 0.5:
            return colored("Egalité", 'cyan')
