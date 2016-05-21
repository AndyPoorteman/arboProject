#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###(
#   Nom du fichier  : arboProject.py
#   Autheur         : Poltergeist42
#   Version         : 2016.05.21
###

###
#   Licence         : CC-BY-NC-SA
#   Liens           : https://creativecommons.org/licenses/by-nc-sa/4.0/
###

###
#   [ lexique ]
#
#   v_              : variable
#   l_              : list
#   t_              : tuple
#   d_              : dictionnaire
#   f_              : fonction
#   C_              : Class
#   i_              : Instance
#   m_              : Module
###

#################### Taille maximum des commentaires (80 caracteres)######################

import os

class C_Arbo(object) :
    """ 
    Class permettan la Creation d'une arboressence standardise
    pour chaque nouveau projet
    """
    def __init__(self) :
        self.v_localDir = os.getcwd()
                            # os.getcwd() : permet de recuperer le chemin
                            # du repertoire local
        self.v_chkTrueFalse = True
        # print("dbgMsg[02] : ", self.v_localDir)

    def f_dir(self) :
        """ Creation de la liste des dossiers et de leur sous dossiers """
        l_arboDir = [
                    "/01_userDoc_v",
                    "/02_modelization_v",
                    "/03_software_v/3-1_test_v",
                    "/04_PCB_v",
                    "/05_techDoc_v",
                    "/06_research_v/6-1_Etude_Documentation_v",
                    "/06_research_v/6-2_liensWeb_v",
                    "/06_research_v/6-3_logiciels_v",
                    "/07_rushes_v/7-1_texts_v",
                    "/07_rushes_v/7-2_audio_v",
                    "/07_rushes_v/7-3_video_v",
                    "/07_rushes_v/7-4_pictures",
                    "/07_rushes_v/7-5_liensWeb_v"
                    ]
                    
        for i in range(len(l_arboDir)) :
            print(l_arboDir[i])
            v_target = self.v_localDir + l_arboDir[i]
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

    def f_wFile(self, v_fileName) :
        """ Creation des fichiers textes '.gitignore' et README.md' """
        if v_fileName == ".gitignore" :
            v_txtData = (
                        "## [ .gitignore ]\n\n" +
                        "## Liste des fichiers et dossiers à ignorer\n\n" +
                        "#.gitignore\n\n" +
                        "## [ Dossiers a ignorer ]\n" +
                        "03_software/test/\n" +
                        "05_*/\n" +
                        "06_*/\n" +
                        "07_*/\n" +
                        "*_v/\n\n" +
                        "## [ listes des extentions a ignorer ]\n" +
                        "*.*~\n" +
                        "*.FCStd1\n" +
                        "*.264\n" +
                        "*.mkv\n" +
                        "*.mp4\n" +
                        "Thumbs.db"
                        )
        else : v_txtData = (
                        "###\n" +
                        "#\n" +
                        "#   Autheur         : Poltergeist42\n" +
                        "#   Project         : \n" +
                        "#   Licence         : CC BY-NC-SA 4.0\n" +
                        "#   Liens           : https://creativecommons.org/licenses/by-nc-sa/4.0/ \n" +
                        "###\n\n" +
                        "# Saisir ici une breve description du projet"
                        )
                        
        # print("dbgMsg[05] : ", v_txtData)
            
        try :
            i_fileLog = open(v_fileName, 'a')
            i_fileLog.write(v_txtData)
            i_fileLog.close()
        except :
            i_fileLog = open(v_fileName, 'w')
            i_fileLog.write(v_txtData)
            i_fileLog.close()
            
    def f_gitInit(self) :
        """ initialisation de git """
        while self.v_chkTrueFalse :
            print("\n\t\tVoulez-vous initialiser git pour ce projet ?\n")
            v_gitChk = input("\t\tOui (O) / Non (N) : ").upper()
            # print("dbgMsg[06] : ", v_gitChk)
            
            if (v_gitChk == 'N') or (v_gitChk == "NON") :
                self.v_chkTrueFalse = False
                # print("dbgMsg[07-NON] : ", v_gitChk, " - ", self.v_chkTrueFalse)
                
            if (v_gitChk == 'O') or (v_gitChk == "OUI") :
                self.v_chkTrueFalse = False
                os.system("git init")
                            # os.system() : permet d'executer une commande exterieur
                # print("dbgMsg[07-OUI] : ", v_gitChk, " - ", self.v_chkTrueFalse)
               

def main() :
    """ fonction principale """
    i_arbo = C_Arbo()
    i_arbo.f_dir()
    i_arbo.f_wFile(".gitignore")
    i_arbo.f_wFile("README.md")
    i_arbo.f_gitInit()
    print("\n")
    input("fin de creation de l'arboressence")

if __name__ == '__main__':
    main()
            
