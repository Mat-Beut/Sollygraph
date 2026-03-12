# Defines my subfolders
# Définition de mes fichiers sous-jacents
__all__ = ["flag"]

# Import files so they can be read by setup.py
# Import des fichiers pour la lecture par le fichier setup.py
from . import flag

# Pas sûr que ça soit utile les fichiers __init__.py dans mon code, ça marche sans
## Pour setup.py et flag.py, faut que j'effectue des tests pour voir si je peux pas supprimer ces fichiers