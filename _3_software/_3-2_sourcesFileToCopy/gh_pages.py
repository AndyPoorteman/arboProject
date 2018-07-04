#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             arboProject
   :Nom du fichier:     gh_pages.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20180203

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
                        
    :Fichiers:          gh_pages.py est un script permettant de créer la branch 'gh-pages'
                        une fois l'arboressence et le dépôt distant créés. Ce fichier est
                        copié directement dans le dossier 'webDoc' pendant la création de l'arborescence.

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

import os, argparse, time


def main() :
    """ Fonction principale """
    # parser.add_argument( "-t", "--test", action='store_true',
                    # help="permet de tester une methode")
    
    # args = parser.parse_args()
    
    # i_arbo = C_Arbo()
    
    v_url = input( "Entrez l'url du dépôt distant : " )
    
    os.system( f"git clone {v_url} html" )
    time.sleep(2)
    os.chdir( ".\html" )
    os.system( "git branch gh-pages" )
    os.system( "git symbolic-ref HEAD refs/heads/gh-pages" )
    os.system( "del .git\index" )
    os.system( "git clean -fdx" )
    
if __name__ == '__main__':
    main()
            
