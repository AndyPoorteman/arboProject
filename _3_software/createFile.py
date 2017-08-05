#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             arboProject
   :Nom du fichier:     createFile.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170721

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.6
    :framework:         
    
####

Déscriptif
==========

    :Projet:            Ce projet permet de créer une arboressence de dossier et de sous
                        dossier nécessaires à chaque nouveau projet. Ainsi que l'ensemble
                        des fichiers qui y son ratachés. Il permet également d'initialiser
                        le dépôt Git et l'outil de documentation Sphinx.
                        
    :Fichiers:          createFile.py regroupe le corps de l'ensemble des fichiers qui
                        doivent être créés par défaut avec chaque nouveau projet.

####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Matrice
   
####

"""


#################### Taille maximum des commentaires (90 caracteres)######################

def f_createREADME(*args) :
    """ Retourne les informations pour la création du fichiers 'README.rst' """
    if args :
        v_projectName   = args[0]
        v_fileName      = args[1]
        v_filePath      = args[2]
        
    v_fqfn = f"{v_filePath}/{v_fileName}"
    v_txtData = (
        "======================={}\n".format("="*len(v_projectName))+
        "Informations générales {}\n".format(v_projectName)+
        "======================={}\n\n".format("="*len(v_projectName))+
        ":Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_\n"\
        ":Projet:             {}\n".format(v_projectName)+
        ":dépôt GitHub:       \n"\
        ":documentation:      \n"\
        ":Licence:            CC BY-NC-SA 4.0\n"\
        ":Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/\n\n"\
        "Déscription\n"\
        "===========\n\n"\
        " Saisir ici une brève déscription du projet\n\n"\
        "Arborescence du projet\n"\
        "======================\n\n"\
        "Pour aider à la compréhension de mon organisation,"\
        " voici un bref déscrptif de l'arborescence de se projet."\
        "Cette arborescence est à reproduire si vous récupérez ce"\
        " dépôt depuis GitHub. ::\n\n"\
        "openFile               # Dossier racine du projet (non versionner)\n"\
        "|\n"\
        "+--project             # (branch master) contient l'ensemble du projet en lui même\n"\
        "|  |\n"\
        "|  +--_1_userDoc       # Contien toute la documentation relative au projet\n"\
        "|  |   |\n"\
        "|  |   \\--source       # Dossier réunissant les sources utilisées par Sphinx\n"\
        "|  |\n"\
        "|  +--_2_modelisation  # contien tous les plans et toutes les modélisations du projet\n"\
        "|  |\n"\
        "|  +--_3_software      # Contien toute la partie programmation du projet\n"\
        "|  |\n"\
        "|  \\--_4_PCB           # Contient toutes les parties des circuits imprimés (routage,\n"\
        "|                      # implantation, typon, fichier de perçage, etc\n"\
        "|\n"\
        "\\--webDoc              # Dossier racine de la documentation qui doit être publiée\n"\
        "   |\n"\
        "   \\--html             # (branch gh-pages) C'est dans se dosier que Sphinx vat\n"\
        "                       # générer la documentation à publié sur internet\n\n"
        )
    return  v_fqfn, v_txtData

####
    
    
def f_createInit(*args) :
    """ Retourne les informations pour la création du fichiers '__init__.py' """
    if args :
        v_projectName   = args[0]
        v_fileName      = args[1]
        v_filePath      = args[2]
        
    v_fqfn = f"{v_filePath}/{v_fileName}"
    v_txtData = False
    return  v_fqfn, v_txtData

    ####
    

           
