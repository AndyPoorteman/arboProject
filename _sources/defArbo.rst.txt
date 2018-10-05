defArbo.json
============

Ce fichier de configuration permet :
    - de définir de nouveaux fichiers et de nouveau dossiers pour l'arborescence qui 
      doit être créer.

    - de déterminer l'emplacement des fichiers spécifiques de configuration de Sphinx
    
    - de définir les fichiers qui seront copier ainsi que le chemin de déstination des
      ces copie
      
Ce fichier étant au format JSON, l'ensemble se compose de plusieurs dictionnaire avec 
un ensemble de clef / valeur.

Les dictionnaires de fin de chaines ont tous les clef suivantes :

    - "fileName" : permet de spécifier les nom du fichiers avec son extension. Cette 
      clef peut être vide si l'objet traité est un dossier. Cette clef doit être
      renseignées par une chaine de type **str**.
      
    - "alterUsage" : Permet de choisir une condition particulière déterminant
      l'utilisation de la clef "path" ou "alterPath". cette clef n'est pour l'instant
      utilisée que dans le cas de l'utilisation de Sphinx. Cette clef peut être vide si
      il n'y a pas de condition alternative. Cette clef doit être renseignées par une 
      chaine de type **str**.
      
    - "path" : permet de rensigner le ou les chemin relatif de destination de l'objet
      traité. Cette clef est une **liste** qui doit contenir au minimum 1 éléments.
      
    - "alterPath" : Permet d'utiliser des chemins alternatifs. Cet éléments est une **liste**
      Elle peut être vide si l'objet traité ne comprend pas de chemin alternatif.


    #. _d_txtFileToCopy
    
        Ce dictionnaire donne les informations sur chacun des fichiers qui devront être
        copier depuis le dossier "_3-2_sourcesFileToCopy". Chacune des clefs 
        correspond au nom (en valeur absolue) du fichier.
        
        Example :
        
            +----------------+----------------+
            | nom du fichier | valeur absolue |
            +================+================+
            | ".gitignore"   | "gitignore"    |
            +----------------+----------------+
            | "VoLAB.rst"    | "VoLAB"        |
            +----------------+----------------+
            
        Ces clef sont également des dictionnaires. les clef "fileName" et "path" ne
        doivent pas être vide. 
        
            - Pour ne pas copier l'un des fichiers se trouvant dans le
              dossier "_3-2_sourcesFileToCopy" il faut supprimer le dictionnaire
              correspondant du dictionnaire "_d_txtFileToCopy".
            
            - Pour ajouter un fichier, il faut copier la source dans le dossier
              "_3-2_sourcesFileToCopy" et créer le dictionnaire correspondant dans le
              dictionnaire "_d_txtFileToCopy".
        
    #. _d_sphinxCFG
    
        Ce dictionnaire permet de configurer les éléments de Sphinx. Cahque éléments
        est un dictionnaire qui ne doit pas être supprimer.
        
        #. "sphinx"
        
            Ce dictionnaire permet de détermine le chemin relatif ou sera installé
            Sphinx. les clefs "alterUsage" et "path" sont renseignées. Si le chemin par
            défaut ne convient pas, il faut modifier le contenu de la clef "path"
            
        #. "makeBat", "Makefile" et "conf"
        
            Ces dictionnaire permettent de réécrire les fichier "make.bat,
            "Makefile" et "conf.py" qui sont générer lors de l'initialisation de
            Sphinx.
            
            les clefs "v_fileName", "alterUsage" et "path" sont renseignées. Si le 
            chemin par défaut ne convient pas, il faut modifier le contenu de la clef
            "path".
            
    #. _d_txtFileToCreate
    
        Ce dictionnaire permet de créer les fichiers qui correspondent au fonctions
        renseignée dans "createFile.py" chacune des clefs est un dictionnaire don le
        nom correspond à une fonction dans "createFile.py" sans le préfix "f_create".
        
        example :
        
            +--------------------+----------------+
            | Nom de la fonction | Nom de la clef |
            +====================+================+
            | f_createREADME     | "README"       |
            +--------------------+----------------+
            | f_createInit       | "Init"         |
            +--------------------+----------------+
            
        Les clefs "v_fileName" et "path" doivent être renseignées.
        
            - Pour ne pas créer l'un des fichiers il faut supprimer le dictionnaire
              correspondant du dictionnaire "_d_txtFileToCreate".
            
            - Pour ajouter un fichier à créer, il faut créer la fonction
              correspondante dans "createFile.py" et créer le dictionnaire
              correspondant dans le dictionnaire "_d_txtFileToCreate".
            
    #. _d_arboDir
    
        Ce dictionnaire permet de créer l'ensemble de dossier de l'arboresence. Chaque
        clef est un dictionnaire représentant un dossier à créer. Le nom des clef doit
        être renseigner mais n'est pas utiliser spécifiquement. Elle est juste 
        utilisée pour l'itteration du dictionnaire "_d_arboDir" pour chaque clef le 
        dossier renseigner dans "path" sera créer.
        
        - Pour ajouter un nouveau dossier, il faut créer un nouveau dictionnaire dans 
          "_d_arboDir" et renseigner sa clef "path" (chemin relatif).
        
        - Pour supprimer un dossier de l'arborescence à créer, il faut supprimer son 
          dictionnaire de "_d_arboDir".
    
    #. _d_gitCFG
    
        Ce dictionnaire permet de détermine le chemin relatif ou sera installé
        GIT. la clef "path" est renseignée. Si le chemin par défaut ne convient pas,
        il faut modifier le contenu de la clef "path".
