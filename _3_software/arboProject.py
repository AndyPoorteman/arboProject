#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     arboProject.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170712

----

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

----

lexique
-------

   :v_:                 variable
   :l_:                 list
   :t_:                 tuple
   :d_:                 dictionnaire
   :f_:                 fonction
   :C_:                 Class
   :i_:                 Instance
   :m_:                 Module
"""

#################### Taille maximum des commentaires (90 caracteres)######################

import os
import shutil
import sys
import argparse

class C_Arbo(object) :
    """ 
    Class permettan la Creation d'une arboressence standardise
    pour chaque nouveau projet
    """
    def __init__(self) :
        self.v_localDir     = os.getcwd()
                                # os.getcwd() : permet de recuperer le chemin
                                # du repertoire local
        self.v_logoPath     = os.path.normpath("C:/mntJeanCloud/Perso/LAB/Pierre/python/projet/arboProject/_7_rushes/_7-4_pictures/logoVoLAB_200x200.jpg")
        
        self._v_gitInit     = False
        self._v_sphinxInit  = False
        
        self._v_projectName  = ""
        
        self.t_lstTxtFile   = (".gitignore", "README.rst", "VoLAB.rst", "__init__.py")
        
        self.l_arboDir =    [
                            "/webDoc",
                            "/project",
                            "/project/_1_userDoc_v",
                            "/project/_2_modelization_v",
                            "/project/_3_software_v/_3-1_test_v",
                            "/project/_3_software_v/oldLibVers",
                            "/project/_4_PCB_v",
                            "/project/_5_techDoc_v/_5-1_liensWeb_v",
                            "/project/_6_research_v/_6-1_Etude_Documentation_v",
                            "/project/_6_research_v/_6-2_liensWeb_v",
                            "/project/_6_research_v/_6-3_logiciels_v",
                            "/project/_7_rushes/_7-1_texts_v",
                            "/project/_7_rushes/_7-2_audio_v",
                            "/project/_7_rushes/_7-3_video_v",
                            "/project/_7_rushes/_7-4_pictures",
                            "/project/_7_rushes/_7-5_liensWeb_v"
                            ]

####

    def f_setProjectName( self, v_projectName=None ) :
        """ Permet de définir le nom du projet """
        if __name__ == '__main__':
            v_projectName = input( "entrez le nom du projet : " )
            
        if v_projectName :
            self._v_projectName = v_projectName

####

    def f_getProjectName( self ) :
        """ Permet de récupérer le nom du projet contenu dans '_v_projectName' """
        return self._v_projectName
            
####
                            
    def f_dirInit(self) :
        """ recuperation du repertoire de travail """
        v_localWorkDir = input("Entrez le chemin absolu du dossier projet : ")
        self.v_localDir = os.path.normpath(v_localWorkDir)
        os.chdir(self.v_localDir)
        print("dbgMsg[03] : ", self.v_localDir)

####
        
    def f_dir(self) :
        """ Creation de la liste des dossiers et de leur sous dossiers """
        for i in range(len(self.l_arboDir)) :
            print(self.l_arboDir[i])
            v_target = self.v_localDir + self.l_arboDir[i]
            # print("dbgMsg[04] : ", os.path.normpath(v_target))
            os.makedirs(os.path.normpath(v_target), mode=0o777, exist_ok=True)
                            # os.makedirs() : Permet de creer le repertoire indiquer par
                            # la variable v_target. Si les repertoires parents n'existent
                            # pas, os.makedirs les creera automatiquement
                            #
                            # os.path.normpath() permet de normaliser la syntaxe du
                            # chemin indiquer par v_target.
                            # N.B : pour windows, les "\\" et '/' seront remplacer
                            # par '\'

####
    
    def f_wFile(self, v_except=None) :
        """ Creation des fichiers textes '.gitignore', 'README.rst' et 'VoLAB.rst' """
        v_projectName = self.f_getProjectName()
        
        for v_fileName in self.t_lstTxtFile :
            print( "dbg : ", v_fileName)
            if v_fileName != v_except :          
                if v_fileName == ".gitignore" :
                    v_txtData = (
                                "## [ .gitignore ]\n\n" +
                                "## Liste des fichiers et dossiers à ignorer\n\n" +
                                "#.gitignore\n\n" +
                                "## [ Dossiers a ignorer ]\n" +
                                "_3_software/_3-1_test*/\n" +
                                "_3_software/oldLibVers*/\n" +
                                "_5_*/\n" +
                                "_6_*/\n" +
                                "_7_*/\n" +
                                "*_v/\n\n" +
                                "## [ listes des extentions a ignorer ]\n" +
                                "*.FCStd1\n" +
                                "*.264\n" +
                                "*.mkv\n" +
                                "*.mp4\n" +
                                "*.json\n\n" +
                                "## Compiled source\n" +
                                "*.com\n" +
                                "*.class\n" +
                                "*.dll\n" +
                                "*.exe\n" +
                                "*.o\n" +
                                "*.so\n" +
                                "*.pyc\n\n" +
                                "## Packages\n" +
                                "*.7z\n" +
                                "*.dmg\n" +
                                "*.gz\n" +
                                "*.iso\n" +
                                "*.jar\n" +
                                "*.rar\n" +
                                "*.tar\n" +
                                "*.zip\n\n" +
                                "## Logs and databases\n" +
                                "*.log\n" +
                                "*.sql\n" +
                                "*.sqlite\n\n" +
                                "## OS generated files\n" +
                                ".DS_Store?\n" +
                                "ehthumbs.db\n" +
                                "Icon?\n" +
                                "Thumbs.db\n" +
                                "*.swp\n" +
                                ".*.swp\n" +
                                "*~\n" +
                                "*.lock\n" +
                                "*.out\n"
                                )
                                
                if v_fileName == "README.rst" :
                    v_txtData = (
                                "======================={}\n".format("="*len(v_projectName))+
                                "Informations générales {}\n".format(v_projectName)+
                                "======================={}\n".format("="*len(v_projectName))+
                                ":Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_\n"+
                                ":Projet:             {}\n".format(v_projectName)+
                                ":dépôt GitHub:       \n"+
                                ":documentation:      \n"+
                                ":Licence:            CC BY-NC-SA 4.0\n"+
                                ":Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/\n\n"+
                                "Description\n"+
                                "===========\n\n"+
                                " Saisir ici une brève déscription du projet\n\n"+
                                "Arborescence du projet\n"+
                                "======================\n\n"+
                                "Pour aider à la compréhension de mon organisation,"+
                                " voici un bref déscrptif de l'arborescence de se projet."+
                                "Cette arborescence est à reproduire si vous récupérez ce"+
                                " dépôt depuis GitHub. ::\n\n"+
                                "openFile                # Dossier racine du projet (non versionner)\n"+
                                "|\n"+
                                "+--project              # (branch master) contient l'ensemble du projet en lui même\n"+
                                "|  |\n"+
                                "|  +--_1_userDoc       # Contien toute la documentation relative au projet\n"+
                                "|  |   |\n"+
                                "|  |   \\--source       # Dossier réunissant les sources utilisées par Sphinx\n"+
                                "|  |\n"+
                                "|  \\--_2_modelisation  # contien tous les plans et toutes les modélisations du projet\n"+
                                "|  |\n"+
                                "|  \\--_3_software      # Contien toute la partie programmation du projet\n"+
                                "|  |\n"+
                                "|  \\--_4_PCB           # Contient toutes les partie des ciercuit imprimés (routage, implantation, typon, fichier\n"+
                                "|                      #de perçage, etc\n"+
                                "|\n"+
                                "\\--webDoc               # Dossier racine de la documentation qui doit être publiée\n"+
                                "|\n"+
                                "\\--html             # (branch gh-pages) C'est dans se dosier que Sphinx vat\n"+
                                "                    # générer la documentation à publié sur internet\n\n"
                                )
                                
                if v_fileName == "VoLAB.rst" :
                    v_txtData = (
                                ".. image:: logoVoLAB_200x200.jpg\n" +
                                "   :align: center\n\n" +
                                "=====\n" +
                                "VoLAB\n" +
                                "=====\n\n" +
                                "Nous connaître\n" +
                                "--------------\n\n" +
                                "   :Le Site Web:       http://www.volab.org \n\n" +
                                "   :Le Wiki:           http://www.vorobotics.com/wiki/index.php?title=Accueil \n\n" +
                                "   :GitHub:            https://github.com/volab \n\n" +
                                "   :Twitter:           https://twitter.com/vorobotics \n\n" +
                                "   :Faceboock:         https://www.facebook.com/VoLab95/ \n\n" +
                                "Qui sommes nous ?\n" +
                                "-----------------\n\n" +
                                "   Le VoLAB, premier FabLab du Val d'Oise, est un FabLab associatif portée par\n" +
                                "   l’associassions VoRoBoTics situé à Vauréal (95480).\n\n" +
                                "   Nous avons pour vocation le partage non marchand des connaissances\n" +
                                "   et l'échange de compétences. Petits et gros projets se côtoient dans divers domaines comme :\n\n"
                                "   Le travail du bois, du métal, l'électronique, la programmation, la sérigraphie,\n" +
                                "   la couture, le scrapbooking et bien d'autres encore.\n\n" +
                                "   Les échanges dynamiques dans la bonne humeur et le respect mutuel permettent\n" +
                                "   à chacun d’appendre et de partager à son rythme\n\n" +
                                "   **N'hésitez pas venir nous rendre visite.**"
                                )
                                
                if v_fileName == "__init__.py" :
                    v_fileName = "_3_software_v/{}".format(v_fileName)
                    v_txtData = False
                    
                if v_fileName == "make.bat" :
                    if not self._v_sphinxInit :
                        pass
                    else :
                        v_fileName = "{}/{}".format(v_fileName)
                        

                v_fileName = "./project/{}".format( v_fileName )
                try :
                    i_fileLog = open(v_fileName, 'a')
                    if v_txtData :
                        i_fileLog.write(v_txtData)
                    # i_fileLog.close()
                except :
                    i_fileLog = open(v_fileName, 'w')
                    if v_txtData :
                        i_fileLog.write(v_txtData)
                    
                finally :
                    i_fileLog.close()
                    pass
                    
                    
            else : pass
    
####    
            
    def f_copyLogo(self) :
        """ copie du logo dans le repertoire de destination """
        v_target = self.v_localDir + self.l_arboDir[1]
        shutil.copy( self.v_logoPath, v_target, follow_symlinks=False )
        v_logoPathTarget = self.v_localDir + self.l_arboDir[14]
        shutil.copy( self.v_logoPath, v_logoPathTarget, follow_symlinks=False )
    
####
            
    def f_gitInit(self) :
        """ initialisation de git """
        if self._v_gitInit :
            os.chdir(self.v_localDir+self.l_arboDir[1])
            os.system("git init")
            # os.system() : permet d'executer une commande exterieur
                
####
                
    def f_sphinxInit( self ) :
        """ Initialisation de Sphinx """
        if self._v_gitInit :
            os.chdir(self.v_localDir+self.l_arboDir[2])
            os.system( "sphinx-quickstart -q -p {} -a Poltergeist42 "\
                        "--sep -l fr --ext-autodoc --ext-githubpages "\
                        "--no-makefile --no-batchfile".format( self.f_getProjectName() )
                        )
    
####

    def f_setSphinx( self ) :
        """ Permet de définir '_v_sphinxInit' à Vrai ou Faux.
            L'état est inversé à chaque appel
        """
        self._v_sphinxInit =  not self._v_sphinxInit
    
####

    def f_setGit( self ) :
        """ Permet de définir '_v_gitInit' à Vrai ou Faux.
            L'état est inversé à chaque appel
        """
        self._v_gitInit =  not self._v_gitInit
    
####
    
    def f_osIdentifier(self) :
        """ Permet d'identifier le type de systeme d'exploitation """
        v_osType = sys.platform
        print( "v_osType = ", v_osType)
        
        if v_osType == 'linux' :
            v_clear = "clear"
            self.v_logoPath = os.path.normpath(
                "/media/polter/JEANCLOUD/Perso/LAB/Pierre/"\
                "python/projet/arboProject/_7_rushes/_7-4_pictures/"\
                "logoVoLAB_200x200.jpg")
        elif  v_osType == "win32" :
            v_clear = "cls"
            self.v_logoPath = os.path.normpath(
                "C:/mntJeanCloud/Perso/LAB/Pierre/"\
                "python/projet/arboProject/_7_rushes/_7-4_pictures/"\
                "logoVoLAB_200x200.jpg")
            
        os.system(v_clear)
        print( "v_osType = ", v_osType)

####
        
def main() :
    """ fonction principale """
    parser = argparse.ArgumentParser()
    parser.add_argument( "-s", "--sphinx", action='store_true', help="Initialisation de Sphinx")
    parser.add_argument( "-g", "--git", action='store_true', help="Initialisation de Git")
                        
    args = parser.parse_args()
    
    i_arbo = C_Arbo()
    i_arbo.f_osIdentifier()
    i_arbo.f_setProjectName()
    
    
    
    if args.sphinx : i_arbo.f_setSphinx()
    if args.git : i_arbo.f_setGit()
        
            
    i_arbo.f_dirInit()
    i_arbo.f_dir()
    i_arbo.f_wFile()
    i_arbo.f_copyLogo()
    i_arbo.f_sphinxInit()
    i_arbo.f_gitInit()
          
    input("\n\n\t\tfin de creation de l'arboressence")

if __name__ == '__main__':
    main()
            
