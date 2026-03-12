# Importing readline to use arrows in input, setting it to import for Mac and Linux but not for Windows otherwise it crashes
# Import de la librairie readline pour utiliser les flèches en le paramétrant pour qu'il soit importé pour Mac et Linux mais pas pour Windows sinon ça crash
import os
if os.name == 'posix' :
    import readline

# Importing the configuration file to choose the language by reading the __init__.py files
# Import du fichier de configuration pour choisir la langue via lecture des fichiers __init__.py
from configparser import ConfigParser

# For colors, see ANSI escape code on github https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
## [0;0m" resets colors, [1;31;49m" is red, [1;34;49m" is blue and [1;37;49m" is white, the characters after a code are the colorized characters
# Pour les couleurs, voir ANSI escape code sur github https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
## [0;0m" réinitialise les couleurs, [1;31;49m" est rouge, [1;34;49m" est bleu et [1;37;49m" est blanc, les caractères après un code est le caractère colorisé
red = "\033[1;31;49m#\033[0;0m"
blue = "\033[1;34;49m%\033[0;0m"
white = "\033[1;37;49m+\033[0;0m"

GB_flag = """
+##++%%%%+###+%%%%+##++
%+##++%%%+###+%%%+##++%
%%+##++%%+###+%%+##++%%
%%%+##++%+###+%+##++%%%
%%%%+##+++###++##++%%%%
++++++++++###++++++++++
#######################
#######################
++++++++++###++++++++++
%%%%++##++###+++##+%%%%
%%%++##+%+###+%++##+%%%
%%++##+%%+###+%%++##+%%
%++##+%%%+###+%%%++##+%
++##+%%%%+###+%%%%++##+
"""

FR_flag = """
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
%%%%%%%%++++++++########
"""

# Check for a specific character in the flag strings and replace it with the corresponding color variable
## First block is for the GB flag, second block is for the FR flag
# Vérifie la présence d'un caractère spécifique dans les blocs de strings des drapeaux et le remplace par la variable de couleur correspondante
## Le premier bloc est pour le drapeau GB, le second bloc est pour le drapeau FR
if '#' in GB_flag :
    GB_flag = GB_flag.replace('#', red)
if '%' in GB_flag :
    GB_flag = GB_flag.replace('%', blue)
if '+' in GB_flag :
    GB_flag = GB_flag.replace('+', white)

if '#' in FR_flag :
    FR_flag = FR_flag.replace('#', red)
if '%' in FR_flag :
    FR_flag = FR_flag.replace('%', blue)
if '+' in FR_flag :
    FR_flag = FR_flag.replace('+', white)

def aligned_flags():
    # Returns GB and FR flags aligned side-by-side on the same lines
    # Retourne les drapeaux GB et FR alignés côte à côte sur les mêmes lignes
    GB_lines = [line for line in GB_flag.split('\n') if line.strip()]
    FR_lines = [line for line in FR_flag.split('\n') if line.strip()]
    
    # Calculates the max length of the GB flag because it's the first flag to be drawn
    ## I need to know this length to be able to put the FR flag next to it
    # Calcul la longueur max du drapeau anglais car c'est le premier drapeau de dessiner
    ## Il me faut donc connaître cette longueur pour pouvoir mettre le drapeau FR à côté
    GB_line_lengths = [len(line) for line in GB_lines]
    GB_width = max(GB_line_lengths)
    
    # Failsafe in case I missed the line count and one flag has 1 less line
    ## This allows the flag with more lines to not see its last lines not displayed
    # Failsafe si jamais j'ai raté le décompte des lignes et qu'un drapeau en a 1 de moins
    ## Ca permet d'éviter au drapeau qui a plus de ligne de voir ses dernières lignes non affichées
    max_lines = max(len(GB_lines), len(FR_lines))
    GB_lines += [''] * (max_lines - len(GB_lines))
    FR_lines += [''] * (max_lines - len(FR_lines))
    
    # I create an empty list that I will fill in my for loop below
    ## Using lists allows to easily put the elements of the different string blocks together
    # Je créer une list vide que je vais remplir dans ma boucle for plus bas
    ## Utiliser des list permet de facilement replacer les éléments des différents blocs de string ensembles
    result = []
    
    # I use zip to transform to fill my lists and transform it back into a string
    ## So I'm sure they'll be no issue with colorizing characters
    # J'utilise zip pour transformer pour remplir mes listes et les transformer à nouveau en string
    ## Comme ça je suis sûr qu'il n'y aura pas de problème avec les caractères colorisés
    for GB_fixed, FR_fixed in zip(GB_lines, FR_lines) :
        # Append allows for the two flags to be put on the same line with the right amount of spaces in between
        # Append permet de mettre les deux drapeaux sur la même ligne avec le bon nombre d'espaces entre les deux
        result.append(f"{GB_fixed}     {FR_fixed:>{GB_width}}")
    # .join allows to transform the list into a string with the right amount of line breaks
    # .join permet de transformer la liste en string avec le bon nombre de sauts de ligne
    return '\n'.join(result)

final_result_to_call = aligned_flags()

# Script by Mathys B.
# Script de Mathys B.

# MIT License :
    # Copyright (c) 2026 Mathys B.

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