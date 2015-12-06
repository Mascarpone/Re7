# RE7

## Version

1.0

## Prérequis d'installation

* Un système Unix

* Une base de données MySQL à laquelle se connecter

* La bibliothèque `libmysqlclient-dev`, obtenable classiquement avec `sudo apt-get install libmysqlclient-dev`

* Python avec le gestionnaire de modules python `pip` : `sudo apt-get install python-pip`

  Si besoin, une procédure d'installation plus détaillée de pip peut être trouvée ici : http://pip.readthedocs.org/en/stable/installing/

* Le gestionnaire d'environnement virtuel pour python `virtualenv`. Installé par défaut avec les dernières verions de python, mais disponible, s'il n'est pas déjà installé, via votre gestionnaire de paquet préféré, sous le nom `python-virtualenv`, ou via `pip`.

  `sudo apt-get install python-virtualenv`

  ou `sudo pip install virtualenv`

## Installation

Placez vous dans un nouveau dossier dédié au projet re7. Nous l'appellerons `projet_re7` dans la suite.

Décompressez l'archive du projet dans un sous-dossier `re7` ou clonez le dépôt du projet (privé pour l'instant) : `git clone https://github.com/gbea/re7.git`

Éditez la section `# MySQL configurations` du fichier `re7/project/__init__.py` pour donner les bons identifiants d'accès à la base de données MySQL.

Si vous envisagez de travailler sur le dépôt git, désactivez les mises à jour de ce fichier avec `git update-index --assume-unchanged __init__.py`

Le dossier `re7/db_scripts` contient un fichier `createbase.sql` pour créer les tables nécessaires au bon fonctionnement du site, ainsi que `populate.sql` pour ajouter des données d'exemple à la base de données.

Afin de ne pas installer les modules requis directement sur vôtre système, et de ne pas dépendre de la configuration actuelle de celui-ci, nous allons créer un environnement virtuel avec `virtualenv`. Pour cela, utilisez la commande suivante : `virtualenv venv`

Nous disposons donc maintenant d'un environnement situé dans le dossier `venv`. Pour le lancer, utilisez la commande : `. venv/bin/activate` (ne pas oublier le point seul au début)

Pour vous assurer de la bonne activation de l'environnement virtuel, vérifiez que l'invite de commande a bien été modifiée et commence maintenant par `(venv)`. Par exemple `(venv)utilisateur@machine:~/projet_re7`

Nous pouvons maintenant installer toutes les dépendances dans l'environnement virtuel : `pip install -r re7/requirements.txt` (il est possible que les droits d'administrateur soient requis pour cela)

Puis lancer le serveur : `python re7/app.py` (Utilisez Ctrl+C pour le quitter)

Le site re7 est maintenant disponible à l'adresse http://localhost:8000

Pour quitter l'environnement virtuel, Utilisez la commande `deactivate`

Bon appétit !



## Un peu de lecture

http://flask.pocoo.org/docs/0.10/quickstart/

http://jinja.pocoo.org/docs/dev/templates/

http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf
