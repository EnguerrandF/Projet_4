from view import ViewMenu, ViewCreateTournament, ViewTournamentInProgress
from models import Tournament


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
            # nouveau tournois
            data_tournament = ViewCreateTournament().main()
            self.list_tournement_in_progress.append(data_tournament)

        elif (result_main_page_menu == "2"):
            tournament_in_progress = ViewTournamentInProgress(self.list_tournement_in_progress)
            tournament_in_progress.main()

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
