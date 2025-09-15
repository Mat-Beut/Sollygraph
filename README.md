# Sollygraph
## EN
### Overall presentation
Sollygraph is a python program that allows you to draw a soil horizon graph by inputting your data, you can zoom in your graph and export it in .png, .pdf, .jpeg, .jpg, .pgf, .eps, .ps, .raw, .rgba, .svg, .svgz, .tif, .tiff or .webp format.
Please note that this program, even though already usable, is still a W.I.P.

### Special thanks
Before we continue, I want to thank Bogdan Sandu (https://github.com/cornusandu) for creating a script to draw an hexagonal custom hatch.
Thanks to his script, I was able to understand how to create the hatches I wanted (in "custom_hatches.py") and to implement them in the overall program.
Even though the script is quite different now, I would have take ages to figure this out, and I needed this time for university.
So, thank you very much Bogdan.

### Requirements
- Python 3,
- A device that can run Python 3.

### Instructions - How to use the program
! PLEASE DO NOT SKIP THIS !
To download the program, click on the green "code" button, then click on "download ZIP" and save the .zip file where you want.
Once saved, please unzip it using the program you want (or the option of your OS in the right-click menu if available).
Once unzipped (and Python 3 installed), **please** run first the "setup.py" script before anything else. This script will allows you to select your language and install the required packages to use the program.

Once you've finish set up the program, you'll see a new file has appeared called "config.ini", this file contains the language settings you chose.
If at any time you want to change the language, you can either rerun "setup.py" or open "config.ini" with a text editor and manually change the language.

Then, to use the program, only run "main.py". If you run something else, it will not work.

### Color option reference sheet
You can find the available colors in the following link: https://matplotlib.org/stable/gallery/color/named_colors.html (xkcd colors are also available at the end of the linked webpage).

<img width="1320" height="180" alt="sphx_glr_named_colors_001_2_00x" src="https://github.com/user-attachments/assets/f4071218-b1be-484c-be6e-0cd87688c10e" />

<img width="896" height="268" alt="sphx_glr_named_colors_002_2_00x" src="https://github.com/user-attachments/assets/bb4b8969-b800-4878-82e4-7c479186844b" />

<img width="1744" height="1676" alt="sphx_glr_named_colors_003_2_00x" src="https://github.com/user-attachments/assets/311568f4-eb2f-43b4-8cfc-305bb535fb00" />

*Please choose one of those colors when prompted in the program. Be careful to not do any typo, otherwise the program will crash and close itself.*

### Hatches option reference sheet
You can find the available hatches down here:

<img width="1920" height="1080" alt="hachures_EN" src="https://github.com/user-attachments/assets/83952261-535f-4cc6-80f5-1ea7dfb6bcc4" />

*Please choose one of those hatches when prompted in the program. Be careful to not do any typo, otherwise the program will crash and close itself.*

### Planned Features
- Make the breach actually a wave and not a succession of "V"s,
- Add options to add rocks in the middle of a horizon with different sizes and their respectives hatches,
- Make a GUI.

## FR
### Présentation globale
Sollygraph est un programme python qui permet de dessiner des profils de sol via des données entrez directement par l'utilisateur.
Vous pouvez zoomer dans le graphique et l'exporter au format .png, .pdf, .jpeg, .jpg, .pgf, .eps, .ps, .raw, .rgba, .svg, .svgz, .tif, .tiff ou .webp
Veuillez noter que ce program, bien que déjà utilisable, est toujours en cours de développement.

### Remerciements
Avant de continuer, j'aimerai remercier Bogdan Sandu (https://github.com/cornusandu) pour avoir créer un script pour dessiner des hachures personnalisées avec un motif hexagonal. Grâce à son script, j'ai pu comprendre comment créer les hachures de mon choix (dans "custom_hatches.py") et d'implémenter cela dans mon programme.
Bien que le script soit assez différent maintenant, cela m'aurait pris un temps monstre pour trouver comment faire, temps dont j'avais besoin pour étudier.
Donc, un grand merci à toi, Bogdan.

### Pré-requis
- Python 3,
- Un appareil qui puisse faire tourner Python 3.

### Instructions - Comment utiliser le programme
! VEUILLEZ PRENDRE LE TEMPS DE LIRE CETTE SECTION S'IL-VOUS-PLAÎT !
Pour télécharger le programme, veuillez cliquer sur le bouton vert "code", puis cliquez sur le bouton "download ZIP" puis sauvegardez le fichier .zip là où vous le souhaitez.
Une fois sauvegardé, veuillez dézipper le fichier à l'aide du programme de votre choix (ou l'option intégré dans le menu du clic-droit de votre OS si disponible).
Une fois dézippé (et Python 3 installé), **s'il-vous-plaît** lancez d'abord le script "setup.py" avant de faire quoique ce soit. Ce script permet de définir la langue que vous souhaitez utiliser ainsi que d'installer les paquets nécessaire au bon fonctionnement de ce programme.

Une fois que vous avez fini de configuré le programme, vous verrez un nouveau fichier nommé "config.ini" apparaître, ce fichier contient les paramètres de langue que vous avez choisis.
Si à tout moment, vous souhaitez modifier la langue, vous pouvez soit lancer de nouveau le fichier "setup.py" soit ouvrir le fichier "config.ini" avec un éditeur de texte et manuellementy changer la langue.

Par la suite, pour utiliser le programme, veuillez uniquement lancer "main.py". Si vous lancer un autre script, le programme ne marchera pas.

### Feuille de références des options de couleurs
Vous pouvez trouver les couleurs disponibles dans le lien suivant : https://matplotlib.org/stable/gallery/color/named_colors.html (les couleurs xkcd sont également disponible à la fin de la page internet envoyé précédemment).

<img width="1320" height="180" alt="sphx_glr_named_colors_001_2_00x" src="https://github.com/user-attachments/assets/f4071218-b1be-484c-be6e-0cd87688c10e" />

<img width="896" height="268" alt="sphx_glr_named_colors_002_2_00x" src="https://github.com/user-attachments/assets/bb4b8969-b800-4878-82e4-7c479186844b" />

<img width="1744" height="1676" alt="sphx_glr_named_colors_003_2_00x" src="https://github.com/user-attachments/assets/311568f4-eb2f-43b4-8cfc-305bb535fb00" />

*Veuillez choisir l'une de ces couleurs lorsque le programme vous le demande. Faites attention à ne pas faire de fautes, sinon le prgramme crashera et se fermera.*

### Feuille de référence des options de hachures
Vous pouvez trouver les hachures disponibles ci-dessous :

<img width="1920" height="1080" alt="hachures_FR" src="https://github.com/user-attachments/assets/abbfaa08-9630-4dd8-82d3-2653a3c50305" />

*Veuillez choisir l'une de ces hachures lorsque le programme vous le demande. Faites attention à ne pas faire de fautes, sinon le programme crashera et se fermera.*

### Fonctionnalitées prévues
- Faire en sorte que la rupture soit réellement une vague et non une succession de "V",
- Ajouter des options pour ajouter des rochers en plein milieu des horizons avec differentes tailles et leurs propres hachures,
- Faire une interface graphique (GUI).
