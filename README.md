# Sollygraph 
<sub> Current version: Alpha 2.0 - Monmaster release </sub>

<img width="320" height="173" alt="Exemple sollygraph alpha 20" src="https://github.com/user-attachments/assets/f358fb41-6382-4779-b036-157650ea8dbc" />


### Contents/Sommaire :
[EN](#en):
- [Overall presentation](#overall-presentation),
- [Special thanks](#special-thanks),
- [Requirements](#requirements),
- [Instructions - How to use the program](#instructions---how-to-use-the-program),
- [Color options](#color-options),
- [Hatch options reference sheet](#hatch-options-reference-sheet),
- [Planned Features](#planned-features).

[FR](#fr) :
- [Présentation globale](#présentation-globale),
- [Remerciements](#remerciements),
- [Pré-requis](#pré-requis),
- [Instructions - Comment utiliser le programme](#instructions---comment-utiliser-le-programme),
- [Options de couleurs](#Options-de-couleurs),
- [Feuille de références des options de hachures](#feuille-de-références-des-options-de-hachures),
- [Fonctionnalités prévues](#fonctionnalités-prévues).

## EN
### Overall presentation
Sollygraph is a python program that allows you to draw a soil horizon graph by inputting your data, you can zoom in your graph, move it and export it in .png, .pdf, .jpeg, .jpg, .pgf, .eps, .ps, .raw, .rgba, .svg, .svgz, .tif, .tiff or .webp format.

*Please note that this program, even though already usable, is still a Work In Progress (W.I.P.)*

### Special thanks
Before we continue, I want to thank [Bogdan Sandu](https://github.com/cornusandu) for creating a script to draw a hexagonal custom hatch. <br />
Thanks to his script, I was able to understand how to create the hatches I wanted (in "custom_hatches.py") and to implement them in the overall program. <br />
Even though the script is quite different now, I would have taken ages to figure this out, and I needed this time for university. <br />
So, thank you very much, Bogdan.

I want to thank as well Mrs. Balland for the further information she provided that helped for the new version of the program. <br />
Without her, the program would still be in a useless proof of concept form. <br />
So, thank you very much.

### Requirements
> [!IMPORTANT]
> - Python 3,
> - A device that can run Python 3.

### Instructions - How to use the program
> [!WARNING]
> <ins> ! PLEASE DO NOT SKIP THIS SECTION ! <ins />

To download the program, click on the green "code" button, then click on "download ZIP" and save the .zip file where you want. <br />
You can also download the program by clicking on the "Release" section on the right side of the page and select the "sollygraph__xx_xx.zip" file of the release of your choice. Most recent release is always the higher one on the list. <br />
Once saved, please unzip it using the program you want (or the option of your OS in the right-click menu if available).

Once unzipped (and Python 3 installed), **please** run first the "setup.py" script before anything else. This script will allow you to select your language and install the required packages to use the program.

Once you've finished setting up the program, you'll see a new file has appeared called "config.ini", this file contains the language settings you chose. <br />
> [!NOTE]
> If at any time you want to change the language, you can either rerun "setup.py" or open "config.ini" with a text editor and manually change the language.

> [!IMPORTANT]
> Then, to use the program, only run "main.py". If you run something else, it will not work.

### Color options
The colors system used is the Munsell color code. It has been coded as a label in the legend, so you can technically use any code, either Munsell or not, the color won't show but its code will appear. Please use a trusted source if you want a reference sheet of Munsell code's colors.

> [!IMPORTANT]
> *Please choose one of those colors when prompted in the program. Be careful to not do any typo, otherwise the program will crash and close itself.*

### Hatch options reference sheet
You can find the available hatches down here:

<img width="1920" height="1080" alt="hachures_EN" src="https://github.com/user-attachments/assets/83952261-535f-4cc6-80f5-1ea7dfb6bcc4" />

If the frontier between two layers is abrupt and straight, then it's a solid line with no breaches. <br />
If the frontier between two layers is gradual and straight, then it's a dotted line with no breaches. <br />
If the frontier between two layers is abrupt but not straight, then it's a solid line with a breach. <br />
If the frontier between two layers is gradual but not straight, then it's a dashed line with a breach. <br />

> [!IMPORTANT]
> *Please choose one of those hatches when prompted in the program. Be careful to not do any typo, otherwise the program will crash and close itself.*

### Planned Features
- Make the breach actually a wave and not a succession of "V"s,
- Add options to add rocks in the middle of a horizon with different sizes and their respective hatches,
- Rework pattern 16 way of rendering so it is consistent between bars and polygons,
- Add an option for the use of multiple patterns overlapping on a same bar/polygon,
- Add a log system,
- Make an import and export system for spreadsheets,
- Make a GUI.


## FR
### Présentation globale
Sollygraph est un programme python qui permet de dessiner des profils de sol via des données entrées directement par l'utilisateur. <br />
Vous pouvez zoomer dans le graphique, le déplacer et l'exporter au format .png, .pdf, .jpeg, .jpg, .pgf, .eps, .ps, .raw, .rgba, .svg, .svgz, .tif, .tiff ou .webp.

*Veuillez noter que ce programme, bien que déjà utilisable, est toujours en cours de développement.*

### Remerciements
Avant de continuer, j'aimerais remercier [Bogdan Sandu](https://github.com/cornusandu) d'avoir créé un script pour dessiner des hachures personnalisées avec un motif hexagonal. <br />
Grâce à son script, j'ai pu comprendre comment créer les hachures de mon choix (dans "custom_hatches.py") et implémenter cela dans mon programme. <br />
Bien que le script soit assez différent maintenant, cela m'aurait pris un temps monstre pour trouver comment faire, temps dont j'avais besoin pour étudier. <br />
Donc, un grand merci à toi, Bogdan.

J'aimerai également remercier Mme. Balland pour les informations supplémentaires qu'elle a fourni et qui ont aidé à la réalisation de la nouvelle version du programme. <br />
Sans elle, ce programme serait probablement toujours une sorte de concept inutilisable. <br />
Un grand merci à vous.

### Pré-requis
> [!IMPORTANT]
> - Python 3,
> - Un appareil qui puisse faire tourner Python 3.

### Instructions - Comment utiliser le programme
> [!WARNING]
> <ins> ! VEUILLEZ PRENDRE LE TEMPS DE LIRE CETTE SECTION S'IL-VOUS-PLAÎT ! <ins />

Pour télécharger le programme, veuillez cliquer sur le bouton vert "code", puis cliquez sur le bouton "download ZIP" puis sauvegardez le fichier .zip là où vous le souhaitez. <br />
Vous pouvez également téléchargé le programme en cliquant sur la section "Release" sur la droite de la page GitHub et sélectionner le fichier "sollygraph_xx_xx.zip" de la version de votre choix. La version la plus récente étant toujours au sommet de la page. <br />
Une fois sauvegardé, veuillez dézipper le fichier à l'aide du programme de votre choix (ou l'option intégrée dans le menu du clic droit de votre OS si disponible).

Une fois dézippé (et Python 3 installé), **s'il-vous-plaît** lancez d'abord le script "setup.py" avant de faire quoique ce soit. Ce script permet de définir la langue que vous souhaitez utiliser ainsi que d'installer les paquets nécessaires au bon fonctionnement de ce programme.

Une fois que vous avez fini de configurer le programme, vous verrez un nouveau fichier nommé "config.ini" apparaître, ce fichier contient les paramètres de langue que vous avez choisis. <br />
> [!NOTE]
> Si à tout moment, vous souhaitez modifier la langue, vous pouvez soit lancer de nouveau le fichier "setup.py" soit ouvrir le fichier "config.ini" avec un éditeur de texte et manuellement changer la langue.

> [!IMPORTANT]
> Par la suite, pour utiliser le programme, veuillez uniquement lancer "main.py". Si vous lancez un autre script, le programme ne marchera pas.

### Options de couleurs
Le système de couleur utilisé est le code couleur Munsell. Il a été codé comme un label dans la légende, vous pouvez donc techniquement utiliser n'importe quel code couleur, Munsell ou non, la couleur n'appraîtra pas mais son code apparaîtra. Veuillez s'il-vous-plaît utiliser une source sûre si vous souhaitez utiliser une feuille de référence pour les couleurs du code Munsell.

> [!IMPORTANT]
> *Veuillez choisir l'une de ces couleurs lorsque le programme vous le demande. Faites attention à ne pas faire de fautes, sinon le programme crashera et se fermera.*

### Feuille de références des options de hachures
Vous pouvez trouver les hachures disponibles ci-dessous :

<img width="1920" height="1080" alt="hachures_FR" src="https://github.com/user-attachments/assets/abbfaa08-9630-4dd8-82d3-2653a3c50305" />

Si la frontière entre deux couches est brutale et droite, alors on utilise une ligne continue sans ruptures. <br />
Si la frontière entre deux couches est graduelle et droite, alors on utilise une ligne en pointillés sans ruptures. <br />
Si la frontière entre deux couches est brutale mais pas droite, alors on utilise une ligne continue avec une rupture. <br />
Si la frontière entre deux couches est graduelle mais pas droite, alors on utilise une ligne en tirets avec une rupture. <br />

> [!IMPORTANT]
> *Veuillez choisir l'une de ces hachures lorsque le programme vous le demande. Faites attention à ne pas faire de fautes, sinon le programme crashera et se fermera.*

### Fonctionnalités prévues
- Faire en sorte que la rupture soit réellement une vague et non une succession de "V",
- Ajouter des options pour ajouter des rochers en plein milieu des horizons avec différentes tailles et leurs propres hachures,
- Retravailler le rendu du motif 16 pour qu'il soit plus constant entre les barres et polygones,
- Ajouter une option pour permettre à plusieurs motifs de se superposer sur une même barre/un même polygone,
- Ajouter un système de log,
- Ajouter un système d'import et d'export de feuilles de tableurs,
- Faire une interface graphique (GUI).
