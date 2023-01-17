from view import ViewMenu, ViewCreateTournament, ViewTournamentInProgress, ViewPlayers, ViewCreatePlayer
from models import Tournament, DataTournament, Player, DataPlayer
from time import gmtime, strftime


class Controler:
    def __init__(self):
        self.list_player_in_data_base = DataPlayer().return_db()
        self.list_tournament_in_progress_data_base = DataTournament().return_db()
        self.answer_view_menu = ""

    def main(self):
        self.answer_view_menu = ViewMenu().main()
        self.selection_menu()

    def selection_menu(self):
        if (self.answer_view_menu == "1"):
            # Créer un nouveau tournois
            data_tournament = ViewCreateTournament(self.list_player_in_data_base).main()
            Tournament(data_tournament[0], data_tournament[1], data_tournament[2], data_tournament[3],
                       data_tournament[4], data_tournament[5]).add_tournament_in_data_base()

        elif (self.answer_view_menu == "2"):
            # Afficher les tournois en cours
            ControlerTournamentInProgress().main()

        elif (self.answer_view_menu == "3"):
            # Afficher les joeurs enregistré
            list_player = DataPlayer().return_all_player()
            change_value_player = ViewPlayers(list_player).main()
            if change_value_player is False:
                pass
            else:
                DataPlayer().update_parameter_in_data_base(change_value_player[0],
                                                           change_value_player[1],
                                                           change_value_player[2])

        elif (self.answer_view_menu == "4"):
            # Ajouter un joueur
            data_player = ViewCreatePlayer().add_player()
            Player(data_player[0], data_player[1], data_player[2],
                   data_player[3], data_player[4]
                   ).add_player_in_data_base()

        elif (self.answer_view_menu == "5"):
            # Afficher les tournois terminé
            tournament_in_progress = ViewTournamentInProgress(self.list_tournament_in_progress_data_base,
                                                              self.list_player_in_data_base,
                                                              False)
            result_menu = tournament_in_progress.menu_tournament_in_progress()
            if result_menu == "01":
                pass
            else:
                tournament_in_progress.report_tournament(result_menu)

        elif (self.answer_view_menu == "6"):
            print("Aurevoir et a bientôt")
            quit()

        else:
            print()
            input("Le chiffre n'est pas valide")


class ControlerTournamentInProgress:
    def __init__(self):
        self.list_player_in_data_base = DataPlayer().return_all_player()
        self.list_tournament_in_progress_data_base = DataTournament().return_all_name_tournament()
        self.db_tournament = DataTournament().return_db()
        self.db_player = DataPlayer().return_db()
        self.tournament_in_progress_data_base = DataTournament().return_db
        self.view_tournament_in_progress = ViewTournamentInProgress(self.db_tournament,
                                                                    self.db_player, True)

        self.answer_view_menu_tournament_in_progress = "None"
        self.selection_tournament = ""
        self.answer_display_tournament = ""
        self.answer_continue_tournament = ""

    def main(self):
        if self.answer_view_menu_tournament_in_progress == "None":
            self.menu_tournament_in_progress()
        elif self.answer_view_menu_tournament_in_progress == "02":
            self.main()
        elif self.answer_view_menu_tournament_in_progress is True:
            print("Afficher le tournois")
            self.display_tournament()
        elif self.answer_display_tournament is True:
            self.continue_tournament()

        if str(self.answer_view_menu_tournament_in_progress) != "01":
            self.main()

    def menu_tournament_in_progress(self):
        print(DataTournament().return_db())
        answer_view_menu_tournament_in_progress = self.view_tournament_in_progress.menu_tournament_in_progress()
        self.answer_view_menu_tournament_in_progress = ""
        if (not answer_view_menu_tournament_in_progress.isdigit()):
            input("Le chiffre n'est pas valide")
            self.menu_tournament_in_progress()
        elif len(answer_view_menu_tournament_in_progress) == 2 and answer_view_menu_tournament_in_progress[0] == "0":
            if answer_view_menu_tournament_in_progress[0] == "0" and answer_view_menu_tournament_in_progress[1] == "1":
                print("Retour au Menu")
                self.answer_view_menu_tournament_in_progress = "01"
            elif (answer_view_menu_tournament_in_progress[0] == "0" and
                    answer_view_menu_tournament_in_progress[1] == "2"):
                self.answer_view_menu_tournament_in_progress = ""
        else:
            self.selection_tournament = int(answer_view_menu_tournament_in_progress)
            self.answer_view_menu_tournament_in_progress = True

    def display_tournament(self):
        answer_display_tournament = self.view_tournament_in_progress.display_tournament(self.selection_tournament)

        if not answer_display_tournament.isdigit() or int(answer_display_tournament) > 3:
            input("Le chiffre sélectionné n'est pas valide")
            self.display_tournament()
        elif len(answer_display_tournament) == 2:
            if answer_display_tournament[0] == "0" and answer_display_tournament[1] == "2":
                self.answer_display_tournament = "02"
                self.answer_view_menu_tournament_in_progress = "None"
            elif answer_display_tournament[0] == "0" and answer_display_tournament[1] == "1":
                self.answer_view_menu_tournament_in_progress = "01"
            elif answer_display_tournament[0] == "0" and answer_display_tournament[1] == "3":
                self.answer_display_tournament = True
                self.answer_view_menu_tournament_in_progress = False

    def continue_tournament(self):
        if len(self.list_tournament_work()["round"]) == 0:
            self.creation_first_round()
        elif len(self.list_tournament_work()["round"]) == 1:
            if self.list_tournament_work()["round"]["round_1"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_1")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round("2")
                self.end_round(value_edit_result_first_round, "round_1")
            else:
                self.creation_round(2)
        elif len(self.list_tournament_work()["round"]) == 2:
            if self.list_tournament_work()["round"]["round_2"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_2")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round("2")
                if value_edit_result_first_round[0] == False or value_edit_result_first_round[0] is False:
                    print()
                self.end_round(value_edit_result_first_round, "round_2")
            else:
                self.creation_round(3)
        elif len(self.list_tournament_work()["round"]) == 3:
            if self.list_tournament_work()["round"]["round_3"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_3")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round("3")
                self.end_round(value_edit_result_first_round, "round_3")
            else:
                self.creation_round(4)
        elif len(self.list_tournament_work()["round"]) == 4:
            if self.list_tournament_work()["round"]["round_4"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_4")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round("4")
                self.end_round(value_edit_result_first_round, "round_4")
            else:
                DataTournament().update_round("status", False, self.selection_tournament)
                self.view_tournament_in_progress.report_tournament(self.selection_tournament)
                self.answer_view_menu_tournament_in_progress = " "
                self.answer_display_tournament = " "

    def creation_first_round(self):
        list_player = []
        for player in self.list_tournament_work()["players"]:
            list_player.append([int(self.db_player.get(doc_id=player)["classification"]),
                                player])
        list_player.sort(reverse=True)
        date_hour_start = strftime("%d %m %Y %H:%M:%S", gmtime())
        creation_round = {"round_1": [
                                    [[list_player[0], 0], [list_player[4], 0]],
                                    [[list_player[1], 0], [list_player[5], 0]],
                                    [[list_player[2], 0], [list_player[6], 0]],
                                    [[list_player[3], 0], [list_player[7], 0]],
                                    [date_hour_start, ""]
                                    ]}
        DataTournament().update_round("round", creation_round, self.selection_tournament)

    def end_round(self, value_edit_result_first_round, id_round):
        print(value_edit_result_first_round[0], value_edit_result_first_round[1])
        if value_edit_result_first_round == "01":
            self.answer_view_menu_tournament_in_progress = "01"
        elif value_edit_result_first_round == "02" or value_edit_result_first_round is False:
            self.answer_view_menu_tournament_in_progress = "None"
        elif value_edit_result_first_round == "end":
            date_hour_end = strftime("%d %m %Y %H:%M:%S", gmtime())
            list_tournament = self.list_tournament_work()["round"]
            list_tournament[id_round][4][1] = date_hour_end
            DataTournament().update_round("round", list_tournament, self.selection_tournament)
            # print("Le Round est terminé")
            # print("La date de début et de fin du round : ", self.list_tournament_work()["round"]["round_1"][4])
        elif (value_edit_result_first_round[0] == "0" or value_edit_result_first_round[0] == "1" or
                value_edit_result_first_round[0] == "0.5" or value_edit_result_first_round[1] == "0" or
                value_edit_result_first_round[1] == "1" or value_edit_result_first_round[1] == "0.5"):
            value_edit_result_first_round[0]  # joueur 1
            value_edit_result_first_round[1]  # joueur 2
            value_edit_result_first_round[2]  # match 1 a 4
            list_tournament = self.list_tournament_work()["round"]
            list_tournament[id_round][value_edit_result_first_round[2]][0][1] = float(value_edit_result_first_round[0]) # joueur 1
            list_tournament[id_round][value_edit_result_first_round[2]][1][1] = float(value_edit_result_first_round[1]) # joueur 2
            DataTournament().update_round("round", list_tournament, self.selection_tournament)
        else:
            input("Le résultat sélectionné n'est pas valide, veuillez sélectionner 0, 1 ou 0.5")
            input("Le résultat sélectionné n'est pas valide, veuillez sélectionner 0, 1 ou 0.5")

    def creation_round(self, id_round):
        list_new_match = self.generate_match_round(id_round)
        new_round_for_update = self.list_tournament_work()["round"]
        new_round_for_update["round_" + str(id_round)] = list_new_match
        DataTournament().update_round("round", new_round_for_update, self.selection_tournament)

    def generate_match_round(self, id_round):
        # cette function doit me retourner une liste de matchs valide
        list_player = self.list_tournament_work()["players"]

        classement_first_round = [[self.calculate_all_point_one_player(list_player[0]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[0])["classification"]),
                                    list_player[0]]],
                                  [self.calculate_all_point_one_player(list_player[1]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[1])["classification"]),
                                    list_player[1]]],
                                  [self.calculate_all_point_one_player(list_player[2]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[2])["classification"]),
                                    list_player[2]]],
                                  [self.calculate_all_point_one_player(list_player[3]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[3])["classification"]),
                                    list_player[3]]],
                                  [self.calculate_all_point_one_player(list_player[4]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[4])["classification"]),
                                    list_player[4]]],
                                  [self.calculate_all_point_one_player(list_player[5]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[5])["classification"]),
                                    list_player[5]]],
                                  [self.calculate_all_point_one_player(list_player[6]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[6])["classification"]),
                                    list_player[6]]],
                                  [self.calculate_all_point_one_player(list_player[7]),
                                   [int(DataPlayer().return_db().get(doc_id=list_player[7])["classification"]),
                                    list_player[7]]]]
        classement_first_round.sort(reverse=True)
        print("Classement des joueurs du", "round_" + str(id_round), classement_first_round)
        list_new_match = []
        i = 0
        for math in range(4):
            for player in range(7):
                match = [int(classement_first_round[0][1][1]), int(classement_first_round[i + 1][1][1])]
                return_match_is_completed = self.check_match_is_not_completed(match)
                if return_match_is_completed is False:
                    pass
                elif return_match_is_completed is True:
                    id_player_one = str(classement_first_round[0][1][1])
                    id_player_two = str(classement_first_round[i + 1][1][1])
                    for_one_match = [
                                    [[self.db_player.get(doc_id=id_player_one)["classification"], id_player_one], 0],
                                    [[self.db_player.get(doc_id=id_player_two)["classification"], id_player_two], 0]
                                    ]
                    list_new_match.append(for_one_match)
                    classement_first_round.pop(0)
                    classement_first_round.pop(i)
                    break
                i += 1

        date_hour_start = strftime("%d %m %Y %H:%M:%S", gmtime())
        list_new_match.append([date_hour_start, ""])
        return list_new_match

    def check_match_is_not_completed(self, new_match):
        # Vérifier dans tout les rounds si le match a pas été déja réalisé
        for round_realized in self.list_tournament_work()["round"]:
            for match in range(4):
                match_round_actuel = [int(self.list_tournament_work()["round"][round_realized][match][0][0][1]),
                                      int(self.list_tournament_work()["round"][round_realized][match][1][0][1])]
                new_match.sort(reverse=True)
                match_round_actuel.sort(reverse=True)

                if new_match == match_round_actuel:
                    return False
                else:
                    pass
        return True

    def calculate_all_point_one_player(self, id_player):
        point_player = 0
        for round in self.list_tournament_work()["round"]:
            # un round
            for match in range(4):
                # un match
                # print(self.list_tournament_work()["round"][round][match]) # le match du round
                # print("Le joueurs", self.list_tournament_work()["round"][round][match][0][0][1],
                #       self.list_tournament_work()["round"][round][match][0][1]) # le score du joeurs premier joueur
                # print("Le joueurs", self.list_tournament_work()["round"][round][match][1][0][1],
                #       self.list_tournament_work()["round"][round][match][1][1]) # le score du joeurs deuxieme joueur
                if self.list_tournament_work()["round"][round][match][0][0][1] == id_player:
                    point_player += self.list_tournament_work()["round"][round][match][0][1]
                if self.list_tournament_work()["round"][round][match][1][0][1] == id_player:
                    point_player += self.list_tournament_work()["round"][round][match][1][1]
        return point_player

    def list_tournament_work(self):
        return self.db_tournament.get(doc_id=str(self.selection_tournament))
