# Importing readline to use arrows in input, setting it to import for Mac and Linux but not for Windows otherwise it crashes
# Import de la librairie readline pour utiliser les flèches en le paramétrant pour qu'il soit importé pour Mac et Linux mais pas pour Windows sinon ça crash
import os
if os.name == 'posix' :
    import readline

# Importing the configuration file to choose the language by reading the __init__.py files
# Import du fichier de configuration pour choisir la langue via lecture des fichiers __init__.py
from configparser import ConfigParser

# Importing Mathplotlib libraries
# Import de librairies Mathplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


# Reading the config.ini file and importing its settings
# Lecture du fichier config.ini et import de ses paramètres
configur = ConfigParser()
configur.read('config.ini')
lang = configur.get('language', 'lang')
if lang == "FR" :
    # Importing FR folder
    # Import du dossier FR
    from FR.input_data import ax
    import FR.input_data as input_data
elif lang == "EN" :
    # Importing EN folder
    # Import du dossier EN
    from EN.input_data import ax
    import EN.input_data as input_data
else :
    # Setting the language in the config.ini file
    ## If somehow, lang is neither EN or FR in the config.ini file, tells the user to rerun the setup.py script and then close this script
    # Définition de la langue dans le fichier config.ini
    ## Si, d'une quelconque façon, lang n'est ni FR ni EN dans le fichier config.ini, dit à l'utilisateur de relancer le script setup.py puis ferme ce script
    input("""
    No supported languages detected, please rerun setup.py and then run main.py again;
    Aucune langue prise en charge n'a été détectée, veuillez relancer setup.py puis exécuter de nouveau main.py.
    """)
    quit()


# Running the input_data.py file to get the graph's data
# Exécution du fichier input_data.py pour obtenir les données du graphique
input_data

# Configuring the graph's axes ticks
## One tick every 1 cm and 9 minor ticks between each major tick
# Configuration des graduations du graphique
## Une graduation tous les 1 cm et 9 petites graduations entre chaque grande graduation
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))

# Hides the x-axis and then inverts the y-axis
# Masque l'axe des abscisses puis inverse l'axe des ordonnées
ax.get_xaxis().set_visible(False)
ax.invert_yaxis()

# Set up the graph's title and the y-axis title
# Configure le titre du graphique et le titre de l'axe des ordonnées
if lang == "FR" :
    plt.title(input("Entrez le titre du graphique : "))
    plt.ylabel("Échelle (en cm)", style = 'italic', loc = 'center')
elif lang == "EN" :
    plt.title(input("Type here your graph's title: "))
    plt.ylabel("Scale (in cm)", style = 'italic', loc = 'center')

# Show the graph
# Affiche le graphique
plt.show()


# Script by Mathys B.
# Script de Mathys B.

# MIT License :
    # Copyright (c) 2025 Mathys B.

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

