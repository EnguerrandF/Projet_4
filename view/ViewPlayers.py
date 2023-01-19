class ViewPlayers:
    def __init__(self, db_player):
        self.list_tempo = []
        self.value_selection = 999
        self.value_player_selected = 0
        self.db_player = db_player

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
        if (not self.value_selection.isdigit() or int(self.value_selection) > len(self.db_player) or
                self.value_selection == "0"):
            # si id s'électionné est pas valide et que c'est une chaine de caractere
            input("Le chiffre sélectionné n'est pas valide")
            return self.main()
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
        for player in self.db_player.all():
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

        for player in self.db_player.all():
            list_player.append([player["name"], player.doc_id, player["classification"]])
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

        for player in self.db_player.all():
            list_player.append([int(player["classification"]), player["name"], player.doc_id])
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
        self.value_player_selected = int(self.value_selection)
        print(self.value_selection)
        i = 0
        for value in self.db_player.get(doc_id=self.value_selection):
            print(i, value, ":", self.db_player.get(doc_id=self.value_selection)[value])
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
