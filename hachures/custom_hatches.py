# Importing necessary libraries
# Import des librairies nécessaires
import numpy as np
from typing import List, Tuple
from shapely.geometry import Polygon, Point, LineString


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


# Draw hatches by tiling line segments defined by shape_to_lines
# Dessine les hachures avec les segments définis par shape_to_lines
def draw_hatch(ax, lines : List[Tuple[np.ndarray, np.ndarray]],
               xlim : Tuple[float, float], ylim : Tuple[float, float],
               spacing : float = 0.5, color : str = 'black') -> None :
    xmin, xmax = xlim
    ymin, ymax = ylim
    # Tile the pattern across boundaries and add some space between each repetition
    # Place le motif parmi les limites du graphique et ajoute un peu d'espace entre chaque répétition
    for dx in np.arange(xmin, xmax, spacing) : 
        for dy in np.arange(ymin, ymax, spacing) :
            for (p1, p2) in lines :
                x = [p1[0] + dx, p2[0] + dx]
                y = [p1[1] + dy, p2[1] + dy]
                # Last argument is the order in which elements are drawn (higher = in front)
                # Le dernier argument correspond à l'ordre dans lequel les éléments sont dessinés (plus grand = devant)
                ax.plot(x, y, color = color, linewidth = 1, zorder = 2)

# Same as draw_hatch but clipped to a polygon
# Idem que draw_hatch mais tronqué pour les limites d'un polygone
def draw_hatch_clipped_for_poly(ax, lines, polygon_xy, xlim, ylim, spacing = 0.5, color = 'black') :
    poly = Polygon(polygon_xy)
    xmin, xmax = xlim
    ymin, ymax = ylim
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
                    ax.plot(x, y, color = color, linewidth = 1, zorder = 3)
                elif clipped.geom_type == "MultiLineString" :
                    for seg in clipped.geoms :
                        x, y = seg.xy
                        ax.plot(x, y, color = color, linewidth = 1, zorder = 3)

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
                ax.plot(x, y, marker = 'o', color = color, markersize = 2, zorder = 2)

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
                ax.plot(x, y, color = color, linewidth = 1, zorder = 2)

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


# Defining various hatch patterns as lists of points
## Each point is defined as a numpy array with its x and y coordinates
# Définis les divers motifs de hachures comme des listes de points
## Chaque point est défini avec numpy array via ses coordonnées x et y

# Large grid : for limestone
# Quadrillage élargi : pour calcaire
large_grid = [
    np.array([0.0, 0.0]),
    np.array([0.2, 0.0]),
    np.array([0.2, 0.2]),
    np.array([0.2, 0.0]),
    np.array([0.4, 0.0]),
    np.array([0.6, 0.0]),
    np.array([0.6, -0.2]),
    np.array([0.6, 0.0]),
    np.array([0.8, 0.0]),
    np.array([1.0, 0.0]),
    np.array([1.0, 0.2]),
    np.array([1.0, 0.0])
]

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

# Wave shape : for localised iron precipitation
## The "ol" and "or" stand for "outer left" and "outer right", while "il" and "ir" stand for "inner left" and "inner right"
# Forme d'onde : pour précipitation localisée de fer
## Les "ol" et "or" signifient "outer left" (extérieur gauche) et "outer right" (extérieur droit), tandis que "il" et "ir" signifient "inner left" (intérieur gauche) et "inner right" (intérieur droit)

# First line
# Première ligne
vibe_ol = [
    np.array([0.1, 0.3]),
    np.array([0.1, 0.8])
]
### Second line
### Deuxième ligne
vibe_il = [
    np.array([0.15, 0.1]),
    np.array([0.15, 1.0])
]
### Third line
### Troisième ligne
vibe_ir = [
    np.array([0.2, 0.1]),
    np.array([0.2, 1.0])
]
### Fourth line
### Quatrième ligne
vibe_or = [
    np.array([0.25, 0.3]),
    np.array([0.25, 0.8])
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
    np.array([0.1, 1]),
    np.array([1, 0.1])
]

# Diagonal line in mirror : for particulate horizon
# Ligne en diagonale en miroir : pour horizon particulaire
reversed_slash = [
    np.array([0.1, 0.1]),
    np.array([1, 1])
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


# Converting shapes into line segments using the functions defined above
# Convertis les formes en segments en utilisant les fonctions définies plus haut
## Defining each line to create the wave shape
## Définition de chaque ligne pour réaliser la forme d'onde
line1 = shape_to_lines(*vibe_ol)
line2 = shape_to_lines(*vibe_il)
line3 = shape_to_lines(*vibe_ir)
line4 = shape_to_lines(*vibe_or)

## Defining each line to create the particulate horizon
## Définition de chaque ligne pour réaliser l'horizon particulaire
slash1 = shape_to_lines(*slash)
slash2 = shape_to_lines(*reversed_slash)

## Defining roots lines as an open shape
## Définis le motif de racines comme une forme ouverte
openlines = open_shape(*racines)        



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