# Sollygraph

<img width="1280" height="692" alt="Exemple_1" src="https://github.com/user-attachments/assets/55541b87-6e22-45b0-9aad-b67f0d0986fe" />
<img width="1280" height="692" alt="Exemple_2" src="https://github.com/user-attachments/assets/3ceebeea-977d-4063-9eb8-bdb7baf13ccc" />
<img width="1280" height="692" alt="Exemple_3" src="https://github.com/user-attachments/assets/2093dc77-0335-40e7-a453-0cb18e493cb0" />

### Contents/Sommaire :
[EN](#en):
- [Overall presentation](#overall-presentation),
- [Special thanks](#special-thanks),
- [Requirements](#requirements),
- [Instructions - How to use the program](#instructions---how-to-use-the-program),
- [Color options reference sheet](#color-options-reference-sheet),
- [Hatch options reference sheet](#hatch-options-reference-sheet),
- [Planned Features](#planned-features).

[FR](#fr) :
- [Présentation globale](#présentation-globale),
- [Remerciements](#remerciements),
- [Pré-requis](#pré-requis),
- [Instructions - Comment utiliser le programme](#instructions---comment-utiliser-le-programme),
- [Feuille de références des options de couleurs](#feuille-de-références-des-options-de-couleurs),
- [Feuille de références des options de hachures](#feuille-de-références-des-options-de-hachures),
- [Fonctionnalités prévues](#fonctionnalités-prévues).

## EN
### Overall presentation
Sollygraph is a python program that allows you to draw a soil horizon graph by inputting your data, you can zoom in your graph and export it in .png, .pdf, .jpeg, .jpg, .pgf, .eps, .ps, .raw, .rgba, .svg, .svgz, .tif, .tiff or .webp format.

*Please note that this program, even though already usable, is still a W.I.P.*

### Special thanks
Before we continue, I want to thank [Bogdan Sandu](https://github.com/cornusandu) for creating a script to draw a hexagonal custom hatch. <br />
Thanks to his script, I was able to understand how to create the hatches I wanted (in "custom_hatches.py") and to implement them in the overall program. <br />
Even though the script is quite different now, I would have taken ages to figure this out, and I needed this time for university. <br />
So, thank you very much, Bogdan.

### Requirements
> [!IMPORTANT]
> - Python 3,
> - A device that can run Python 3.

### Instructions - How to use the program
> [!WARNING]
> <ins> ! PLEASE DO NOT SKIP THIS SECTION ! <ins />

To download the program, click on the green "code" button, then click on "download ZIP" and save the .zip file where you want. <br />
Once saved, please unzip it using the program you want (or the option of your OS in the right-click menu if available).

Once unzipped (and Python 3 installed), **please** run first the "setup.py" script before anything else. This script will allow you to select your language and install the required packages to use the program.

Once you've finished setting up the program, you'll see a new file has appeared called "config.ini", this file contains the language settings you chose. <br />
> [!NOTE]
> If at any time you want to change the language, you can either rerun "setup.py" or open "config.ini" with a text editor and manually change the language.

> [!IMPORTANT]
> Then, to use the program, only run "main.py". If you run something else, it will not work.

### Color options reference sheet
You can find the available colors in the following link: https://matplotlib.org/stable/gallery/color/named_colors.html (xkcd colors are also available at the end of the linked webpage).

<img width="1320" height="180" alt="sphx_glr_named_colors_001_2_00x" src="https://github.com/user-attachments/assets/f4071218-b1be-484c-be6e-0cd87688c10e" />

<img width="896" height="268" alt="sphx_glr_named_colors_002_2_00x" src="https://github.com/user-attachments/assets/bb4b8969-b800-4878-82e4-7c479186844b" />

<img width="1744" height="1676" alt="sphx_glr_named_colors_003_2_00x" src="https://github.com/user-attachments/assets/311568f4-eb2f-43b4-8cfc-305bb535fb00" />

> [!IMPORTANT]
> *Please choose one of those colors when prompted in the program. Be careful to not do any typo, otherwise the program will crash and close itself.*

### Hatch options reference sheet
You can find the available hatches down here:

<img width="1920" height="1080" alt="hachures_EN" src="https://github.com/user-attachments/assets/83952261-535f-4cc6-80f5-1ea7dfb6bcc4" />

If the frontier between two layers is abrupt and straight, then it's a solid line with no breaches.
If the frontier between two layers is gradual and straight, then it's a dotted line with no breaches.
If the frontier between two layers is abrupt but not straight, then it's a solid line with a breach.
If the frontier between two layers is gradual but not straight, then it's a dashed line with a breach.

> [!IMPORTANT]
> *Please choose one of those hatches when prompted in the program. Be careful to not do any typo, otherwise the program will crash and close itself.*

### Planned Features
- Make the breach actually a wave and not a succession of "V"s,
- Add options to add rocks in the middle of a horizon with different sizes and their respective hatches,
- Make a GUI.


## FR
### Présentation globale
Sollygraph est un programme python qui permet de dessiner des profils de sol via des données entrées directement par l'utilisateur. <br />
Vous pouvez zoomer dans le graphique et l'exporter au format .png, .pdf, .jpeg, .jpg, .pgf, .eps, .ps, .raw, .rgba, .svg, .svgz, .tif, .tiff ou .webp.

*Veuillez noter que ce programme, bien que déjà utilisable, est toujours en cours de développement.*

### Remerciements
Avant de continuer, j'aimerais remercier [Bogdan Sandu](https://github.com/cornusandu) d'avoir créé un script pour dessiner des hachures personnalisées avec un motif hexagonal. <br />
Grâce à son script, j'ai pu comprendre comment créer les hachures de mon choix (dans "custom_hatches.py") et implémenter cela dans mon programme. <br />
Bien que le script soit assez différent maintenant, cela m'aurait pris un temps monstre pour trouver comment faire, temps dont j'avais besoin pour étudier. <br />
Donc, un grand merci à toi, Bogdan.

### Pré-requis
> [!IMPORTANT]
> - Python 3,
> - Un appareil qui puisse faire tourner Python 3.

### Instructions - Comment utiliser le programme
> [!WARNING]
> <ins> ! VEUILLEZ PRENDRE LE TEMPS DE LIRE CETTE SECTION S'IL-VOUS-PLAÎT ! <ins />

Pour télécharger le programme, veuillez cliquer sur le bouton vert "code", puis cliquez sur le bouton "download ZIP" puis sauvegardez le fichier .zip là où vous le souhaitez. <br />
Une fois sauvegardé, veuillez dézipper le fichier à l'aide du programme de votre choix (ou l'option intégrée dans le menu du clic droit de votre OS si disponible).

Une fois dézippé (et Python 3 installé), **s'il-vous-plaît** lancez d'abord le script "setup.py" avant de faire quoique ce soit. Ce script permet de définir la langue que vous souhaitez utiliser ainsi que d'installer les paquets nécessaires au bon fonctionnement de ce programme.

Une fois que vous avez fini de configurer le programme, vous verrez un nouveau fichier nommé "config.ini" apparaître, ce fichier contient les paramètres de langue que vous avez choisis. <br />
> [!NOTE]
> Si à tout moment, vous souhaitez modifier la langue, vous pouvez soit lancer de nouveau le fichier "setup.py" soit ouvrir le fichier "config.ini" avec un éditeur de texte et manuellement changer la langue.

> [!IMPORTANT]
> Par la suite, pour utiliser le programme, veuillez uniquement lancer "main.py". Si vous lancez un autre script, le programme ne marchera pas.

### Feuille de références des options de couleurs
Vous pouvez trouver les couleurs disponibles dans le lien suivant : https://matplotlib.org/stable/gallery/color/named_colors.html (les couleurs xkcd sont également disponibles à la fin de la page internet envoyée précédemment).

<img width="1320" height="180" alt="sphx_glr_named_colors_001_2_00x" src="https://github.com/user-attachments/assets/f4071218-b1be-484c-be6e-0cd87688c10e" />

<img width="896" height="268" alt="sphx_glr_named_colors_002_2_00x" src="https://github.com/user-attachments/assets/bb4b8969-b800-4878-82e4-7c479186844b" />

<img width="1744" height="1676" alt="sphx_glr_named_colors_003_2_00x" src="https://github.com/user-attachments/assets/311568f4-eb2f-43b4-8cfc-305bb535fb00" />

> [!IMPORTANT]
> *Veuillez choisir l'une de ces couleurs lorsque le programme vous le demande. Faites attention à ne pas faire de fautes, sinon le programme crashera et se fermera.*

### Feuille de références des options de hachures
Vous pouvez trouver les hachures disponibles ci-dessous :

<img width="1920" height="1080" alt="hachures_FR" src="https://github.com/user-attachments/assets/abbfaa08-9630-4dd8-82d3-2653a3c50305" />

Si la frontière entre deux couches est brutale et droite, alors on utilise une ligne continue sans ruptures.
Si la frontière entre deux couches est graduelle et droite, alors on utilise une ligne en pointillés sans ruptures.
Si la frontière entre deux couches est brutale mais pas droite, alors on utilise une ligne continue avec une rupture.
Si la frontière entre deux couches est graduelle mais pas droite, alors on utilise une ligne en tirets avec une rupture.

> [!IMPORTANT]
> *Veuillez choisir l'une de ces hachures lorsque le programme vous le demande. Faites attention à ne pas faire de fautes, sinon le programme crashera et se fermera.*

### Fonctionnalités prévues
- Faire en sorte que la rupture soit réellement une vague et non une succession de "V",
- Ajouter des options pour ajouter des rochers en plein milieu des horizons avec différentes tailles et leurs propres hachures,
- Faire une interface graphique (GUI).
