# Importing necessary libraries
# Import des librairies nécessaires
import numpy as np
from typing import List, Tuple
from shapely.geometry import Polygon, Point, LineString
from matplotlib.patches import Circle


# Convert a shape (list of points) into line segments
## Points corresponds to the x and y coordinates of the points defined below, then lists the x and y points in an array, then the array is drawn as patchwork
### Regarding the use of "*" before a variable, if I understood correctly it's a pointer, it's used to make sure the arrays are correctly detected and imported in the function
# Convertis une forme (liste de points) en segments
## Les points correspondent aux coordonnées x et y des points définis plus bas, puis liste les points x et y dans une suite, puis la suite est tracé en mosaïque
### Concernant "*" avant le nom d'une variable, si j'ai bien compris, il s'agit d'un pointeur, ça a pour but de s'assurer que les suites sont correctement détectées et leurs valeurs correctement importées dans la fonction
def shape_to_lines(*points : np.ndarray) -> List[Tuple[np.ndarray, np.ndarray]] :
    return [(points[i], points[(i + 1) % len(points)]) for i in range(len(points))]

# Same as shape_to_lines except that the first and last points are not connected
# Idem que shape_to_lines sauf que le premier point et le dernier point ne sont pas reliés
def open_shape(*points : np.ndarray) -> List[Tuple[np.ndarray, np.ndarray]] :
    return [(points[i], points[i + 1]) for i in range(len(points) - 1)]

# Patched pattern for pattern 16 (to use with draw_circles_patches)
# Motif en patch pour le motif 16 (à utiliser avec draw_circles_patches)
circle_patch = Circle((0.1, 0.1), 0.1, fill = False, linewidth = 1)

# Draw hatches by tiling line segments defined by shape_to_lines
# Dessine les hachures avec les segments définis par shape_to_lines
def draw_hatch(ax, lines : List[Tuple[np.ndarray, np.ndarray]],
               xlim : Tuple[float, float], ylim : Tuple[float, float],
               spacing : float = 0.5, color : str = 'black', **kwargs) -> None :
    xmin, xmax = xlim
    ymin, ymax = ylim
    # Kwargs allows to pass additional parameters to the ax.plot function, such as linewidth for example
    ## It's used here so the parameter isn't fixed nor gets duplicated when it's different in input_data.py
    ### .pop and not .get because if we use .get we get an error because the parameter is passed to ax.plot which doesn't recognize it, while .pop removes the parameter from kwargs so it won't be passed to ax.plot
    # Kwargs permet de passer des paramètres supplémentaires à la fonction ax.plot, comme linewidth (épaisseur des traits dans un motif) par exemple
    ## C'est utilisé ici pour que le paramètre ne soit pas fixe ni dupliqué lorsqu'il est différent dans input_data.py
    ### .pop et pas .get parce que si on utilise .get on a une erreur car la valeur est transmise à ax.plot qui ne la reconnaît pas, alors que .pop supprime le paramètre de kwargs une fois utilisé pour qu'il ne soit pas passé à ax.plot
    lw = kwargs.pop('linewidth', kwargs.pop('lw', 1))
    # Tile the pattern across boundaries and add some space between each repetition
    # Place le motif parmi les limites du graphique et ajoute un peu d'espace entre chaque répétition
    for dx in np.arange(xmin, xmax, spacing) : 
        for dy in np.arange(ymin, ymax, spacing) :
            for line in lines :
                p1 = line[0] + np.array([dx, dy])
                p2 = line[1] + np.array([dx, dy])                
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=lw, zorder = 1, **kwargs)


# Same as draw_hatch but clipped to a polygon
# Idem que draw_hatch mais tronqué pour les limites d'un polygone
def draw_hatch_clipped_for_poly(ax, lines, polygon_xy, xlim, ylim, spacing = 0.5, color = 'black', **kwargs) :
    poly = Polygon(polygon_xy)
    xmin, xmax = xlim
    ymin, ymax = ylim
    # Kwargs allows to pass additional parameters to the ax.plot function, such as linewidth for example
    ## It's used here so the parameter isn't fixed nor gets duplicated when it's different in input_data.py
    ### .pop and not .get because if we use .get we get an error because the parameter is passed to ax.plot which doesn't recognize it, while .pop removes the parameter from kwargs so it won't be passed to ax.plot
    # Kwargs permet de passer des paramètres supplémentaires à la fonction ax.plot, comme linewidth (épaisseur des traits dans un motif) par exemple
    ## C'est utilisé ici pour que le paramètre ne soit pas fixe ni dupliqué lorsqu'il est différent dans input_data.py
    ### .pop et pas .get parce que si on utilise .get on a une erreur car la valeur est transmise à ax.plot qui ne la reconnaît pas, alors que .pop supprime le paramètre de kwargs une fois utilisé pour qu'il ne soit pas passé à ax.plot
    lw = kwargs.pop('linewidth', kwargs.pop('lw', 1))
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax, spacing) :
            for line in lines :
                p1 = line[0] + np.array([dx, dy])
                p2 = line[1] + np.array([dx, dy])
                # Create a shapely LineString for the pattern's lines
                # Crée une LineString shapely pour les lignes du motif
                motif_line = LineString([tuple(p1), tuple(p2)])
                clipped = poly.intersection(motif_line)
                # Bruteforce clipping so patterns can be cut if needed so it fits in the polygon
                # Force les motifs à rentrer dans les polys en les coupant si besoin
                if clipped.is_empty :
                    continue
                if clipped.geom_type == "LineString" :
                    x, y = clipped.xy
                    ax.plot(x, y, color = color, linewidth = lw, zorder = 3, **kwargs)
                elif clipped.geom_type == "MultiLineString" :
                    for seg in clipped.geoms :
                        x, y = seg.xy
                        ax.plot(x, y, color = color, linewidth = lw, zorder = 3, **kwargs)

# Same as draw_hatch but it doesn't connect points and draw lines between them
# Idem que draw_hatch mais ne connecte pas les points, évitant de tracer des lignes entre eux
def draw_dots(ax, dots : List[np.ndarray],
               xlim : Tuple[float, float], ylim : Tuple[float, float],
               spacing : float = 0.5, color : str = 'black') -> None :
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax, spacing) :
            for p in dots :
                x = p[0] + dx
                y = p[1] + dy
                # Marker 'o' draws dots, markersize is the size of the dot
                # Le marker 'o' dessine des points, markersize c'est la taille du point
                ax.plot(x, y, marker = 'o', color = color, markersize = 2, zorder = 1)

# Same as draw_dots but clipped to a polygon
# Idem que draw_dots mais tronqué pour les limites d'un polygone
def draw_dots_clipped_for_poly(ax, dots : List[np.ndarray],
                              polygon_xy : List[np.ndarray],
                              xlim : Tuple[float, float], ylim : Tuple[float, float],
                              spacing : float = 0.5, color: str = 'black') -> None :
    poly = Polygon(polygon_xy)
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax, spacing) :
            for p in dots :
                x = p[0] + dx
                y = p[1] + dy
                pt = Point(x, y)
                if poly.contains(pt) :
                    ax.plot(x, y, marker = 'o', color = color, markersize = 2, zorder = 3)

def draw_circles(ax, dots : List[np.ndarray],
               xlim : Tuple[float, float], ylim : Tuple[float, float],
               spacing : float = 0.5, color : str = 'black') -> None :
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax, spacing) :
            for p in dots :
                x = p[0] + dx
                y = p[1] + dy
                # Marker 'o' draws dots, markersize is the size of the dot
                # Le marker 'o' dessine des points, markersize c'est la taille du point
                ax.plot(x, y, marker = 'o', markeredgecolor = color, markerfacecolor = 'none', markersize = 15, zorder = 1)

# Draw circles using matplotlib Circle patches (used for pattern 16)
# Dessine les cercles avec des patches Circle matplotlib (utilisé pour le motif 16)
def draw_circles_patches(ax, dots : List[np.ndarray],
                         xlim : Tuple[float, float], ylim : Tuple[float, float],
                         spacing : float = 0.5, color : str = 'black', radius : float = 0.08) -> None :
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax, spacing) :
            for p in dots :
                x = p[0] + dx
                y = p[1] + dy
                circle_patch = Circle((x, y), radius=radius, fill=False, edgecolor=color, linewidth=1, zorder=1)
                ax.add_patch(circle_patch)

# Same as draw_circles_patches but clipped to a polygon
# Idem que draw_circles_patches mais tronqué pour les limites d'un polygone
def draw_circles_patches_clipped_for_poly(ax, dots : List[np.ndarray],
                                         polygon_xy : List[np.ndarray],
                                         xlim : Tuple[float, float], ylim : Tuple[float, float],
                                         spacing : float = 0.5, color: str = 'black', radius : float = 0.05) -> None :
    poly = Polygon(polygon_xy)
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax, spacing) :
            for p in dots :
                x = p[0] + dx
                y = p[1] + dy
                pt = Point(x, y)
                # Only draw circle if center point is inside the polygon
                ## N.B. This means that circles that would be partially inside the polygon
                ### but with their center outside won't be drawn, thus avoiding clipping issues
                # Dessine seulement les cercles dont le point central est à l'intérieur du polygone
                ## N.B. Cela signifie que les cercles qui seraient partiellement à l'intérieur du polygone
                ### mais avec leur centre à l'extérieur ne seront pas dessinés, évitant ainsi les problèmes de cliping
                if poly.contains(pt) :
                    circle_patch = Circle((x, y), radius=radius, fill=False, edgecolor=color, linewidth=1, zorder=3)
                    ax.add_patch(circle_patch)

# Same as draw_hatch but without the y spacing, otherwise it draws a spiral shape
# Idem que draw_hatch mais sans l'espacement en y, sinon ça dessine une forme hélicoïdale
def draw_racines(ax, lines: List[Tuple[np.ndarray, np.ndarray]],
               xlim: Tuple[float, float], ylim: Tuple[float, float],
               spacing: float = 0.5, color: str = 'black') -> None :
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax) :
            for (p1, p2) in lines :
                x = [p1[0] + dx, p2[0] + dx]
                y = [p1[1] + dy, p2[1] + dy]
                ax.plot(x, y, color = color, linewidth = 1, zorder = 1)

# Same as draw_racines but clipped to a polygon
# Idem que draw_racines mais tronqué pour les limites d'un polygone
def draw_racines_clipped_for_poly(ax, lines, polygon_xy, xlim, ylim, spacing = 0.5, color = 'black') :
    poly = Polygon(polygon_xy)
    xmin, xmax = xlim
    ymin, ymax = ylim
    for dx in np.arange(xmin, xmax, spacing) :
        for dy in np.arange(ymin, ymax) :
            for line in lines:
                p1 = line[0] + np.array([dx, dy])
                p2 = line[1] + np.array([dx, dy])
                motif_line = LineString([tuple(p1), tuple(p2)])
                clipped = poly.intersection(motif_line)
                if clipped.is_empty :
                    continue
                if clipped.geom_type == "LineString" :
                    x, y = clipped.xy
                    ax.plot(x, y, color = color, linewidth = 1, zorder = 3)
                elif clipped.geom_type == "MultiLineString" :
                    for seg in clipped.geoms :
                        x, y = seg.xy
                        ax.plot(x, y, color = color, linewidth = 1, zorder = 3)


# Plus shape : for silica
# Forme de plus : pour silice
plus = [
    np.array([0.1, 0.2]),
    np.array([0.2, 0.2]),
    np.array([0.2, 0.4]),
    np.array([0.2, 0.0]),
    np.array([0.2, 0.2]),
    np.array([0.3, 0.2])
]

# Reversed T shape : for something alternating (I genuinely have no idea what it's supposed to really represent, sorry...)
# Forme de T retourné : pour quelque chose d'alterné (je n’ai vraiment aucune idée de ce que c'est censé réellement représenter, désolé...)
reversed_t = [
    np.array([0.1, 0.2]),
    np.array([0.2, 0.2]),
    np.array([0.2, 0.0]),
    np.array([0.2, 0.2]),
    np.array([0.3, 0.2])
]

# Dashed vertical line shape : for Gley
# Forme de ligne verticale en pointillé : pour Gley
dashed_vline = [
    np.array([0.1, 0.2]),
    np.array([0.1, 0.4])
]

# Vertical line shape : for accumulation of iron
# Forme de ligne verticale : pour accumulation de fer
vline = [
    np.array([0.1, 0.0]),
    np.array([0.1, 1.0])
]

# Horizontal line shape : for limestone (to use with Vertical line shape -> Grid shape)
# Forme de ligne horizontale : pour calcaire (à utiliser avec Forme de ligne verticale -> Forme de grille)
hline = [
    np.array([0.0, 0.1]),
    np.array([0.2, 0.1])
]

# hline2 pour la chaux
hline2 = [
    np.array([0.0, 0.2]),
    np.array([0.2, 0.2])
]

# Full horizontal line : for clay 2/1 (other)
# Ligne horizontale pleine : pour argile 2/1 (autre)
hline_full = [
    np.array([0.0, 0.1]),
    np.array([0.5, 0.1])
]


# Wave shape : for localised iron precipitation
## The "ol" and "or" stand for "outer left" and "outer right", while "il" and "ir" stand for "inner left" and "inner right"
# Forme d'onde : pour précipitation localisée de fer
## Les "ol" et "or" signifient "outer left" (extérieur gauche) et "outer right" (extérieur droit), tandis que "il" et "ir" signifient "inner left" (intérieur gauche) et "inner right" (intérieur droit)

# First line
# Première ligne
vibe_ol = [
    np.array([0.1, 0.3]),
    np.array([0.1, 0.6])
]
### Second line
### Deuxième ligne
vibe_il = [
    np.array([0.15, 0.1]),
    np.array([0.15, 0.8])
]
### Third line
### Troisième ligne
vibe_ir = [
    np.array([0.2, 0.1]),
    np.array([0.2, 0.8])
]
### Fourth line
### Quatrième ligne
vibe_or = [
    np.array([0.25, 0.3]),
    np.array([0.25, 0.6])
]


# First line adapted for pattern 16
# Première ligne adaptée pour le motif 16
vibe_ol_16 = [
    np.array([0.07, 0.075]),
    np.array([0.07, 0.125])
]
### Second line adapted for pattern 16
### Deuxième ligne adaptée pour le motif 16
vibe_il_16 = [
    np.array([0.09, 0.05]),
    np.array([0.09, 0.15])
]
### Third line adapted for pattern 16
### Troisième ligne adaptée pour le motif 16
vibe_ir_16 = [
    np.array([0.11, 0.05]),
    np.array([0.11, 0.15])
]
### Fourth line adapted for pattern 16
### Quatrième ligne adaptée pour le motif 16
vibe_or_16 = [
    np.array([0.13, 0.075]),
    np.array([0.13, 0.125])
]



# Wave (alt) shape : for organic slightly decomposed
# Forme de vague : pour organique peu décomposé
orga_peu_decomp = [
    np.array([0.1, 0.2]),
    np.array([0.2, 0.3]),
    np.array([0.3, 0.2]),
    np.array([0.2, 0.3]),
    np.array([0.1, 0.2])
]

# Diagonal line : for lumpy horizon (also used for particulate horizon)
# Ligne en diagonale : pour horizon grumeleux (sers également pour horizon particulaire)
slash = [
    np.array([0.0, 1.0]),
    np.array([1.0, 0.0])
]

# Diagonal line in mirror : for particulate horizon
# Ligne en diagonale en miroir : pour horizon particulaire
reversed_slash = [
    np.array([0.0, 0.0]),
    np.array([1.0, 1.0])
]

# Zigzag shape : for roots
# Forme en zigzag : pour racines
racines = [
    np.array([0.1, 0.0]),
    np.array([0.5, 0.5]),
    np.array([0.1, 1.0])
]

# Dots : for sandstone
# Des points : pour grès
dots = [np.array([0.1, 0.1])]

# Circles : for free alumina
# Cercles : pour l'alumine libre
circles = [np.array([0.1, 0.1])]

## Defining each line to create the limestone's pattern
## Définition de chaque ligne pour réaliser le motif du calcaire
grid1 = shape_to_lines(*vline)
grid2 = shape_to_lines(*hline)

# Converting shapes into line segments using the functions defined above
# Convertis les formes en segments en utilisant les fonctions définies plus haut
## Defining each line to create the wave shape
## Définition de chaque ligne pour réaliser la forme d'onde
line1 = shape_to_lines(*vibe_ol)
line2 = shape_to_lines(*vibe_il)
line3 = shape_to_lines(*vibe_ir)
line4 = shape_to_lines(*vibe_or)

# Same as above but adapted for pattern 16
# Pareil que le bloc de ligne au-dessus, mais adapté pour le motif 16
line1_16 = shape_to_lines(*vibe_ol_16)
line2_16 = shape_to_lines(*vibe_il_16)
line3_16 = shape_to_lines(*vibe_ir_16)
line4_16 = shape_to_lines(*vibe_or_16)

## Defining each line to create the particulate horizon
## Définition de chaque ligne pour réaliser l'horizon particulaire
slash1 = shape_to_lines(*slash)
slash2 = shape_to_lines(*reversed_slash)        

# Defining each line for clay 2/1 (other)
# Définition de chaque ligne pour Argile 2/1 (pas kaolinite, l'autre)
hlineA = shape_to_lines(*hline)
hlineB = shape_to_lines(*hline2)

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