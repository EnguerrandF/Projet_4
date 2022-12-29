from view import ViewMenu, ViewCreateTournament, ViewTournamentInProgress, ViewPlayers, ViewCreatePlayer
from models import Tournament, DataExtractTournament, Player, DataPlayer


class Controler:
    def __init__(self):
        self.list_player_in_data_base = DataPlayer().return_all_player() 
        self.list_tournament_in_progress_data_base = DataExtractTournament().return_all_name_tournament()

    def main(self):
        answer_view_menu = ViewMenu().main()
        self.test_selection_menu(answer_view_menu)
        self.main()

    def test_selection_menu(self, result_main_page_menu):
        if (result_main_page_menu == "1"):
            # Créer un nouveau tournois
            data_tournament = ViewCreateTournament(self.list_player_in_data_base).main()
            Tournament(data_tournament[0], data_tournament[1], data_tournament[2], data_tournament[3],
                       data_tournament[4], data_tournament[5]).add_tournament_in_data_base()

        elif (result_main_page_menu == "2"):
            # Afficher les tournois en cours
            tournament_in_progress = ViewTournamentInProgress(self.list_tournament_in_progress_data_base,
                                                              self.list_player_in_data_base,
                                                              True)
            tournament_in_progress.main()

        elif (result_main_page_menu == "3"):
            # Afficher les joeurs enregistré
            list_player = DataPlayer().return_all_player()
            change_value_player = ViewPlayers(list_player).main()
            if change_value_player is False:
                pass
            else:
                DataPlayer().update_parameter_in_data_base(change_value_player[0],
                                                           change_value_player[1],
                                                           change_value_player[2])

        elif (result_main_page_menu == "4"):
            # Ajouter un joueur
            data_player = ViewCreatePlayer().add_player()
            Player(data_player[0], data_player[1], data_player[2],
                   data_player[3], data_player[4]
                   ).add_player_in_data_base()

        elif (result_main_page_menu == "5"):
            # Afficher les tournois terminé
            tournament_in_progress = ViewTournamentInProgress(self.list_tournament_in_progress_data_base,
                                                              self.list_player_in_data_base,
                                                              False)
            result_tournament_in_progress = tournament_in_progress.main()

        elif (result_main_page_menu == "6"):
            print("Aurevoir et a bientôt")
            quit()

        else:
            print()
            input("Le chiffre n'est pas valide")
            self.main()
