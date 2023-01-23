# Projet_4
## 1- Sélectionner la commande Git ci-dessous afin de récupérer le projet:
```
    git clone https://github.com/EnguerrandF/Projet_4.git
```

## 2- Accéder au dossier avec la command cd
```
    cd nom_du_dossier
```

## 3- Créer l'environnement virtuel en exécutant la commande ci-dessous:
```
    python -m venv env
```

## 4- Activer l'environnement 
    - Windows:
```
    env/Scripts/activate
```
    - mac et linux:
```
    source venv/bin/activate
```

## 5- Ajoutez-les modules du fichier requirements.txt en executant la commande si dessous:
```
    pip install -r requirements.txt
```

## 6- Maintenant vous pouvez lancer le programme en executant la commande ci-dessous:
```
    python main.py
```

##### Vous pouvez maintenant naviguer dans les menus afin d'ajouter des joueurs et des tournois.
##### Les joueurs non enregistré qui doivent jouer dans un tournoi doit être créés avant la création du tournoi.
##### Faite attention à bien sélectionner les bonnes valeurs afin d'éviter d'éventuels plantages du programme.

## Flake8
##### Pour générer un compte rendu flake8 exécuter la commande ci-dessous dans l'environnement créer au-dessus
```
    flake8 .\controleur\ .\models\ .\view\ .\main.py  --format=html --htmldir=flake-report --max-line-length=120
```