==================================
Informations générales ArboProject
==================================

:Auteur:            `Poltergeist42 <https://github.com/poltergeist42>`_
:Projet:            ArboProject
:Version:           20181006
:dépôt GitHub:      https://github.com/poltergeist42/arboProject
:documentation:     https://poltergeist42.github.io/arboProject/
:Licence:           CC BY-NC-SA 4.0
:Liens:             https://creativecommons.org/licenses/by-nc-sa/4.0/

####

Description
===========

    Ce projet permet de créer une arborescence de dossier et de sous dossier nécessaires à
    chaque nouveau projet. Ainsi que l'ensemble des fichiers qui y sont rattachés. Il permet
    également d'initialiser le dépôt Git et l'outil de documentation Sphinx.
    
####

Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref descriptif de
l'arborescence de ce projet. Cette arborescence est à reproduire si vous récupérez ce
dépôt depuis GitHub. ::

    ProjectDir_Name        # Dossier racine du projet (non versionner)
    |
    +--project             # (Branch master) contient l'ensemble du projet en lui même
    |  |
    |  +--_1_userDoc       # Contiens toute la documentation relative au projet
    |  |   |
    |  |   \--source       # Dossier réunissant les sources utilisées par Sphinx
    |  |
    |  +--_2_modelisation  # Contiens tous les plans et toutes les modélisations du projet
    |  |
    |  +--_3_software      # Contiens toute la partie programmation du projet
    |  |
    |  +--_4_PCB           # Contient toutes les parties des circuits imprimés (routage,
    |  |                   # Implantation, typon, fichier de perçage, etc.)
    |  |
    |  +--_5_techDoc       # Contiens toutes les documentations techniques des différents composants
    |  |                   # ou éléments qui constituent le projet. Ces éléments sont identifiés
    |  |                   # par un liens Web dans la documentation. Ce dossier n'est pas 'poussé'
    |  |                   # dans le dépôt distant (.gitignore).
    |  |
    |  +--_6_research      # Regroupe toutes les recherches relatives à l'élaboration ou au
    |  |                   # développement du projet. Ces éléments sont identifiés
    |  |                   # par un liens Web dans la documentation. Ce dossier n'est pas 'poussé'
    |  |                   # dans le dépôt distant (.gitignore).
    |  |
    |  \--_7_rushes        # Contient tous les éléments qui seront potentiellement intégrés dans la
    |                      # doc ou dans le projet. Ce dossier n'est pas 'poussé' dans le dépôt
    |                      # distant (.gitignore).
    |
    +--webDoc              # Dossier racine de la documentation qui doit être publiée
    |  |
    |  \--html             # (Branch gh-pages) C'est dans ce dossier que Sphinx va
    |                      # générer la documentation a publié sur internet
    |
    \--trash               # Se dossier sert à retirer des éléments du projet sans les
                           # supprimé réélement. Ce dossier n'est pas pris en compte par
                           # GIT ou par GitHub


