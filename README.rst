==================================
Informations générales ArboProject
==================================

:Auteur:            `Poltergeist42 <https://github.com/poltergeist42>`_
:Projet:             ArboProject
:dépôt GitHub:       https://github.com/poltergeist42/arboProject
:documentation:      https://poltergeist42.github.io/arboProject/
:Licence:            CC BY-NC-SA 4.0
:Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

   
------------------------------------------------------------------------------------------

Description
===========

    Ce projet permet de créer une arborescence de dossier et de sous dossier nécessaires à
    chaque nouveau projet. Ainsi que l'ensemble des fichiers qui y sont rattachés. Il permet
    également d'initialiser le dépôt Git et l'outil de documentation Sphinx.
    
Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref descriptif de
l'arborescence de ce projet. Cette arborescence est à reproduire si vous récupérez ce
dépôt depuis GitHub. ::

    openFile               # Dossier racine du projet (non versionner)
    |
    +--project             # (branch master) contient l'ensemble du projet en lui même
    |  |
    |  +--_1_userDoc       # Contiens toute la documentation relative au projet
    |  |   |
    |  |   \--source       # Dossier réunissant les sources utilisées par Sphinx
    |  |
    |  +--_2_modelisation  # Contiens tous les plans et toutes les modélisations du projet
    |  |
    |  +--_3_software      # Contiens toute la partie programmation du projet
    |  |
    |  \--_4_PCB           # Contient toutes les parties des circuits imprimés (routage,
    |                      # implantation, typon, fichier de perçage, etc.
    |
    \--webDoc              # Dossier racine de la documentation qui doit être publiée
       |
       \--html             # (branch gh-pages) C'est dans ce dossier que Sphinx vat
                           # générer la documentation a publié sur internet


