# Import des librairies nécessaires
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import hachures.custom_hatches as custom_hatches


# Mathplotlib prend ses valeurs en pouces, mais je les veux en cm
## 1 pouce = 2,54 cm
inch_to_cm = 1 * 2.54

# Crée une figure et un axe avec des dimensions fixes en centimètres via conversion des unités
## Les dimensions fixes sont là pour éviter que les barres ne se déforment quand on ajoute des couches
### Elles sont aussi là pour que les proportions restent les mêmes à l'export, peu importe la résolution et le ppi de l'écran
fig, ax = plt.subplots(figsize=(4 * inch_to_cm, 8 *inch_to_cm))

# Définis la variable pour un usage ultérieur
bar = 0

# Largeur des couches. C'est purement esthétique !
bar_width = 4

# Pour la légende
labels = []
munsells = []
horizons = []


# Fonction pour demander à l'utilisateur s'il veut ajouter un motif à sa couche
def hatch() :
    # Définis des variables globales pour un usage ultérieur dans la fonction principale du script : loopy_bar()
    global motif, ask_hatch, motif_available, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    
    # .strip().lower() pour éviter les problèmes de casse et d'espaces accidentels
    ## .strip() gère les espaces au début/à la fin, et .lower() met tout en minuscules
    ### Pour plus d'informations sur \033 etc., c'est du code ANSI escape, pour plus d'infos, vous pouvez consulter ce site : https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
    ask_hatch = input("""
        Voulez-vous ajouter un motif à votre couche ? \033[1;34;49m(oui/non)\033[0;0m : """).strip().lower()
    
    # Simplifie la saisie en acceptant "o" pour "oui"
    if ask_hatch in ["oui", "o"] :
        ask_hatch = "oui"
    
    if ask_hatch == "oui" :
        motif_available = ("""
            \033[4mMotifs disponibles :\033[0m
              \033[1;33;49m
              1. Accumulation de fer hydraté        |  2. Altéré
              3. Grès                               |  4. Calcaire
              5. Organique peu décomposé            |  6. Silice
              7. Précipitation localisée de fer     |  8. Gley
              9. Horizon particulaire               |  10. Horizon grumeleux
              11. Racines                           |  12. Carbonate de chaux
              13. Argile 2/1 (illites, vermiculites |  14. Argile 2/1 (kaolinite)
                  montmorillonite                   |
                  avec oxyde de fer absorbé)        |  
              15. Alumine libre                     |  16. Concrétion ferro-magnétique
              17. Accumulation de fer déshydraté    | \033[0;0m
             """)
        # Définit une couleur pour "|", puis remplace les "|" dans le texte de "motif_available" par le même "|" mais coloré 
        default_color = "\033[0;1m|\033[1;33;49m"
        if '|' in motif_available :
            motif_available = motif_available.replace('|', default_color)
        print(motif_available)
        motif_choice = input("Entrez le numéro du motif que vous souhaitez utiliser : ").strip()

        # Vérifie si la valeur saisie est 1, 2, 5, 6, 8, 10, 13, 14 ou 17
        ## Si la valeur est l'une d'entre elles, vérifie de laquelle il s'agit et assigne à "motif" le motif correspondant
        if motif_choice in ['1', '2', '5', '6', '8', '10', '13', '14', '17'] :
            if motif_choice == '1' :
                motif = custom_hatches.vline
            if motif_choice == '2' :
                motif = custom_hatches.reversed_t
            if motif_choice == '5' :
                motif = custom_hatches.orga_peu_decomp
            if motif_choice == '6' :
                motif = custom_hatches.plus
            if motif_choice == '8' :
                motif = custom_hatches.dashed_vline
            if motif_choice == '10' :
                motif = custom_hatches.slash
            if motif_choice == '13' :
                motif = custom_hatches.hline_full
            if motif_choice == '14' :
                motif = custom_hatches.hline
            if motif_choice == '17' :
                 motif = custom_hatches.vline
            # Convertis le motif en lignes pour l'utiliser avec la fonction draw_hatch du fichier custom_hatches.py
            ## S'appelle ainsi, car cette variable peut être ajoutée dans les dictionnaires bar_dict ou poly_dict
            motif_for_dict = custom_hatches.shape_to_lines(*motif)

        # Si la valeur saisie est 3, assigne à "motif" le motif de points
        ## Puisque nous ne voulons pas de segments entre les points, pas besoin d'utiliser la fonction shape_to_line()
        if motif_choice in ['3'] :
            motif = custom_hatches.dots
            motif_for_dict = motif
        
        # Si la valeur saisie est 4, assigne à "motif_for_dict" les différentes variables utilisées pour réaliser le motif en forme de grille
        if motif_choice in ['4'] :
           custom_hatches.grid1
           custom_hatches.grid2
           # Le signe "+" n’est ici non pas utilisé pour additionner la moindre valeur, mais pour tracer les 2 variables utilisées pour le motif en forme de grilles (avec les motifs de la ligne verticale et de la ligne horizontale)
           motif_for_dict = custom_hatches.grid1 + custom_hatches.grid2

        # Si la valeur saisie est 7, assigne à "motif_for_dict" les différentes variables utilisées pour réaliser le motif en forme d'onde
        if motif_choice in ['7'] :
           custom_hatches.line1
           custom_hatches.line2
           custom_hatches.line3
           custom_hatches.line4
           # Le signe "+" n’est ici non pas utilisé pour additionner la moindre valeur, mais pour tracer les 4 variables utilisées pour le motif en forme d'onde
           motif_for_dict = custom_hatches.line1 + custom_hatches.line2 + custom_hatches.line3 + custom_hatches.line4
        
        # Si la valeur saisie est 9, assigne à "motif_for_dict" les différentes variables utilisées pour réaliser le motif des lignes en diagonale
        if motif_choice in ['9'] :
            custom_hatches.slash1
            custom_hatches.slash2
            # Idem qu'avant, 2 variables sont dessinées
            motif_for_dict = custom_hatches.slash1 + custom_hatches.slash2

        # Si la valeur saisie est 11, assigne à "motif_for_dict" le motif des racines
        if motif_choice in ['11'] :
            motif = custom_hatches.racines
            # Idem que shape_to_line() sauf que le premier et dernier point ne sont pas reliés (voir custom_hatches.py)
            motif_for_dict = custom_hatches.open_shape(*motif)

        # Si la valeur saisie est 12, assigne à "motif_for_dict" le motif des deux hlines
        if motif_choice in ['12'] :
            custom_hatches.hlineA
            custom_hatches.hlineB
            # Le signe "+" n’est ici non pas utilisé pour additionner la moindre valeur, mais pour tracer les 2 variables utilisées pour le motif 12
            motif_for_dict = custom_hatches.hlineA + custom_hatches.hlineB

        # Si la valeur saisie est 15, assigne à "motif" le motif de cercles
        ## Comme pour les points, on ne veut pas de segments, on garde juste les centres
        if motif_choice in ['15'] :
            motif = custom_hatches.circles
            motif_for_dict = motif

        # Si la valeur saisie est 16, assigne à "motif" le motif de cercles mais patché pour acceuillir des lignes vertical en plus
        ## Pour fusionner les deux types de motifs, il faut les définir séparément dans un dictionnaire et définir un type par figure (pour que le script sache comment les dessiner plus tard)
        if motif_choice in ['16'] :
            motif_for_dict = [
                {"data": custom_hatches.line1_16 + custom_hatches.line2_16 + custom_hatches.line3_16 + custom_hatches.line4_16, "type": "multilines"},
                {"data": custom_hatches.circles, "type": "circles"}
            ]

        # Petit code de secours au cas où quelqu'un entrerait un numéro non proposé
        if motif_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] :
            print("""\033[31;49;3mChoix invalide, aucun motif ne sera appliqué.
                  \033[0;0m""")
            ask_hatch = "non"
    else :
        ask_hatch = "non"

def loopy_bar() :
    global bar_width, bar, x_wave, y_wave, labels, munsells, motif, motif_available, ask_hatch, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    loopy = int(input("""
        Entrez le nombre de couches que vous souhaitez créer : """))
    bottom = 0

    # Permets de répéter la création de barres en fonction du nombre de couches voulues
    for i in range(loopy) :
        x = [0]
        # Le "f" permet d'utiliser {i + 1} au milieu du texte affiché dans l'input
        ## {i + 1} montre dans quelle boucle on est. Si c'est la première boucle, "couche 1" sera affiché, si c'est la 3e boucle, "couche 3" sera affiché.
        y = int(input(f"""
        Entrez la hauteur de votre couche {i + 1} en cm : """))
        
        bar_wave = input("""
        Votre couche comporte-t-elle une rupture ? \033[1;34;49m(oui/non)\033[0;0m : """).strip().lower()
        if bar_wave in ["oui", "o"] :
            bar_wave = "oui"

        # Label correspond au nom de la couche
        ## munsell_color est une sorte de deuxième label avec un nom différent pour éviter tout bug
        label = input("""
        Entrez le nom de votre couche : """)
        munsell_color = input("""
        Entrez le code couleur Munsell de votre choix : """)


        if bar_wave == "oui" :
            dash_wave = input("""
        Tirets ou ligne continue ? \033[1;34;49m(tirets/ligne)\033[0;0m : """).strip().lower()
            # Simplifie la saisie en acceptant "t" pour "tirets"
            if dash_wave in ["tirets", "t"] :
                dash_wave = "tirets"
            # Valeurs x et y pour la rupture
            bar_bottom = bottom
            x_wave = [0, 1, 2, 3, 4]
            y_wave = [y - 1, y, y - 1, y, y - 1]


            # Le polygone devrait suivre la forme donnée par x_wave et y_wave
            bar_left = x_wave[0]
            bar_right = x_wave[-1]

            # Points des polygones
            poly_x = [bar_left] + x_wave + [bar_right, bar_left]
            # Pour que la rupture ne commence pas à 0 à chaque fois
            poly_y = [bar_bottom] + [bar_bottom + yw for yw in y_wave] + [bar_bottom, bar_bottom]

            # Stocke les données de polygones
            ## Obligatoire pour pas avoir la barre du dessous qui cache le polygone
            poly_dict = {
                "type" : "poly",
                # "xy" correspond à une liste de tuples de coordonnées x et y, zip permet de les associer ensemble
                ## List est utilisé pour que les coordonnées soient regroupées en une liste et soit facilement utilisables pour tracer le polygone plus tard
                "xy" : list(zip(poly_x, poly_y)),
                "label" : label,
                "munsell" : munsell_color,
                "linestyle" : 'dashed' if dash_wave == "tirets" else 'solid'
            }
            # Lance la fonction hatch() afin de demander si des hachures sont nécessaires, et lesquels utiliser
            hatch()

            if ask_hatch == "oui" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] :
                    # Ajoute l'option "motif" dans le dictionnaire du polygone et le fait correspondre à "motif_for_dict"
                    ## Allez voir hatch() pour savoir à quoi "motif_for_dict" correspond, ça change en fonction du motif choisi
                    poly_dict["motif"] = motif_for_dict
                    if motif_choice in ['3'] :
                        # Ajoute et configure l'option "motif_type". Cela servira plus tard quand il sera nécessaire de préciser exactement comment les hachures doivent être dessinées
                        poly_dict["motif_type"] = "dots"
                    elif motif_choice in ['4'] :
                        poly_dict["motif_type"] = "grid"
                    elif motif_choice in ['7'] :
                        poly_dict["motif_type"] = "multilines"
                    elif motif_choice in ['9', '10'] :
                        poly_dict["motif_type"] = "slash"
                    elif motif_choice in ['11'] :
                        poly_dict["motif_type"] = "racines"
                    elif motif_choice in ['12'] :
                        poly_dict["motif_type"] = "double_hline"
                    elif motif_choice in ['15'] :
                        poly_dict["motif_type"] = "circles"
                    elif motif_choice in ['16'] :
                        # Puisque le motif 16 correspond à deux types de motifs différents prédéfinis précédemment
                        ## On assigne une valeur none ici afin que motif_type soit enregistré dans le dictionnaire poly_dict
                        ### Tout en récupérant les deux types de motifs dans "motif_for_dict" 
                        poly_dict["motif_type"] = None
                    else :
                        # Ajoute et configure l'option "motif_type", sauf que c'est pour la majorité des motifs et non pour des exceptions comme juste au-dessus
                        poly_dict["motif"] = motif_for_dict
                        poly_dict["motif_type"] = "lines"
            else :
                # Configure ces options en tant que "None" afin qu'elles soient ignorées sans faire buguer le script
                poly_dict["motif"] = None
                poly_dict["motif_type"] = None
            
            # Stocke le dictionnaire sous le nom "horizons" pour plus tard
            horizons.append(poly_dict)

            # Mise à jour de "bottom" pour permettre le l'empilement des couches
            ## À partir du point le plus haut de la dernière rupture
            ### (le point le plus haut, car l'axe y du graphique est inversé)
            bottom += min(y_wave)


        else :
            dash = input("""
        Pointillés ou ligne continue ? \033[1;34;49m(pointillés/ligne)\033[0;0m : """).strip().lower()
            # Simplifie la saisie en acceptant "p" pour "pointillets"
            if dash in ["pointillés", "p"] :
                dash = "pointillés"


            # Stocke les données de la barre
            bar_dict = {
                "type" : "bar",
                "x" : x,
                "y" : y,
                "bottom" : bottom,
                "label" : label,
                "munsell" : munsell_color,
                "linestyle" : 'dotted' if dash == "pointillés" else 'solid'
            }

            # Lance la fonction hatch() afin de demander si des hachures sont nécessaires et lesquels utiliser
            hatch()

            if ask_hatch == "oui" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] :
                    # Ajoute l'option "motif" dans le dictionnaire de la barre et le fait correspondre à "motif_for_dict"
                    ## Allez voir hatch() pour savoir à quoi "motif_for_dict" correspond, ça change en fonction du motif choisi
                    bar_dict["motif"] = motif_for_dict
                    if motif_choice in ['3'] :
                        # Ajoute et configure l'option "motif_type". Cela servira plus tard quand il sera nécessaire de préciser exactement comment les hachures doivent être dessinées
                        bar_dict["motif_type"] = "dots"
                    elif motif_choice in ['4'] :
                        bar_dict["motif_type"] = "grid"
                    elif motif_choice in ['7'] :
                        bar_dict["motif_type"] = "multilines"
                    elif motif_choice in ['9', '10'] :
                        bar_dict["motif_type"] = "slash"
                    elif motif_choice in ['11'] :
                        bar_dict["motif_type"] = "racines"
                    elif motif_choice in ['12'] :
                        bar_dict["motif_type"] = "double_hline"
                    elif motif_choice in ['15'] :
                        bar_dict["motif_type"] = "circles"
                    elif motif_choice in ['16'] :
                        # Puisque le motif 16 correspond à deux types de motifs différents prédéfinis précédemment
                        ## On assigne une valeur none ici afin que motif_type soit enregistré dans le dictionnaire bar_dict
                        ### Tout en récupérant les deux types de motifs dans "motif_for_dict"
                        bar_dict["motif_type"] = None
                    else :
                        # Ajoute et configure l'option "motif_type", sauf que c'est pour la majorité des motifs et non pour des exceptions comme juste au-dessus
                        bar_dict["motif"] = motif_for_dict
                        bar_dict["motif_type"] = "lines"
            else :
                # Configure ces options en tant que "None" afin qu'elles soient ignorées sans faire buguer le script
                bar_dict["motif"] = None
                bar_dict["motif_type"] = None

            # Stocke le dictionnaire sous le nom "horizons" pour plus tard
            horizons.append(bar_dict)
            
            # Mise à jour de "bottom" pour permettre le l'empilement des couches
            ## Ajoute la valeur de y afin d'être sûr que la prochaine couche ne soit pas dessinée devant la précédente
            bottom += y


    # "reversed" permet aux couches d'être dessinées de la dernière à la première. C'est également pour cela qu'il était nécessaire de d'abord stocker les données
    ## Cela permet d'éviter divers soucis de couches les unes devant les autres
    for h in reversed(horizons) :
        if h["type"] == "bar" :
            bar = ax.bar(
                h["x"], 
                h["y"],
                bar_width,
                # Puisqu'h correspond à "horizons" (mais reversed), la ligne suivante signifie que "bottom" = le paramètre bottom de, dans ce cas-ci, bar_dict
                bottom = h["bottom"],
                # Idem ici pour "label", puis "color", etc.
                ## "label" correspond à la légende
                label = h["label"],
                # "facecolor" est la couleur de la barre
                facecolor = 'white',
                # "edgecolor" est la couleur du coutour de la barre
                edgecolor = 'black',
                # "linestyle" est le type de contour ("pointillés", "ligne")
                linestyle = h["linestyle"],
                # Aligne les bords gauches de la barre avec les positions de x
                align = 'edge',
                # "zorder" détermine l'ordre dans lequel les barres, polygones, etc., doivent être tracés
                ## Plus le nombre est grand, plus l'objet sera dessiné tard
                zorder = 1
            )
            # Récupère la valeur de "motif", si ce n'est pas None, rempli la barre avec la bonne hachure et la dessine
            if h.get("motif") is not None :
                # Vérifie si c'est une liste de dicts (multi-motif) ou juste des données (single-motif)
                ## Plus précisément, isinstance vérifie si h["motif"] est un dictionnaire ou pas
                ### Si oui, alors on enchaîne sur la boucle for m in h["motif"]
                if h["motif"] and isinstance(h["motif"][0], dict) :
                    # Plusieurs motifs : chaque élément est un dictionnaire avec "data" et "type"
                    for m in h["motif"] :
                        # En fonction du type de motif, utilise la fonction de dessin appropriée
                        if m["type"] == "multilines" :
                            custom_hatches.draw_hatch(ax, m["data"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                        elif m["type"] == "circles" :
                            custom_hatches.draw_circles_patches(ax, m["data"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black', radius = 0.08)
                else :
                    # Un seul motif : h["motif"] contient directement les données du motif
                    if h["motif_type"] == "lines" :
                        ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                        # Si le motif choisi est le numéro 17, alors on ajoute linedwidth = 2 pour que les lignes soient plus épaisses
                        if motif_choice in ['17'] :
                            # (ce sur quoi doit être mis le motif, type de motif (côté gauche de la barre, côté droit de la barre), (partie haute de la barre, partie basse de la barre))
                            ## "spacing" est l'espace entre chaque liste de points. Cela joue aussi bien sur l'espace vertical qu'horizontal (sauf pour l'espace vertical pour "racines", puisque dans custom_hatches/draw_racines, l'argument "spacing" a été enlevé pour dy)
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black', linewidth = 2)
                        else :
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')

                    if h["motif_type"] == "grid" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.2, color = 'black')
                    if h["motif_type"] == "multilines" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 1.2, color = 'black')
                    if h["motif_type"] == "slash" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 1.0, color = 'black')
                    if h["motif_type"] == "racines" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = "black")
                            custom_hatches.draw_racines(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                    if h["motif_type"] == "dots" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_dots(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                    if h["motif_type"] == "double_hline" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                    if h["motif_type"] == "circles" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_circles_patches(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black', radius = 0.08)
                            
                            ax.set_aspect('equal')


            # Stocke le nom pour l'annotation et le code Munsell pour la légende
            labels.append(h["label"])
            # h.get et pas h["munsell"] pour éviter les problèmes si jamais "munsell" n'est pas défini dans le dictionnaire (ça évite un KeyError)
            munsells.append(h.get("munsell"))
        
        
            # Calcul le milieu de la barre (ajusté pour la largeur des barres)
            bar_x = h["x"][0] + (bar_width - 0.5)
            bar_y = h["bottom"] + h["y"] / 2

            # Annote la barre avec une ligne et le nom de la barre (qui correspond au label)
            ax.annotate(
                h["label"],
                xy = (bar_x, bar_y),
                # Positionne le nom de la barre à droite de la ligne 
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                xytext = (bar_x + 1, bar_y),
                va = 'center',
                ha = 'left',
                # Pour dessiner une ligne, il faut en fait dessiner une flèche
                ## Le type de la flèche est une ligne droite
                arrowprops = dict(arrowstyle = '-', color = 'black')
            )

            # Annote la barre avec une ligne et le code Munsell en dessous du label
            ax.annotate(
                h["munsell"] + "*",
                xy = (bar_x, bar_y + 0.5),
                # Positionne le code Munsell à droite de la ligne 
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                xytext = (bar_x + 1, bar_y + 0.5),
                va = 'center',
                ha = 'left',
                # Pour dessiner une ligne, il faut en fait dessiner une flèche
                ## Le type de la flèche est une ligne droite
                arrowprops = dict(arrowstyle = '-', color = 'black')
            )

    # "reversed" permet aux couches d'être dessinées de la dernière à la première. C'est également pour cela qu'il était nécessaire de d'abord stocker les données
    ## Cela permet d'éviter divers soucis de couches les unes devant les autres
    for h in reversed(horizons) :
        if h["type"] == "poly" :
            poly = patches.Polygon(
                # Puisqu'h correspond à "horizons" (mais reversed), la ligne suivante signifie que "xy" = le paramètre xy de, dans ce cas-ci, poly_dict
                xy = h["xy"],
                # Quand "closed" est True, alors le premier et dernier points sont reliés
                ## C'est ainsi qu'on obtient un polygone qui ressemble à une barre, mais avec une rupture en vague en v en bas
                closed = True,
                # Idem que "xy" mais pour "label", puis "color", etc.
                ## "label" correspond à la légende
                label = h["label"],
                # "facecolor" est la couleur du polygone
                facecolor = 'white',
                # "edgecolor" est la couleur du coutour du polygone
                edgecolor = 'black',
                # "linestyle" est le type de contour ("tirets", "ligne")
                linestyle = h['linestyle'],
                # Honnêtement, je ne me souviens plus de ce que ça fait, je suis désolé...
                clip_on = True,
                # "zorder" détermine l'ordre dans lequel les barres, polygones, etc., doivent être tracés
                ## Plus le nombre est grand, plus l'objet sera dessiné tard
                zorder = 3
            )
            # Dessine le polygone
            ax.add_patch(poly)

            # Stocke le nom pour l'annotation et le code Munsell pour la légende
            labels.append(h["label"])
            # h.get et pas h ["munsell"] pour éviter les problèmes si jamais "munsell" n'est pas défini dans le dictionnaire (ça évite un KeyError)
            munsells.append(h.get("munsell"))
            
            
            # Détermine la valeur de x la plus à droite et la moyenne de y pour le placement du label plus tard
            poly_xs, poly_ys = zip(*h["xy"])

            # Calcule les limites x et y une seule fois pour tous les motifs
            xmin, xmax = min(poly_xs), max(poly_xs)
            ymin, ymax = min(poly_ys), max(poly_ys)

            # Récupère la valeur de "motif", si ce n'est pas None, rempli le polygone avec la bonne hachure et la dessine
            if h.get("motif") is not None :
                # Vérifie si c'est une liste de dicts (multi-motif) ou juste des données (single-motif)
                ## Plus précisément, isinstance vérifie si h["motif"] est un dictionnaire ou pas
                ### Si oui, alors on enchaîne sur la boucle for m in h["motif"]
                if h["motif"] and isinstance(h["motif"][0], dict) :
                    # Plusieurs motifs : chaque élément est un dictionnaire avec "data" et "type"
                    for m in h["motif"] :
                        # En fonction du type de motif, utilise la fonction de dessin appropriée
                        if m["type"] == "multilines" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, m["data"], h["xy"], (xmin, xmax), (ymin, ymax), spacing=0.5, color='black')
                        elif m["type"] == "circles" :
                            custom_hatches.draw_circles_patches_clipped_for_poly(ax, m["data"], h["xy"], (xmin, xmax), (ymin, ymax), spacing=0.5, color='black', radius= 0.05)
                else :
                    # Un seul motif : h["motif"] contient directement les données du motif
                    if h.get("motif_type") == "lines" :
                            # Si le motif choisi est le numéro 17, alors on ajoute linedwidth = 2 pour que les lignes soient plus épaisses
                            if motif_choice in ['17'] :
                                # (ce sur quoi doit être mis le motif, type de motif, positions de xy (afin que x et y max et min puissent être utilisé juste après) (côté gauche du poly, côté droit du poly), (partie haute du poly, partie basse du poly))
                                ## "spacing" est l'espace entre chaque liste de points. Cela joue aussi bien sur l'espace vertical qu'horizontal (sauf pour l'espace vertical pour "racines", puisque dans custom_hatches/draw_racines, l'argument "spacing" a été enlevé pour dy)
                                custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, linewidth = 2, color = 'black')
                            else :
                                custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "grid" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.2, color = 'black')
                    if h.get("motif_type") == "multilines" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.2, color = 'black')
                    if h.get("motif_type") == "slash" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.0, color = 'black')
                    if h.get("motif_type") == "racines" :
                            custom_hatches.draw_racines_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "dots" :
                            custom_hatches.draw_dots_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "double_hline" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "circles" :
                            custom_hatches.draw_circles_patches_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black', radius = 0.08)

            # Détermine les positions de x et y pour le "label" et "munsell" et leur positionnement dans annotate()
            label_x = max(poly_xs) + 0.5
            label_y = sum(poly_ys) / len(poly_ys)
            munsell_x = max(poly_xs) + 0.5
            munsell_y = (sum(poly_ys) / len(poly_ys)) + 0.5
            
            
            # Annote le polygone avec une ligne et le nom du polygone (qui correspond au label)
            ax.annotate(
                h["label"],
                xy = (max(poly_xs) - 0.5, label_y),
                # Positionne le nom de la barre à droite de la ligne
                xytext = (label_x, label_y),
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                va = 'center',
                ha = 'left',
                # Pour dessiner une ligne, il faut en fait dessiner une flèche
                ## Le type de la flèche est une ligne droite
                arrowprops=dict(arrowstyle = '-', color = 'black')
                )
            
            # Annote le polygone avec une ligne et le code Munsell en dessous du label
            ax.annotate(
                h["munsell"] + "*",
                xy = (max(poly_xs) - 0.5, munsell_y),
                # Positionne le code Munsell à droite de la ligne
                xytext = (munsell_x, munsell_y),
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                va = 'center',
                ha = 'left',
                # Pour dessiner une ligne, il faut en fait dessiner une flèche
                ## Le type de la flèche est une ligne droite
                arrowprops=dict(arrowstyle = '-', color = 'black')
                )

    # Allez savoir pourquoi, mais d'un coup, mes couches n’allaient pas jusqu'en bas ni jusqu'en haut, j'avais le 0 de décalé en hauteur et le bazar dans mes ticks, j'ai dû tout modifier
    ## D'où l'ajout de (0, bottom) pour ax.set_ylim()
    ax.set_ylim(0, bottom)


# Lance la fonction principale du script 
loopy_bar()


# Script de Mathys B.
## Certaines parties sont inspirées d'un script écrit par Bogdan S.

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