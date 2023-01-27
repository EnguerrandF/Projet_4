from time import gmtime, strftime

from models.models import DataPlayer, DataTournament
from view.ViewTournamentInProgress import ViewTournamentInProgress


class ControlerTournamentInProgress:
    def __init__(self):
        self.db_tournament = DataTournament().return_db()
        self.db_player = DataPlayer().return_db()
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
            self.display_tournament()
        elif self.answer_display_tournament is True:
            self.continue_tournament()

        if str(self.answer_view_menu_tournament_in_progress) != "01":
            self.main()

    def menu_tournament_in_progress(self):
        answer_view_menu_tournament_in_progress = self.view_tournament_in_progress.menu_tournament_in_progress()
        self.answer_view_menu_tournament_in_progress = ""
        if (answer_view_menu_tournament_in_progress in str(DataTournament().return_tournament_end(True)) and
                answer_view_menu_tournament_in_progress != ""):
            self.selection_tournament = int(answer_view_menu_tournament_in_progress)
            self.answer_view_menu_tournament_in_progress = True
        elif len(answer_view_menu_tournament_in_progress) == 2 and answer_view_menu_tournament_in_progress[0] == "0":
            if answer_view_menu_tournament_in_progress[0] == "0" and answer_view_menu_tournament_in_progress[1] == "1":
                print("Retour au Menu")
                self.answer_view_menu_tournament_in_progress = "01"
            elif (answer_view_menu_tournament_in_progress[0] == "0" and
                    answer_view_menu_tournament_in_progress[1] == "2"):
                self.answer_view_menu_tournament_in_progress = ""
        else:
            input("Le chiffre n'est pas valide")
            self.menu_tournament_in_progress()

    def display_tournament(self):
        answer_display_tournament = self.view_tournament_in_progress.display_tournament(self.selection_tournament)

        if (not answer_display_tournament.isdigit() or int(answer_display_tournament) > 3 or
                answer_display_tournament == "0"):
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
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round()
                self.end_round(value_edit_result_first_round, "round_1")
            else:
                self.creation_round(2)
        elif len(self.list_tournament_work()["round"]) == 2:
            if self.list_tournament_work()["round"]["round_2"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_2")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round()
                self.end_round(value_edit_result_first_round, "round_2")
            else:
                self.creation_round(3)
        elif len(self.list_tournament_work()["round"]) == 3:
            if self.list_tournament_work()["round"]["round_3"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_3")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round()
                self.end_round(value_edit_result_first_round, "round_3")
            else:
                self.creation_round(4)
        elif len(self.list_tournament_work()["round"]) == 4:
            if self.list_tournament_work()["round"]["round_4"][4][1] == "":
                self.view_tournament_in_progress.display_match_round(self.list_tournament_work(), "round_4")
                value_edit_result_first_round = self.view_tournament_in_progress.edit_result_round()
                self.end_round(value_edit_result_first_round, "round_4")
            else:
                DataTournament().update_round("status", False, self.selection_tournament)
                self.view_tournament_in_progress.report_tournament(self.selection_tournament,
                                                                   self.players_and_score(self.selection_tournament))
                self.answer_view_menu_tournament_in_progress = "01"
                self.answer_display_tournament = ""

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
        if value_edit_result_first_round == "01":
            self.answer_view_menu_tournament_in_progress = "01"
        elif value_edit_result_first_round == "02" or value_edit_result_first_round is False:
            self.answer_view_menu_tournament_in_progress = "None"
        elif value_edit_result_first_round == "end":
            date_hour_end = strftime("%d %m %Y %H:%M:%S", gmtime())
            list_tournament = self.list_tournament_work()["round"]
            list_tournament[id_round][4][1] = date_hour_end
            DataTournament().update_round("round", list_tournament, self.selection_tournament)
        elif ((value_edit_result_first_round[0] == "0" and value_edit_result_first_round[1] == "1") or
              (value_edit_result_first_round[1] == "0" and value_edit_result_first_round[0] == "1") or
              (value_edit_result_first_round[1] == "0.5" and value_edit_result_first_round[1] == "0.5")):
            list_tournament = self.list_tournament_work()["round"]
            list_tournament[id_round][value_edit_result_first_round[2]][0][1] = float(
                value_edit_result_first_round[0])  # joueur 1
            list_tournament[id_round][value_edit_result_first_round[2]][1][1] = float(
                value_edit_result_first_round[1])  # joueur 2
            DataTournament().update_round("round", list_tournament, self.selection_tournament)
        else:
            input("Le résultat sélectionné n'est pas valide, veuillez sélectionner 0 et 1 ou 0.5 et 0.5 ou 1 et 0")

    def creation_round(self, id_round):
        list_new_match = self.generate_match_round(id_round)
        new_round_for_update = self.list_tournament_work()["round"]
        new_round_for_update["round_" + str(id_round)] = list_new_match
        DataTournament().update_round("round", new_round_for_update, self.selection_tournament)

    def generate_match_round(self, id_round):
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
        list_new_match = []
        for math in range(4):
            i = 0
            for player in range(7):
                match = [int(classement_first_round[0][1][1]), int(classement_first_round[i + 1][1][1])]
                return_match_is_completed = self.check_match_is_not_completed(match)
                if return_match_is_completed is False and len(classement_first_round) > 2:
                    pass
                elif return_match_is_completed is True or len(classement_first_round) == 2:
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
            for match in range(4):
                if self.list_tournament_work()["round"][round][match][0][0][1] == id_player:
                    point_player += self.list_tournament_work()["round"][round][match][0][1]
                if self.list_tournament_work()["round"][round][match][1][0][1] == id_player:
                    point_player += self.list_tournament_work()["round"][round][match][1][1]
        return point_player

    def players_and_score(self, id_tournament):
        self.selection_tournament = id_tournament
        list_player_and_score = []
        for player in self.list_tournament_work()["players"]:
            list_player_and_score.append([int(self.calculate_all_point_one_player(player)), player])
        return list_player_and_score

    def list_tournament_work(self):
        return self.db_tournament.get(doc_id=str(self.selection_tournament))
