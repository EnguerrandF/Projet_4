from view import ViewMenu, ViewCreateTournament, ViewTournamentInProgress
from models import Tournament, DataExtractTournament


class Controler:
    def __init__(self):
        self.list_tournement_in_progress = []
        self.player = []

    def main(self):
        answer_view_menu = ViewMenu().main()
        self.test_selection_menu(answer_view_menu)
        self.main()

    def test_selection_menu(self, result_main_page_menu):
        if (result_main_page_menu == "1"):
            # Créer un nouveau tournois
            # Sauvegarder dans la base de donné avec le model Tournaments
            data_tournament = ViewCreateTournament().main()
            print(data_tournament)
            Tournament(data_tournament[0], data_tournament[1], data_tournament[2], data_tournament[3],
                       data_tournament[4], data_tournament[5]).add_tournament_in_data_base()

        elif (result_main_page_menu == "2"):
            # Parcourir les tournois
            tournament_in_progress = ViewTournamentInProgress(DataExtractTournament().return_all_name_tournament())
            result_tournament_in_progress = tournament_in_progress.main()
            print(result_tournament_in_progress)

        elif (result_main_page_menu == "3"):
            print("joueurs sauvegardés")
            return 3
        elif (result_main_page_menu == "4"):
            print("Ajouter un joueur")
            return 4
        elif (result_main_page_menu == "5"):
            print("Aurevoir et a bientôt")
            quit()
        else:
            print()
            input("Le chiffre n'est pas valide")
            self.main()
