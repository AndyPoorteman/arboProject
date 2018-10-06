#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             arboProject
   :Nom du fichier:     arboProject.py
   :Auteur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20181006

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev langage:      Python 3.6
    :Framework:         
    
####

Descriptif
==========

    :Projet:            Ce projet permet de créer une arborescence de dossier et de sous
                        dossiers nécessaires à chaque nouveau projet. Ainsi que l'ensemble
                        des fichiers qui y sont rattachés. Il permet également d'initialiser
                        le dépôt Git et l'outil de documentation Sphinx.
                        
    :Fichiers:          arboProject.py : c'est le programme principal. On peut le lancer
                        par la commande : ::
                        
                            python arboProject.py
                            
                        ou utiliser une ou plusieurs options disponibles. Voir les options
                        disponibles avec '--help' ::
                        
                            python arboProject.py --help
                            
                            ou
                            
                            python arboProject.py -h

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

#################### Taille maximum des commentaires (90 caractères)######################

import os
import shutil
import sys
import argparse
import json

try :
    import createFile as cf
    
except ModuleNotFoundError :
    print( "module non trouvé" )

class C_Arbo(object) :
    """ 
    Class permettant la création d'une arborescence standardisée
    pour chaque nouveau projet
    """
    def __init__(self) :
        ## Initialisation des chemins par défaut
        self.v_localDir     = os.getcwd()
                                # os.getcwd() : permet de récupérer le chemin
                                # du répertoire local
        self.v_sourceDir    = os.path.normpath(
            "{}/_3-2_sourcesFileToCopy".format( self.v_localDir ))
            
        ## Création et initialisation des variables globales
        self._v_gitInit     = False
        self._v_sphinxInit  = False
        self._v_verbose     = False
        
        self._v_projectName = ""
        self._v_author      = ""
        self._v_authorSite  = ""
        
        ## Extraction des différents dictionnaires depuis le fichiers 'defArbo.json'
        with open("defArbo.json", 'r', encoding = "utf-8") as f :
            self._d_defArboJson = json.load(f)
        
        self._d_txtFileToCopy       = self._d_defArboJson["_d_txtFileToCopy"]
        self._d_sphinxCFG           = self._d_defArboJson["_d_sphinxCFG"]
        self._d_gitCFG              = self._d_defArboJson["_d_gitCFG"]
        self._d_txtFileToCreate     = self._d_defArboJson["_d_txtFileToCreate"]
        self._d_arboDir             = self._d_defArboJson["_d_arboDir"]
        self._d_credit              = self._d_defArboJson["_d_credit"]

        self.f_setAuthor()
        self.f_setAuthorSite()

####

    def f_setProjectName( self, v_projectName=None ) :
        """ Permet de définir le nom du projet """
        if v_projectName :
            self._v_projectName = v_projectName
            
        elif __name__ == '__main__':
            v_projectName = input( "Entrez le nom du projet : " )
            self._v_projectName = v_projectName
            
####

    def f_getProjectName( self ) :
        """ Permet de récupérer le nom du projet contenu dans '_v_projectName' """
        return self._v_projectName
        
####

    def f_setAuthor( self, v_author=None) :
        """ Permet de définir un Auteur pour le projet. Par défaut cette valeur est fixée
            à 'Poltergeist42'
        """
        if not v_author:
            self._v_author = self._d_credit["v_author"]
        else:
            self._v_author = v_author
        
####

    def f_setAuthorSite( self, v_authorSite=None) :
        """ Permet de définir un Auteur pour le projet. Par défaut cette valeur est fixée
            à 'Poltergeist42'
        """
        if not v_authorSite:
            self._v_authorSite = self._d_credit["v_authorSite"]
        else:
            self._v_authorSite = v_authorSite
        
####
    def f_getAuthor (self ) :
        """ Retourne le nom contenu par '_v_author'.
            Par défaut se nom est 'Poltergeist42'
        """
        return self._v_author
####

    def f_getAuthorSite (self ) :
        """ Retourne le nom contenu par '_v_author'.
            Par défaut se nom est 'Poltergeist42'
        """
        return self._v_authorSite
####

    def f_getArboDir( self ) :
        return self._d_arboDir
            
####
                            
    def f_dirInit( self ) :
        """ récupération du répertoire de travail """
        v_localWorkDir = input("Entrez le chemin absolu du dossier projet : ")
        self.v_localDir = os.path.normpath(v_localWorkDir)
        os.chdir(self.v_localDir)
            # Permet de définir le nouveau répertoire de travail

####
        
    def f_dir(self, *t_exeptArgs) :
        """ Création de la liste des dossiers et de leur sous dossiers.
        
            Ces dossiers sont créés à partir du dictionnaire '_d_arboDir' qui est extrait
            du fichier 'defArbo.json'.
        """
        ## Verbose
        if self._v_verbose :
            print( "** Début de création des dossiers **\n")
            
        for k in self._d_arboDir.keys() :
           
            v_target = self.v_localDir + self._d_arboDir[k]["path"][0]
            if self.f_chkIfDir( v_target ) :
                pass
            else :
            
                ## Verbose
                if self._v_verbose :
                    print( f"\t* Création du dossier : {self._d_arboDir[k]['path'][0]}")
                    
                os.makedirs(os.path.normpath(v_target), mode=0o777, exist_ok=True)
                    # os.makedirs() : Permet de créer le répertoire indiquer par
                    # la variable v_target. Si les répertoires parents n'existent
                    # pas, os.makedirs les créera automatiquement
                    #
                    # os.path.normpath() permet de normaliser la syntaxe du
                    # chemin indiquer par v_target.
                    # N.B : pour Windows, les "\\" et '/' seront remplacer
                    # par '\'
        
        ## Verbose
        if self._v_verbose :
            print( "** Fin de création des dossiers **\n")
                        
####
                            
    def f_chkIfDir(self, v_dir, v_path=None) :
        """ Retourne Vrai si le dossier existe et Faux s’il n'existe pas.
        
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche sera effectuée.
        """
        if not v_path :
            v_path = '.'
        
        v_chk = False
        for _, l_dir, _ in os.walk( v_path ) :
            for i in l_dir :
                if i == v_dir :
                    v_chk = True
                    return True

            if not v_chk :
                return False
                            
####
                            
    def f_chkIfFile(self, v_file, v_path=None) :
        """ Retourne Vrai si le fichier existe et Faux s’il n'existe pas.
        
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche sera effectuée.
        """
        if not v_path :
            v_path = '.'
        
        v_chk = False
        for _, _, l_file in os.walk( v_path ) :
            for i in l_file :
                if i == v_file :
                    v_chk = True
                    return True

            if not v_chk :
                return False
                            
####
    
    def f_loopFile(self, *args, **kwargs) :
        """ Permet de parcourir '_d_txtFileToCreate' pour créer les fichiers textes
        associés à chaque clef.
        
        Ces fichiers sont créés à partir du dictionnaire '_d_txtFileToCreate' qui est
        extrait du fichier 'defArbo.json'.
        """
        ## Verbose
        if self._v_verbose :
            print( "** Début de création des fichiers**\n")
            
        v_projectName   = self.f_getProjectName()
        t_exeptArgs     = args

        v_author        = self.f_getAuthor()
        v_authorSite    = self.f_getAuthorSite()
        v_licence       = self._d_credit["v_licence"]
        v_licenceLink   = self._d_credit["v_licenceLink"]


        for k in self._d_txtFileToCreate.keys() :
            
            v_exec = f"cf.f_create{k}"
            v_fqfn, v_txtData = eval( v_exec )(   self.f_getProjectName(),
                                    self._d_txtFileToCreate[k]["v_fileName"],
                                    self._d_txtFileToCreate[k]["path"][0],
                                    v_author,
                                    v_authorSite,
                                    v_licence,
                                    v_licenceLink
                                )
            v_fqfn = os.path.normpath( f"{self.v_localDir}{v_fqfn}" )
            self.f_wFile( v_fqfn, v_txtData )
                            
        ## Verbose
        if self._v_verbose :
            print( "** Fin de création des fichiers**\n")

####

    def f_wFile( self, v_fileName, v_txtData ) :
        """ Permet de créer les fichiers texte dans l'arborescence du projet """
        v_fileName = os.path.normpath(v_fileName)
        with open(v_fileName, 'w', encoding = "utf-8") as i_fileLog :
            
            if v_txtData :
                i_fileLog.write(v_txtData)

            ## Verbose
            if self._v_verbose :
                print( f"\t* Création du fichier : '{v_fileName}'")

####    

    def f_copyFile(self) :
        """ Permet de copier tous les fichiers qui se trouvent dans le dossier
            '_3-2_sourcesFileToCopy' vers leur destination dans la nouvelle arborescence
        """
        ## Verbose
        if self._v_verbose :
            print( "** Début de copie des fichiers**\n")
            
        v_workDir = self.v_localDir
        for _, _, l_file in os.walk( self.v_sourceDir ) :
            for i in l_file :
            
                if i[0] == '.' : i = i[1:]
                if i[-2]== '.' : i = i[:-2]
                if i[-3]== '.' : i = i[:-3]
                if i[-4]== '.' : i = i[:-4]
                
                fileName = alterUsage = path = alterPath = None
                fileName = self._d_txtFileToCopy[i]["fileName"]
                alterUsage = self._d_txtFileToCopy[i]["alterUsage"]
                path = self._d_txtFileToCopy[i]["path"]
                alterPath = self._d_txtFileToCopy[i]["alterPath"]

                if alterUsage == "sphinx" and self._v_sphinxInit :
                    v_path = alterPath
                
                elif alterUsage == "git" and self._v_gitInit :
                    v_path = alterPath
                
                else :
                    v_path = path
                    
                v_source = os.path.normpath(self.v_sourceDir + "/" + fileName)

                for id in range(len(v_path)) :
                    v_target = os.path.normpath(v_workDir + v_path[id])

                    try:
                        shutil.copy(v_source, v_target)
                        
                        ## Verbose
                        if self._v_verbose :
                            print( 
                                f"\t* copie du fichier : {fileName}"\
                                f" dans le répertoire : {v_path[id]}")
                            
                    except shutil.Error as e:
                        print(f"Error: {e}")
                    # eg. source or destination doesn't exist
                    except IOError as e:
                        print(f"Error: {e.strerror}")
                        
        ## Verbose
        if self._v_verbose :
            print( "** Fin de copie des fichiers**\n")

####
            
    def f_gitInit(self) :
        """ initialisation de git """
        if self._v_gitInit :
            ## Verbose
            if self._v_verbose :
                print("** Début d'initialisation de GIT **\n")
                
            os.chdir(self.v_localDir+self._d_gitCFG["path"][0])
            os.system("git init")
            os.chdir(self.v_localDir)
            
            ## Verbose
            if self._v_verbose :
                print("** Fin d'initialisation de GIT **\n")

        else : pass
                
####
                
    def f_sphinxInit( self ) :
        """ Initialisation de Sphinx """
        if self._v_sphinxInit :
            ## Verbose
            if self._v_verbose :
                print("** Début d'initialisation de Sphinx **\n")
                
            os.chdir(self.v_localDir+self._d_sphinxCFG["sphinx"]["path"][0])
            os.system( "sphinx-quickstart -q -p {} -a {} "\
                        "--sep -l fr --ext-autodoc --ext-githubpages "\
                        "--no-makefile --no-batchfile".format(  self.f_getProjectName(),
                                                                self.f_getAuthor())
                        )
            v_fqfn, v_txtData = self.f_createMakeBat(   self.f_getProjectName(),
                                    self._d_sphinxCFG["makeBat"]["v_fileName"],
                                    self._d_sphinxCFG["makeBat"]["path"][0]
                                )
            v_fqfn = os.path.normpath( f"{self.v_localDir}{v_fqfn}" )
            self.f_wFile( v_fqfn, v_txtData )
            
            v_fqfn, v_txtData = self.f_createMakefile(   self.f_getProjectName(),
                                    self._d_sphinxCFG["Makefile"]["v_fileName"],
                                    self._d_sphinxCFG["Makefile"]["path"][0]
                                )
                                
            v_fqfn = os.path.normpath( f"{self.v_localDir}{v_fqfn}" )
            self.f_wFile( v_fqfn, v_txtData )

            self.f_setChangeConf()
            os.chdir(self.v_localDir)
                            
            ## Verbose
            if self._v_verbose :
                print("** Fin d'initialisation de Sphinx **\n")
                
        else : pass
    
####

    def f_setChangeConf( self, v_relativPath = False ) :
        """ Permet de modifier le fichiers 'conf.py' qui est générer par Sphinx.
            Le chemin relatif par défaut est : '../../'.
            Cette valeur est à modifier (v_relativPath)si l'arborescence utilisée est
            différente de l'arborescence par défaut. 
            
            Cette Méthode est appelée par : 'f_sphinxInit'.
        """
        if not v_relativPath :
            v_relativPath = "../../"
        
        if self._v_sphinxInit :
            v_path = self.v_localDir + self._d_sphinxCFG["conf"]["path"][0]
            v_tempFile = f"{v_path}/tempF"
            v_confFile = f"{v_path}/{self._d_sphinxCFG['conf']['v_fileName']}"
            with open(v_tempFile, 'a', encoding = "utf-8") as tf:
                with open(v_confFile, 'r', encoding = "utf-8") as rm :
                    for l in rm :
                        if l[:-1] == "# import os" :
                            tf.write("import os\n")
                        elif l[:-1] == "# import sys" :
                            tf.write("import sys\n")
                        elif l[:-1] == "# sys.path.insert(0, os.path.abspath('.'))" :
                            tf.write(f"sys.path.insert(0, os.path.abspath(\"{v_relativPath}\"))\n")
                        elif l[:-1] == "exclude_patterns = []" :
                            tf.write("exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']\n")
                        elif l[:-1] == "html_theme = 'alabaster'" :
                            tf.write("html_theme = 'classic'\n")
                        else :
                            tf.write(l)

            os.remove(v_confFile)
            os.rename(v_tempFile, v_confFile )
            
            ## Verbose
            if self._v_verbose :
                print( "\t* Modification du fichier 'conf.py'" )
                
        else : pass
    
####

    def f_createMakeBat(self, *args, **kwargs) :
        """ Retourne les informations pour la création du fichiers 'make.bat'.
            Si le chemin de destination est différent du dossier par défaut
            ('..\\..\\webDoc\\'), il faut passer un quatrième argument sous la forme d'une
            chaine de caractère représentant le chemin relatif vers le nouveau dossier de
            destination.
        
            Cette Méthode est appelée par : 'f_sphinxInit'. Ce fichier faisant parti des
            fichiers de configuration de Sphinx, il n'est pas généré depuis 'createFile'.
        """
        if args :
            v_projectName   = args[0]
            v_fileName      = args[1]
            v_filePath      = args[2]
            if len(args) == 4 :
                v_buildir   = args[3]
            else :
                v_buildir   = "..\\..\\webDoc"
            
        v_fqfn = f"{v_filePath}/{v_fileName}"
        v_txtData = (
            "@ECHO OFF\n\n"\
            "pushd %~dp0\n\n"\
            ":: Command file for Sphinx documentation\n\n"\
            "if \"%SPHINXBUILD%\" == \"\" (\n"\
            "    set SPHINXBUILD=python -msphinx\n"\
            ")\n"
            "set SOURCEDIR=source\n"\
            "set BUILDDIR= {}\n"\
            "set SPHINXPROJ={}\n\n".format( v_buildir, v_projectName ) +
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
            "\n\n"\
            ":: recupération de la branch active dans la variable : \"v_branch\"\n"\
            "for /f %%i in ('git symbolic-ref HEAD --short') do set v_branch=%%i\n"\
            "\n\n"\
            "if %v_branch% == master (\n"\
            "    echo.\n"\
            "    echo ************************************\n"\
            "    echo.\n"\
            "    echo branch : %v_branch%.\n"\
            "    echo Envoie de la doc vers gh-pages\n"\
            "    echo.\n"\
            "    echo ************************************\n"\
            "    echo.\n"\
            "    \n\n"\
            "    :: reconstruction de la branch \"gh-pages\" et mise a jour du depot distant\n"\
            "    cd %BUILDDIR%\html\n"\
            "    git add .\n"\
            "    git commit -m \"rebuilt docs\"\n"\
            "    git push origin gh-pages\n"\
            "    \n\n"\
            "    goto end\n"\
            ") else (\n"\
            "    echo.\n"\
            "    echo ************************************\n"\
            "    echo.\n"\
            "    echo Branch : %v_branch%\n"\
            "    echo La doc reste en local\n"\
            "    echo.\n"\
            "    echo ************************************\n"\
            "    echo.\n"\
            "    \n\n"\
            "    goto end\n"\
            ")\n\n"\
            ":end\n"\
            "popd\n"
                    )
        return  v_fqfn, v_txtData
   
####
    
    def f_createMakefile(self, *args, **kwargs) :
        """ Retourne les informations pour la création du fichiers 'Makefile'.
            Si le chemin de destination est différent du dossier par défaut
            ('..\..\webDoc\'), il faut passer un quatrième argument sous la forme d'une
            chaine de caractère représentant le chemin relatif vers le nouveau dossier de
            destination.
        
            Cette Méthode est appelée par : 'f_sphinxInit'. Ce fichier faisant parti des
            fichiers de configuration de Sphinx, il n'est pas généré depuis 'createFile'.        """
        if args :
            v_projectName   = args[0]
            v_fileName      = args[1]
            v_filePath      = args[2]
            if len(args) == 4 :
                v_buildir = args[3]
            else :
                v_buildir = "../../webDoc"
            
        v_fqfn = f"{v_filePath}/{v_fileName}"
        v_txtData = (
            "# Minimal makefile for Sphinx documentation\n\n"\
            "# You can set these variables from the command line.\n"\
            "SPHINXOPTS      = \n"\
            "SPHINXBUILD     = python -msphinx\n"\
            "SPHINXPROJ      = {}\n".format( v_projectName ) +
            "SOURCEDIR       = .\n"\
            f"BUILDDIR        = {v_buildir}\n\n"\
            "# Put it first so that 'make' without argument is like 'make help'.\n"\
            "help:\n"\
            "    @$(SPHINXBUILD) -M help \"$(SOURCEDIR)\" \"$(BUILDDIR)\" $(SPHINXOPTS) $(O)\n\n"\
            ".PHONY: help Makefile\n\n"\
            "# Catch-all target: route all unknown targets to Sphinx using the new\n"\
            "# 'make mode' option.  $(O) is meant as a shortcut for $(SPHINXOPTS).\n"\
            "%: Makefile\n"\
            "    @$(SPHINXBUILD) -M $@ \"$(SOURCEDIR)\" \"$(BUILDDIR)\" $(SPHINXOPTS) $(O)\n\n"\
            "# reconstruction de la branch 'gh-pages' et mise à jour du dépôt distant\n"\
            "buildandcommithtml: html\n\n"\
            "    cd $(BUILDDIR)/html; git add . ; git commit -m \rebuilt docs\"; git push origin gh-pages\n"
                            )
        return  v_fqfn, v_txtData

####

    def f_setToggleSphinxInit( self ) :
        """ Permet de définir '_v_sphinxInit' à Vrai ou Faux.
            L'état est inversé à chaque appel
        """
        self._v_sphinxInit =  not self._v_sphinxInit
    
####

    def f_setToggleGitInit( self ) :
        """ Permet de définir '_v_gitInit' à Vrai ou Faux.
            L'état est inversé à chaque appel
        """
        self._v_gitInit =  not self._v_gitInit
    
####

    def f_setToggleVerbose( self ) :
        """ Permet de définir '_v_gitInit' à Vrai ou Faux.
            L'état est inversé à chaque appel
        """
        self._v_verbose =  not self._v_verbose
    
####

    def f_testFunc(self, *args, **kwargs ) :
        """ Cette méthode permet de tester méthode pour éviter de devoir modifier la
            séquence exécutée dans le 'main’. Elle s'active avec l'option -t ou --test.
        """
        print( "\n\t\t ## f_testFunc ##\n" )
        print("args\t: ",args)
        print("kwargs\t: ", kwargs)
        for i in args :
            print( "i\t: ", i )
            v_exec = "self.{}".format(i)
            print( "v_exec\t: ", v_exec )
            eval( v_exec )()
        
def main() :
    """ fonction principale """
    parser = argparse.ArgumentParser()
    parser.add_argument( "-s", "--sphinx", action='store_true',
                        help="Initialisation de Sphinx")
    
    parser.add_argument( "-g", "--git", action='store_true',
                        help="Initialisation de Git")
    
    parser.add_argument( "-v", "--verbose", action='store_true',
                        help="permet l'affichage du déroulement des opérations")
    
    parser.add_argument( "-a", "--all", action='store_true',
                        help="active toutes les options d'arboProject")

    parser.add_argument( "-t", "--test", action='store_true',
                        help="permet de tester une méthode")
    
    args = parser.parse_args()
    
    i_arbo = C_Arbo()
    
    if args.verbose or args.all : i_arbo.f_setToggleVerbose()
    if args.sphinx or args.all : i_arbo.f_setToggleSphinxInit()
    if args.git or args.all : i_arbo.f_setToggleGitInit()
    
    i_arbo.f_setProjectName()
    i_arbo.f_dirInit()
    i_arbo.f_dir()
    i_arbo.f_sphinxInit()

    i_arbo.f_loopFile()
    i_arbo.f_copyFile()
    i_arbo.f_gitInit()
    
    if args.test :
        i_arbo.f_testFunc("" )
        
    input("\n\t\tfin de création de l'arborescence")

if __name__ == '__main__':
    main()
            

