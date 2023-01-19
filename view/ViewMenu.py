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
