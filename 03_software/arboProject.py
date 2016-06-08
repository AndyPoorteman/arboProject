#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     arboProject.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            2016.06.07

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
                    "/05_techDoc_v/5-1_liensWeb_v",
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
                        "03_software/3-1_test*/\n" +
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
                        
        if v_fileName == "README.rst" :
            v_txtData = (
                        "=========================\n" +
                        "saisir le titre du projet\n" +
                        "=========================\n\n" +
                        "   :Autheur:          `Poltergeist42 <https://github.com/poltergeist42>`_\n" +
                        "   :Projet:          \n" +
                        "   :Licence:          CC BY-NC-SA 4.0\n" +
                        "   :Liens:            https://creativecommons.org/licenses/by-nc-sa/4.0/ \n\n" +
                        "------------------------------------------------------------------------------------------\n\n" +
                        "Description\n" +
                        "-----------\n\n" +
                        " Saisir ici une breve description du projet"
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
    i_arbo.f_wFile("README.rst")
    i_arbo.f_wFile("VoLAB.rst")
    i_arbo.f_gitInit()
    print("\n\n Pensez à copier l'image \"logoVoLAB_200x200.jpg\" \n a la racine de votre arborescence\n\n")
          
    input("fin de creation de l'arboressence")

if __name__ == '__main__':
    main()
            
