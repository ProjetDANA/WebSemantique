# Projet DANA



## Accès aux données



Pour pouvoir exécuter des requêtes sur notre jeu de données, il suffit d'être sur le réseau universitaire et de se connecter à :

* [serveur GRP2](http://podman.ensinfo.sciences.univ-nantes.prive:8310/#/)



## Description du dataset



Ce jeu de données provient de la source [All Natural Disasters 1900-2021 (EOSDIS)](https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis/data).

Chaque catastrophe est modélisée sous la forme d'une entité `dbo:Disaster` et `schema:Event`. La forme des données s'articule autour de quatre dimensions principales :

* **Classification** : L'événement est défini par sa catégorie (`schema:category`), son sous-groupe (`ex:disasterSubgroup`), son type (`dbo:type`) et son sous-type (`ex:disasterSubtype`).


* **Temporalité** : L'occurrence est datée avec précision par l'année (`dbo:year`) et le mois de début (`dbo:month`).


* **Géographie** : La localisation inclut les coordonnées (`geo:lat`, `geo:long`), le pays (`dbo:country`), le continent (`dbo:continent`), la région (`dbo:region`) et le code ISO (`dbo:isoCode`).


* **Impact** : Le bilan chiffre le nombre de décès (`dbo:deathToll`), le total des personnes affectées (`ex:totalAffected`) et les dommages financiers (`dbo:damage`).