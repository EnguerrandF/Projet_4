from view.ViewTournamentInProgress import ViewTournamentInProgress
from view.ViewCreateTournament import ViewCreateTournament
from view.ViewPlayers import ViewCreatePlayer, ViewPlayers
from view.ViewMenu import ViewMenu
from models.models import Tournament, DataTournament, Player, DataPlayer
from .ControlerTournamentInProgress import ControlerTournamentInProgress


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
            # Afficher les joueurs enregistrés
            change_value_player = ViewPlayers(self.list_player_in_data_base).main()
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
            id_tournament_end = DataTournament().return_tournament_end(False)

            if result_menu != "" and result_menu != "0" and result_menu in str(id_tournament_end):
                list_players_score = ControlerTournamentInProgress().players_and_score(result_menu)
                result_report_tournament = tournament_in_progress.report_tournament(result_menu, list_players_score)
                if result_report_tournament == "02":
                    self.answer_view_menu = "5"
                    self.selection_menu()
                elif result_report_tournament == "01":
                    self.answer_view_menu = ""
                else:
                    input("Sélection non valide : ")
                    self.answer_view_menu = "5"
                    self.selection_menu()

            elif result_menu == "01":
                pass
            else:
                input("La sélection n'est pas valide")
                self.answer_view_menu = "5"
                self.selection_menu()

        elif (self.answer_view_menu == "6"):
            print("Aurevoir et a bientôt")
            quit()

        else:
            print()
            input("Le chiffre n'est pas valide")
