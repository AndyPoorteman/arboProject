#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             arboProject
   :Nom du fichier:     arboProject.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170728

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
                        
    :Fichiers:          arboProject.py : c'est le programme pricipale. On peux le lancer
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

#################### Taille maximum des commentaires (90 caracteres)######################

import os
import shutil
import sys
import argparse
import json

import createFile as cf

class C_Arbo(object) :
    """ 
    Class permettan la Creation d'une arboressence standardisée
    pour chaque nouveau projet
    """
    def __init__(self) :
        self.v_localDir     = os.getcwd()
                                # os.getcwd() : permet de recuperer le chemin
                                # du repertoire local
        self.v_sourceDir    = os.path.normpath(
            "{}/_3-2_sourcesFileToCopy".format( self.v_localDir ))
            
        self._v_logoSourceFQFN     = os.path.normpath(
            "{}/logoVoLAB_200x200.jpg".format(self.v_sourceDir))
        
        self._v_gitInit     = False
        self._v_sphinxInit  = False
        self._v_verbose       = False
        
        self._v_projectName = ""
        self._v_author      = "Poltergeist42"
        
        self._d_arboDir     =   {
                                "000":"/webDoc",
                                "001":"/project",
                                "002":"/project/_1_userDoc_v",
                                "003":"/project/_2_modelization_v",
                                "004":"/project/_3_software_v/_3-1_test_v",
                                "005":"/project/_3_software_v/oldLibVers",
                                "006":"/project/_4_PCB_v",
                                "007":"/project/_5_techDoc_v/_5-1_liensWeb_v",
                                "008":"/project/_6_research_v/_6-1_Etude_Documentation_v",
                                "009":"/project/_6_research_v/_6-2_liensWeb_v",
                                "010":"/project/_6_research_v/_6-3_logiciels_v",
                                "011":"/project/_7_rushes/_7-1_texts_v",
                                "012":"/project/_7_rushes/_7-2_audio_v",
                                "013":"/project/_7_rushes/_7-3_video_v",
                                "014":"/project/_7_rushes/_7-4_pictures",
                                "015":"/project/_7_rushes/_7-5_liensWeb_v",
                                "016":"/project/_3_software_v",
                                "017":"/project/_1_userDoc/source",
                                "018":"/project/_1_userDoc",
                                "019":"/project/_1_userDoc_v/source"
                                }
                                
        self._d_txtFileToCreate   =   {
            "gitignore":(
                        cf.f_createGitignore,
                        self._d_arboDir["001"]),
            "README":(
                        cf.f_createREADME,
                        self._d_arboDir["001"]),
            "VoLAB":(
                        cf.f_createVoLAB,
                        self._d_arboDir["001"]),

            "init":(
                        cf.f_createInit,
                        self._d_arboDir["016"]),

            "BugToDoLst":(
                        cf.f_createBugToDoLst,
                        self._d_arboDir["002"]),

            "make":(
                        cf.f_createMakeBat,
                        self._d_arboDir["002"]),

            "Makefile":(
                        cf.f_createMakefile,
                        self._d_arboDir["002"])
            }

####

    def f_setProjectName( self, v_projectName=None ) :
        """ Permet de définir le nom du projet """
        if v_projectName :
            self._v_projectName = v_projectName
            
        elif __name__ == '__main__':
            v_projectName = input( "entrez le nom du projet : " )
            self._v_projectName = v_projectName
            
####

    def f_getProjectName( self ) :
        """ Permet de récupérer le nom du projet contenu dans '_v_projectName' """
        return self._v_projectName
        
####

    def f_setAuthor( self, v_author) :
        """ Permet de définir un Autheur pour le projet. Par défaut cette valeur est fixé
            à 'Poltergeist42'
        """
        self._v_author = v_author
        
####

    def f_getAuthor (self ) :
        """ Retourne le nom contenu par '_v_author'.
            Par défaut se nom est 'Poltergeist42'
        """
        return self._v_author
####

    def f_getArboDir( self ) :
        return self._d_arboDir
            
####
                            
    def f_dirInit( self ) :
        """ recuperation du repertoire de travail """
        v_localWorkDir = input("Entrez le chemin absolu du dossier projet : ")
        self.v_localDir = os.path.normpath(v_localWorkDir)
        os.chdir(self.v_localDir)
            # Permet de définir le nouveau répertoire de travail

####
        
    def f_dir(self, *t_exeptArgs) :
        """ Creation de la liste des dossiers et de leur sous dossiers """
        for k in self._d_arboDir.keys() :
            if (
                # (k not in t_exeptArgs) or\
                (k not in t_exeptArgs[0])
                ) :
                v_target = self.v_localDir + self._d_arboDir[k]
                if self.f_chkIfDir( v_target ) :
                    pass
                else :
                    if self._v_verbose :
                        print( "Création du dossier : '{}'".format(self._d_arboDir[k]))
                        
                    os.makedirs(os.path.normpath(v_target), mode=0o777, exist_ok=True)
                        # os.makedirs() : Permet de creer le repertoire indiquer par
                        # la variable v_target. Si les repertoires parents n'existent
                        # pas, os.makedirs les creera automatiquement
                        #
                        # os.path.normpath() permet de normaliser la syntaxe du
                        # chemin indiquer par v_target.
                        # N.B : pour windows, les "\\" et '/' seront remplacer
                        # par '\'
            else : pass
                        
####
                            
    def f_chkIfDir(self, v_dir, v_path=None) :
        """ Retourne Vrai si le dossier existe et Faux si il n'éxiste pas.
        
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche serat effectuée.
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
        """ Retourne Vrai si le fichier existe et Faux si il n'éxiste pas.
        
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche serat effectuée.
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
        """ Permet de parcourrir '_d_txtFileToCreate' pour créer les fichiers textes associers
            à chaque item du tuple
        """
        v_projectName   = self.f_getProjectName()
        t_exeptArgs     = args
        for k in self._d_txtFileToCreate.keys() :
            
            if (k not in t_exeptArgs) or (k not in t_exeptArgs[0]) :
                v_filePath = self.v_localDir + self._d_txtFileToCreate[k]["001"]
                
                v_fileName, v_txtData = self._d_txtFileToCreate[k][0]( v_projectName, v_filePath )
                
                self.f_wFile( v_fileName, v_txtData )
            
            else : pass

####

    def f_wFile( self, v_fileName, v_txtData ) :
        """ Permet de créer les fichiers texte dans l'arborescence du projet """
        v_fileName = os.path.normpath(v_fileName)
        with open(v_fileName, 'w', encoding = "utf-8") as i_fileLog :
            if self._v_verbose :
                print( "Création du fichier : '{}'".format(v_fileName))
            if v_txtData :
                i_fileLog.write(v_txtData)
    
####    

    def f_copyFile(self) :
        """ Permet de copier tous les fichiers qui se trouvent dans le dossier
            '_3-2_sourcesFileToCopy' vers leur déstination dans la nouvelle arborescence
        """
        
        for _, _, l_file in os.walk( self.v_sourceDir ) :
            for i in l_file :
                if i[-4] == '.' :
                    print( i[:-4] )
                else :
                    if i[0] == '.' :
                        print( i[1:] )
        
####
            
    def f_copyLogo(self) :
        """ copie du logo dans le repertoire de destination """
        try :
            v_target = self.v_localDir + self._d_arboDir["001"]
            shutil.copy( self._v_logoSourceFQFN, v_target, follow_symlinks=False )
            if self._v_verbose :
                print( "copie du fichier : {} dans : {}".format(self._v_logoSourceFQFN,v_target))
            
            v_logoPathTarget = self.v_localDir + self._d_arboDir["014"]
            shutil.copy( self._v_logoSourceFQFN, v_logoPathTarget, follow_symlinks=False )
            
            if self._v_verbose :
                print( "copie du fichier : {} dans : {}".format(self._v_logoSourceFQFN, v_logoPathTarget))
        
        except FileNotFoundError :
            print( "fichier non trouvé" )
####
            
    def f_gitInit(self) :
        """ initialisation de git """
        if self._v_gitInit :
            os.chdir(self.v_localDir+self._d_arboDir["001"])
            os.system("git init")
            # os.system() : permet d'executer une commande exterieur
        else : pass
                
####
                
    def f_sphinxInit( self ) :
        """ Initialisation de Sphinx """
        if self._v_gitInit :
            os.chdir(self.v_localDir+self._d_arboDir["002"])
            os.system( "sphinx-quickstart -q -p {} -a Poltergeist42 "\
                        "--sep -l fr --ext-autodoc --ext-githubpages "\
                        "--no-makefile --no-batchfile".format( self.f_getProjectName() )
                        )
        else : pass
    
####

    def f_setChangeConf( self ) :
        """ Permet de modifier le fichiers 'conf.py' qui est générer par Sphinx """
        if self._v_sphinxInit :
            v_path = self.v_localDir + self._d_arboDir["019"]
            
            v_tempFile = "{}/tempF".format( v_path )
            v_confFile = "{}/conf.py".format( v_path )
            with open(v_tempFile, 'a', encoding = "utf-8") as tf:
                with open(v_confFile, 'r', encoding = "utf-8") as rm :
                    for l in rm :
                        if l[:-1] == "# import os" :
                            tf.write("import os\n")
                        elif l[:-1] == "# import sys" :
                            tf.write("import sys\n")
                        elif l[:-1] == "# sys.path.insert(0, os.path.abspath('.'))" :
                            tf.write("sys.path.insert(0, os.path.abspath('../../'))\n")
                        elif l[:-1] == "exclude_patterns = []" :
                            tf.write("exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']\n")
                        else :
                            tf.write(l)

            os.remove(v_confFile)
            os.rename(v_tempFile, v_confFile )
            print( "Modification du fichier 'conf.py'" )
        else : pass
    
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
    parser.add_argument( "-s", "--sphinx", action='store_true', help="Initialisation de Sphinx")
    parser.add_argument( "-g", "--git", action='store_true', help="Initialisation de Git")
    parser.add_argument( "-v", "--verbose", action='store_true', help="permet l'affichage du déroulement des opérations")
    parser.add_argument( "-a", "--all", action='store_true', help="active toutes les options d'arboProject")
    parser.add_argument( "-t", "--test", action='store_true', help="permet de tester une methode")
    
    args = parser.parse_args()
    
    # Création d'un tuple contenant l'ensemble des exeptions de dossier
    t_exeptDir = ("016", "017", "018", "019")
        
    # Création d'un tuple contenant l'ensemble des exeptions de fichier
    t_exeptFile = ()
    
    i_arbo = C_Arbo()
    
    if args.verbose or args.all : i_arbo.f_setToggleVerbose()
    if args.sphinx or args.all : i_arbo.f_setToggleSphinxInit()
    if args.git or args.all : i_arbo.f_setToggleGitInit()
    
    i_arbo.f_setProjectName()
    i_arbo.f_dirInit()
    i_arbo.f_dir(t_exeptDir)
    i_arbo.f_sphinxInit()

    i_arbo.f_loopFile(t_exeptFile)
    i_arbo.f_setChangeConf()
    i_arbo.f_copyLogo()
    i_arbo.f_gitInit()
    
    if args.test :
        i_arbo.f_testFunc("f_copyFile" )
        
    input("\n\n\t\tfin de creation de l'arboressence")

if __name__ == '__main__':
    main()
            
