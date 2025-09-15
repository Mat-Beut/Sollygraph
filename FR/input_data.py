# Import de la librairie readline pour utiliser les flèches en le paramétrant pour qu'il soit importé pour Mac et Linux mais pas pour Windows sinon ça crash
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
horizons = []


# Fonction pour demander à l'utilisateur s'il veut ajouter un motif à sa couche
def hatch() :
    # Définis des variables globales pour un usage ultérieur dans la fonction principale du script : loopy_bar()
    global motif, ask_hatch, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    
    # .strip().lower() pour éviter les problèmes de casse et d'espaces accidentels
    ## .strip() gère les espaces au début/à la fin, et .lower() met tout en minuscules
    ask_hatch = input("Voulez-vous ajouter un motif à votre couche ? (oui/non) : ").strip().lower()
    
    # Simplifie la saisie en acceptant "o" pour "oui"
    if ask_hatch in ["oui", "o"] :
        ask_hatch = "oui"
    
    if ask_hatch == "oui" :
        print("Motifs disponibles :")
        print("1. Accumulation de fer")
        print("2. Altéré")
        print("3. Grès")
        print("4. Calcaire")
        print("5. Organique peu décomposé")
        print("6. Silice")
        print("7. Précipitation localisée de fer")
        print("8. Gley")
        print("9. Horizon particulaire")
        print("10. Horizon grumeleux")
        print("11. Racines")
        motif_choice = input("Entrez le numéro du motif que vous souhaitez utiliser : ").strip()

        # Vérifie si la valeur saisie est 1, 2, 4, 5, 6, 8 ou 10
        ## Si la valeur est l'une d'entre elles, vérifie de laquelle il s'agit et assigne à "motif" le motif correspondant
        if motif_choice in ['1', '2', '5', '6', '8', '10'] :
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
           # Le signe "+" n’est ici non pas utilisé pour additionner la moindre valeur, mais pour tracer les 4 variables utilisées pour le motif en forme d'onde
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

        # Petit code de secours au cas où quelqu'un entrerez un numéro non proposé
        if motif_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] :
            print("Choix invalide, aucun motif ne sera appliqué.")
            ask_hatch = "non"
    else :
        ask_hatch = "non"

def loopy_bar() :
    global bar_width, bar, x_wave, y_wave, labels, motif, ask_hatch, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    loopy = int(input("Entrez le nombre de couches que vous souhaitez créer : "))
    bottom = 0

    # Permets de répéter la création de barres en fonction du nombre de couches voulues
    for i in range(loopy) :
        x = [0]
        # Le "f" permet d'utiliser {i + 1} au milieu du texte affiché dans l'input
        ## {i + 1} montre dans quelle boucle on est. Si c'est la première boucle, "couche 1" sera affiché, si c'est la 3e boucle, "couche 3" sera affiché.
        y = int(input(f"Entrez la hauteur de votre couche {i + 1} en cm : "))
        
        bar_wave = input("Votre couche comporte-t-elle une rupture ? (oui/non) : ").strip().lower()
        if bar_wave in ["oui", "o"] :
            bar_wave = "oui"

    
        label = input("Entrez le nom de votre couche : ")
        color = input("Entrez la couleur de votre choix parmi celles disponibles : ")


        if bar_wave == "oui" :
            dash_wave = input("Tirets ou ligne continue ? (tirets/ligne) : ").strip().lower()
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
                "xy" : list(zip(poly_x, poly_y)),
                "color" : color,
                "label" : label,
                "linestyle" : 'dashed' if dash_wave == "tirets" else 'solid'
            }

            # Lance la fonction hatch() afin de demander si des hachures sont nécessaires, et lesquels utiliser
            hatch()

            if ask_hatch == "oui" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] :
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
                    else :
                        # Idem que le précédent commentaire sauf que c'est pour la majorité des motifs et non pour des exceptions comme juste au-dessus
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
            dash = input("Pointillés ou ligne continue ? (pointillés/ligne) : ").strip().lower()
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
                "color" : color,
                "linestyle" : 'dotted' if dash == "pointillés" else 'solid'
            }

            # Lance la fonction hatch() afin de demander si des hachures sont nécessaires et lesquels utiliser
            hatch()

            if ask_hatch == "oui" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] :
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
                    else :
                        # Idem que le précédent commentaire sauf que c'est pour la majorité des motifs et non pour des exceptions comme juste au-dessus
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
                facecolor = h["color"],
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
                if h["motif_type"] == "lines" :
                        ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                        # (ce sur quoi doit être mis le motif, type de motif (côté gauche de la barre, côté droit de la barre), (partie haute de la barre, partie basse de la barre))
                        ## "spacing" est l'espace entre chaque liste de points. Cela joue aussi bien sur l'espace vertical qu'horizontal (sauf pour l'espace vertical pour "racines", puisque dans custom_hatches/draw_racines, l'argument "spacing" a été enlevé pour dy)
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
                        ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = "white")
                        custom_hatches.draw_racines(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'white')
                if h["motif_type"] == "dots" :
                        ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                        custom_hatches.draw_dots(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')


            # Stocke les données de "labels" pour être utilisé plus tard avec "annotate" pour la légende
            labels.append(h["label"])
        
        
            # Calcul le milieu de la barre (ajusté pour la largeur des barres)
            bar_x = h["x"][0] + (bar_width - 0.5)
            bar_y = h["bottom"] + h["y"] / 2

            # Annote la barre avec une ligne et le nom de la barre (qui correspond au label)
            ax.annotate(
                h["label"],
                xy = (bar_x, bar_y),
                # Positionne le nom de la barre à droite de la ligne 
                xytext = (bar_x + 1, bar_y),
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
                facecolor = h["color"],
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

            # Stocke les données de "labels" pour être utilisé plus tard avec "annotate" pour la légende
            labels.append(h["label"])
            
            
            # Détermine la valeur de x la plus à droite et la moyenne de y pour le placement du label plus tard
            poly_xs, poly_ys = zip(*h["xy"])

            # Récupère la valeur de "motif", si ce n'est pas None, rempli le polygone avec la bonne hachure et la dessine
            if h.get("motif") is not None :
                if h["motif_type"] == "lines" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        # (ce sur quoi doit être mis le motif, type de motif, positions de xy (afin que x et y max et min puissent être utilisé juste après) (côté gauche de la barre, côté droit de la barre), (partie haute de la barre, partie basse de la barre))
                        ## "spacing" est l'espace entre chaque liste de points. Cela joue aussi bien sur l'espace vertical qu'horizontal (sauf pour l'espace vertical pour "racines", puisque dans custom_hatches/draw_racines, l'argument "spacing" a été enlevé pour dy)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                if h["motif_type"] == "grid" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.2, color = 'black')
                if h["motif_type"] == "multilines" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.2, color = 'black')
                if h["motif_type"] == "slash" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.0, color = 'black')
                if h["motif_type"] == "racines" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_racines_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'white')
                if h["motif_type"] == "dots" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_dots_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')


            # Détermine les positions de x et y pour le "label" et son positionnement dans annotate()
            label_x = max(poly_xs) + 0.5
            label_y = sum(poly_ys) / len(poly_ys)
            

            # Utilise le point le plus à droite (- 0,5) pour le début de la flèche
            arrow_start = (max(poly_xs) - 0.5, label_y)
            
            # Annote le polygone avec une ligne et le nom du polygone (qui correspond au label)
            ax.annotate(
                h["label"],
                xy = arrow_start,
                # Positionne le nom de la barre à droite de la ligne
                xytext = (label_x, label_y),
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



# MIT License :
    # Copyright (c) 2024 Mathys B., aka Γucky

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