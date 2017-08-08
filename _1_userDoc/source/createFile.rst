createFile
==========

 .. automodule:: _3_software.createFile
    :members:
    
    
Utilisation :
-------------

    #. Chaque nouvelle fonction ajoutée doit avoir un nom sous la forme :
    
        f_create[nom_du_fichier_sans_extension]
        
        example : ::
        
            f_createREADME
            
        Le nom du fichier correspond à une clef du dictionnaire "_d_txtFileToCreate{}"
        extrait depuis le fichier de configuration "defArbo.json". Cette est elle même un
        dictionnaire.
            
    #. Chaque fonction reçoit 3 argument qui doivent être présenter dans l'ordre suivant :
    
        - v_projectName reçoit "args[0]". C'est le nom du projet qui est fournie par
          l'utilisateur au lancement de l'application.
          
        - v_fileName reçoit args[1]. c'est le nom complet (avec son extension) du fichier
          à créer. Ce nom est récupérer depuis la clef "v_fileName" du dictionnaire
          correspondant au fichier dans le fichier de configuration "defArbo.json".
        
        - v_filePath reçoit args[2]. c'est le chemin relatif du fichier
          à créer. Ce chemin est récupérer depuis la clef "v_filePath" du dictionnaire
          correspondant au fichier dans le fichier de configuration "defArbo.json".
          
    #. Donnée retournée par les fonctions :
    
        Les données retournées par les méthodes sont :
        
        - v_fqfn : c'est le regroupement des 2 variables "v_filePath" et "v_fileName" ::
        
            v_fqfn = f"{v_filePath}/{v_fileName}"
        
        - v_txtData : C'est le corps du fichiers. Si le fichiers est vide, mettre cette
          varriable à False. Si le fichiers doit contenir du texte, il faut le formater
          dans une chaine de caractère (type str)
          
        **N.B** : les fonctions doivent obligatoirement retourner ces 2 variables (dans
        cette ordre) ::
        
            return  v_fqfn, v_txtData