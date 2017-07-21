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

def f_createGitignore(*args) :
    """ Retourne les informations pour la création du fichiers '.gitignore' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/.gitignore".format( v_filePath)
    v_txtData = (
            "## [ .gitignore ]\n\n"\
            "## Liste des fichiers et dossiers à ignorer\n\n"\
            "#.gitignore\n\n"\
            "## [ Dossiers a ignorer ]\n"\
            "_3_software/_3-1_test*/\n"\
            "_3_software/oldLibVers*/\n"\
            "_5_*/\n"\
            "_6_*/\n"\
            "_7_*/\n"\
            "*_v/\n\n"\
            "## [ listes des extentions a ignorer ]\n"\
            "*.FCStd1\n"\
            "*.264\n"\
            "*.mkv\n"\
            "*.mp4\n"\
            "*.json\n\n"\
            "## Compiled source\n"\
            "*.com\n"\
            "*.class\n"\
            "*.dll\n"\
            "*.exe\n"\
            "*.o\n"\
            "*.so\n"\
            "*.pyc\n\n"\
            "## Packages\n"\
            "*.7z\n"
            "*.dmg\n"\
            "*.gz\n"\
            "*.iso\n"\
            "*.jar\n"\
            "*.rar\n"\
            "*.tar\n"\
            "*.zip\n\n"
            "## Logs and databases\n"\
            "*.log\n"\
            "*.sql\n"\
            "*.sqlite\n\n"\
            "## OS generated files\n"\
            ".DS_Store?\n"\
            "ehthumbs.db\n"\
            "Icon?\n"\
            "Thumbs.db\n"\
            "*.swp\n"\
            ".*.swp\n"\
            "*~\n"\
            "*.lock\n"\
            "*.out\n"
                )
    return  v_fileName, v_txtData
    
####

def f_createREADME(*args) :
    """ Retourne les informations pour la création du fichiers 'README.rst' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/README.rst".format( v_filePath )
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
        "openFile                # Dossier racine du projet (non versionner)\n"\
        "|\n"\
        "+--project              # (branch master) contient l'ensemble du projet en lui même\n"\
        "|  |\n"\
        "|  +--_1_userDoc        # Contien toute la documentation relative au projet\n"\
        "|  |   |\n"\
        "|  |   \\--source       # Dossier réunissant les sources utilisées par Sphinx\n"\
        "|  |\n"\
        "|  \\--_2_modelisation  # contien tous les plans et toutes les modélisations du projet\n"\
        "|  |\n"\
        "|  \\--_3_software      # Contien toute la partie programmation du projet\n"\
        "|  |\n"\
        "|  \\--_4_PCB           # Contient toutes les partie des ciercuit imprimés (routage,"\
        "|                       # implantation, typon, fichier de perçage, etc\n"\
        "|\n"\
        "\\--webDoc              # Dossier racine de la documentation qui doit être publiée\n"\
        "|\n"\
        "\\--html                # (branch gh-pages) C'est dans se dosier que Sphinx vat\n"\
        "                        # générer la documentation à publié sur internet\n\n"
        )
    return  v_fileName, v_txtData

####
    
def f_createVoLAB(*args) :
    """ Retourne les informations pour la création du fichiers 'VoLAB.rst' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/VoLAB.rst".format( v_filePath )
    v_txtData = (
        ".. image:: logoVoLAB_200x200.jpg\n"\
        "   :align: center\n\n"\
        "=====\n"\
        "VoLAB\n"\
        "=====\n\n"\
        "Nous connaître\n"\
        "--------------\n\n"\
        "   :Le Site Web:       http://www.volab.org \n\n"\
        "   :Le Wiki:           http://www.vorobotics.com/wiki/index.php?title=Accueil \n\n"\
        "   :GitHub:            https://github.com/volab \n\n"\
        "   :Twitter:           https://twitter.com/vorobotics \n\n"\
        "   :Faceboock:         https://www.facebook.com/VoLab95/ \n\n"\
        "Qui sommes nous ?\n"\
        "-----------------\n\n"\
        "   Le VoLAB, premier FabLab du Val d'Oise, est un FabLab associatif portée par\n"\
        "   l’associassions VoRoBoTics situé à Vauréal (95480).\n\n"\
        "   Nous avons pour vocation le partage non marchand des connaissances\n"\
        "   et l'échange de compétences. Petits et gros projets se côtoient dans divers domaines comme :\n\n"\
        "   Le travail du bois, du métal, l'électronique, la programmation, la sérigraphie,\n"\
        "   la couture, le scrapbooking et bien d'autres encore.\n\n"\
        "   Les échanges dynamiques dans la bonne humeur et le respect mutuel permettent\n"\
        "   à chacun d’appendre et de partager à son rythme\n\n"\
        "   **N'hésitez pas venir nous rendre visite.**"  
                )
    return  v_fileName, v_txtData
   

####
    
def f_createInit(*args) :
    """ Retourne les informations pour la création du fichiers '__init__.py' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/__init__.py".format(v_filePath)
    v_txtData = False
    return  v_fileName, v_txtData
   

####
    
def f_createBugToDoLst(*args) :
    """ Retourne les informations pour la création du fichiers 'Bug_ToDoLst.rst' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/Bug_ToDoLst.rst".format( v_filePath)
    v_txtData = (
        "================\n"\
        "Bug et ToDo-list\n"\
        "================\n\n"\
        "Déscription\n"\
        "===========\n\n"\
        "    Dans se fichier sont renseigner les bugs identifiés et la liste des choses à faire.\n\n"\
        "    #. Bugs identifiés\n\n"\
        "        A chaque fois qu'un bug est identifés, il doit être renseigner ici si il ne fait\n"\
        "        pas l'objet d'un traitemant immédiat.\n\n"\
        "    #. ToDo-list\n\n"\
        "        Ici doivent être renseigner la liste des tâches à faire. Il s'agit souvent de\n"\
        "        petites choses à fort potentiel d'oublie ou des tâches qui ne peuvent pas faire\n"\
        "        l'objet d'un traitemant immédiat.\n\n"\
        "Model Type\n"\
        "==========\n\n"\
        "    :Date de saisie:        Date à laquelle la problématique à été identifiée\n"\
        "    :Date de traitemant:    Date du traitement de la probélmatique\n"\
        "    :Cible:                 [userDoc, modelisation, software, PCB, autre]\n"\
        "    :Status:                [NONE, WIP, DONE]\n"\
        "    :Problematique:         Déscriptif de la problématique\n"\
        "    :Traitement:            Déscriptif du traitement de la probélmatique\n\n"\
        "{}\n\n".format("-"*90) +
        "Bug identifiés\n"\
        "==============\n\n"\
        "    :Date de saisie:        \n"\
        "    :Date de traitemant:    \n"\
        "    :Cible:                 \n"\
        "    :Status:                \n"\
        "    :Problematique:         \n"\
        "    :Traitement:            \n\n"\
        "{}\n\n".format("-"*90) +
        "ToDo-list\n"\
        "=========\n\n"\
        "    :Date de saisie:        \n"\
        "    :Date de traitemant:    \n"\
        "    :Cible:                 \n"\
        "    :Status:                \n"\
        "    :Problematique:         \n"\
        "    :Traitement:            \n"

                )
    return  v_fileName, v_txtData
   

####
    
def f_createMakeBat(*args) :
    """ Retourne les informations pour la création du fichiers 'make.bat' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/make.bat".format( v_filePath)
    v_txtData = (
        "@ECHO OFF\n\n"\
        "pushd %~dp0\n\n"\
        "REM Command file for Sphinx documentation\n\n"\
        "if \"%SPHINXBUILD%\" == \"\" (\n"\
        "    set SPHINXBUILD=python -msphinx\n"\
        ")\n"
        "set SOURCEDIR=source\n"\
        "set BUILDDIR= ..\\..\\webDoc\n"\
        "set SPHINXPROJ={}\n\n".format( v_projectName ) +
        "if \"%1\" == \"\" goto help\n\n"\
        "%SPHINXBUILD% >NUL 2>NUL\n"\
        "if errorlevel 9009 (\n"\
        "    echo.\n"\
        "    echo.The Sphinx module was not found. Make sure you have Sphinx installed,\n"\
        "    echo.then set the SPHINXBUILD environment variable to point to the full\n"\
        "    echo.path of the 'sphinx-build' executable. Alternatively you may add the\n"\
        "    echo.Sphinx directory to PATH.\n"\
        "    echo.\n"\
        "    echo.If you don't have Sphinx installed, grab it from\n"\
        "    echo.http://sphinx-doc.org/\n"\
        "    exit /b 1\n"\
        ")\n\n"\
        "%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%\n"\
        "rem reconstruction de la branch \"gh-pages\" et mise a jour du depot distant\n"\
        "cd %BUILDDIR%\\html\n"\
        "git add .\n"\
        "git commit -m \"rebuilt docs\"\n"\
        "git push origin gh-pages\n\n"\
        "goto end\n\n"\
        ":help\n"\
        "%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%\n\n"\
        ":end\n"\
        "popd\n"
                )
    return  v_fileName, v_txtData
   

####
    
def f_createMakefile(*args) :
    """ Retourne les informations pour la création du fichiers 'Makefile' """
    if args :
        v_projectName   = args[0]
        v_filePath      = args[1]
        
    v_fileName = "{}/Makefile".format( v_filePath)
    v_txtData = (
        "# Minimal makefile for Sphinx documentation\n\n"\
        "# You can set these variables from the command line.\n"\
        "SPHINXOPTS      = \n"\
        "SPHINXBUILD     = python -msphinx\n"\
        "SPHINXPROJ      = {}\n".format( v_projectName ) +
        "SOURCEDIR       = .\n"\
        "BUILDDIR        = ../../webDoc\n\n"\
        "# Put it first so that 'make' without argument is like 'make help'.\n"\
        "help:\n"\
        "    @$(SPHINXBUILD) -M help \"$(SOURCEDIR)\" \"$(BUILDDIR)\" $(SPHINXOPTS) $(O)\n\n"\
        ".PHONY: help Makefile\n\n"\
        "# Catch-all target: route all unknown targets to Sphinx using the new\n"\
        "# 'make mode' option.  $(O) is meant as a shortcut for $(SPHINXOPTS).\n"\
        "%: Makefile\n"\
        "    @$(SPHINXBUILD) -M $@ \"$(SOURCEDIR)\" \"$(BUILDDIR)\" $(SPHINXOPTS) $(O)\n\n"\
        "# reconstruction de la branch 'gh-pages' et mise a jour du depot distant\n"\
        "buildandcommithtml: html\n\n"\
        "    cd $(BUILDDIR)/html; git add . ; git commit -m \rebuilt docs\"; git push origin gh-pages\n"
                        )
    return  v_fileName, v_txtData
           
