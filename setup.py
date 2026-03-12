# Importing readline to use arrows in input, setting it to import for Mac and Linux but not for Windows otherwise it crashes
# Import de la librairie readline pour utiliser les flèches en le paramétrant pour qu'il soit importé pour Mac et Linux mais pas pour Windows sinon ça crash
import os
if os.name == 'posix' :
    import readline

# Importing the configuration file to choose the language by reading the __init__.py files
# Import du fichier de configuration pour choisir la langue via lecture des fichiers __init__.py
from configparser import ConfigParser
# Importing indent from textwrap so the flags are spaced correctly
# Import de indent dans textwrap pour que les drapeaux soient espacés correctement
from textwrap import indent
# Importing the flags from the flags module to show them in the language selection message
# Import des drapeaux du module flags pour les afficher dans le message de sélection de langue
import flags.flag as flag

# Importing pip library to install the necessary packages
## From what I understood, using pip directly is depracted as it's a security breach so we use subprocess instead to use pip cleanerly
# Import la librairie pip pour installer les paquets nécessaires
## D'après ce que j'ai compris, utiliser pip directement est déconseillé car c'est une faille de sécurité, alors on utilise subprocess à la place pour utiliser pip proprement
import sys
import subprocess


# Defines the necessary packages
# Définis les paquets nécessaires
package1 = 'matplotlib'
package2 = 'mpl_visual_context'
package3 = 'numpy'
package4 = 'typing'
package5 = 'shapely'


# Defines the base content of an .ini file, later defined as "config.ini"
# Définit le contenu de base d'un fichier .ini, plus tard définit comme "config.ini"
code_configur = ConfigParser()
code_configur["language"] = {
    "lang" : ''
}

file_configur = ConfigParser()

# Try to read the file config.ini
# Essaie de lire le fichier config.ini
try :
    file_configur.read('config.ini')
    # Verify the file sections
    # Vérifie les sections du fichier
    for language in code_configur.sections() :
        # Verify there's a [language] section
        # Vérifie qu'il y a une section [language]
        for lang in code_configur[language] :
            # Verify there's a [lang] subsection in [language] section
            # Vérifie qu'il y a une sous-section [lang] dans la section [language] 
            file_configur[language][lang]
except :
    # If at any time, one of the previous lines from the try/except loop fails, create a config.ini file (or overwrites it) with its base configuration
    # Si, à tout moment, une des lignes précédentes de la boucle try/except a une erreur, créer un fichier config.ini (ou l'écrase) avec sa configuration de base
    code_configur.write(open('config.ini', 'w'))

# Read the config.ini files and get its functions
# Lecture du fichier config.ini et récupère ses fonctions
file_configur.read('config.ini')
code_configur.get('language', 'lang')

# This is the message to show to choose the language
## .strip().upper() to avoid issues with case sensitivity and accidental spaces
### .strip() takes care of leading/trailing spaces, and .upper() makes everything uppercase
# C'est le message pour choisir la langue
## .strip().upper() pour éviter les problèmes de casse et d'espaces accidentels
### .strip() gère les espaces au début/à la fin, et .upper() met tout en majuscules
user_lang = input(f"""
    Please choose your language. / Veuillez choisir votre langue.
                  
{indent(flag.final_result_to_call, '       ')}
            EN : English                FR : Français

-> """).strip().upper()




# If the input is neither FR or EN, then the language set up in the file will be English (EN)
## This is a failsafe that could be useful for any languages that gets added later
# Si ce qui est saisi n'est ni FR ni EN, alors la langue configurée dans le fichier sera anglais (EN)
## C'est un secours qui pourrait s'avérer utile si jamais d'autres langues sont ajoutées plus tard
if user_lang not in ["FR", "EN"] :
    user_lang = "EN"

# Set the language and then save the file
# Défini la langue puis sauvegarde le fichier
code_configur.set('language', 'lang', user_lang)
code_configur.write(open('config.ini', 'w'))

# This is the package verification and installation loop for French (FR)
## For more information about \033etc., it's ANSI escape code, fopr more intels, you can check this website : https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
# C'est la boucle de vérification et d'installation des paquets pour le français (FR)
## Pour plus d'informations sur \033etc., c'est du code ANSI escape, pour plus d'infos, vous pouvez consulter ce site : https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
if user_lang == "FR" :
    input("""
            Bonjour. Ce script vérifie que tous les paquets requis sont installés.
            Les paquets requis sont les suivants :
            - matplotlib,
            - mpl-visual-context.
            
            Vous pouvez modifier la langue en modifiant le fichier config.ini via un éditeur de texte ou en exécutant de nouveau ce script.
            Si vous souhaitez installer ces paquets manuellement, vous êtes libre de fermer ce script.
          
            \033[94;5m Veuillez appuyer sur Entrée pour continuer...\033[0;0m
        """)
    def import_or_install() :
        # Tries to import all the packages
        ## If it's successful, print a message saying everything is already installed
        # Essaie d'importer tous les paquets
        ## Si l'import est un succès, affiche un message disant que tout est déjà installé
        try :
            __import__(package1)
            __import__(package2)
            __import__(package3)
            __import__(package4)
            __import__(package5)
            
            input("\033[32;49m Les paquets sont déjà installés, appuyez sur Entrée pour quitter...\033[0;0m")
       
        # If any import fails, print a message saying some packages are missing and will be installed
        ## Install all packages (tried by the past to install only the missing packages but it installed all of them, so I just reverted it to this simpler code)
        # Si n'importe quel import échoue, affiche un message qui dit que certains paquets sont manquants et vont être installés
        ## Installe tous les paquets (j'ai essayé par le passé de faire en sorte que seuls les paquets non installés soient installés, mais ça n'a pas marché alors j'ai remis ce code plus simple) 
        except ImportError :
            input("\033[31;49m Certains paquets sont manquants et vont être installés dans un instant. Veuillez appuyer sur Entrée pour installer les paquets...\033[0;0m")
            print("\033[33;5m Installation en cours...\033[0;0m")

            # Use pip to install packages
            ## Installation using subprocess and -m pip because it's more stable
            # Utilise pip pour installer les paquets
            ## Installation via subprocess et -m pip car c'est plus stable
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package1, package2, package3, package4, package5])

            __import__(package1)
            __import__(package2)
            __import__(package3)
            __import__(package4)
            __import__(package5)
            
            # Prints a message saying that the installation was successful
            # Affiche un message disant que l'installation est terminée
            input("""\033[32;49m
                  Les paquets ont été installés avec succès.
                  Vous pouvez à présent fermer ce script et exécuter main.py.\033[0;0m
                  """)
    
    # Run the function that just was defined
    # Lance la fonction qui vient juste d'être définie
    import_or_install()
            
# This is the package verification and installation loop for English (EN)
## For more information about \033etc., it's ANSI escape code, fopr more intels, you can check this website : https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
# C'est la boucle de vérification et d'installation des paquets pour l'anglais (EN)
## Pour plus d'informations sur \033etc., c'est du code ANSI escape, pour plus d'infos, vous pouvez consulter ce site : https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
elif user_lang == "EN" :
    input("""
            Hello. This script will check if you have the required packages installed.
            The following packages are required:
            - matplotlib,
            - mpl-visual-context.
          
            At any time you can change the language by editing the config.ini file using a text editor or by rerunning this script.
            If you desire to install those packages manually, you're free to close this script.
            
            \033[94;5m Please, press Enter to continue...\033[0;0m
        """)
    def import_or_install() :
        # Tries to import all the packages
        ## If it's successful, print a message saying everything is already installed
        # Essaie d'importer tous les paquets
        ## Si l'import est un succès, affiche un message disant que tout est déjà installé
        try :
            __import__(package1)
            __import__(package2)
            __import__(package3)
            __import__(package4)
            __import__(package5)
            
            input("\033[32;49m Packages already installed, press Enter to close this script...\033[0;0m")
        
        # If any import fails, print a message saying some packages are missing and will be installed
        ## Install all packages (tried by the past to install only the missing packages but it installed all of them, so I just reverted it to this simpler code)
        # Si n'importe quel import échoue, affiche un message qui dit que certains paquets sont manquants et vont être installés
        ## Installe tous les paquets (j'ai essayé par le passé de faire en sorte que seuls les paquets non installés soient installés, mais ça n'a pas marché alors j'ai remis ce code plus simple)
        except ImportError :
            input("\033[31;49m Some packages are missing and will be installed now, press Enter to install packages...\033[0;0m").strip().lower()
            print("\033[33;5m Installation in progress...\033[0;0m")

            # Use pip to install packages
            ## Installation using subprocess and -m pip because it's more stable
            # Utilise pip pour installer les paquets
            ## Installation via subprocess et -m pip car c'est plus stable
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package1, package2, package3, package4, package5])

            __import__(package1)
            __import__(package2)
            __import__(package3)
            __import__(package4)
            __import__(package5)
            
            # Prints a message saying that the installation was successful
            # Affiche un message disant que l'installation est terminée
            input("""\033[32;49m
                  Packages successfully installed.
                  You can now close this script and run main.py.\033[0;0m
                  """)
    
    # Run the function that just was defined
    # Lance la fonction qui vient juste d'être définie
    import_or_install()



# Script by Mathys B.
# Script de Mathys B.

# MIT License :
    # Copyright (c) 2025-2026 Mathys B.

    # Permission is hereby granted, free of charge, to any person obtaining a copy
    # of this software and associated documentation files (the "Software"), to deal
    # in the Software without restriction, including without limitation the rights
    # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    # copies of the Software, and to permit persons to whom the Software is
    # furnished to do so, subject to the following conditions:

    # The above copyright notice and this permission notice shall be included in all
    # copies or substantial portions of the Software.

    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    # SOFTWARE.

