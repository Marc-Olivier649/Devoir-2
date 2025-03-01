<<<<<<< HEAD
import numpy as np
from pointfixe import pointfixe  # Importation de la fonction pointfixe

# Définition des fonctions
def f(x):
    return (x + 1) * (x - 1)**2

def g(x):
    return x - f(x) / 5

# Paramètres
x0 = -1.5  # Point de départ pour r1 = -1
nmax = 50  # Nombre maximum d'itérations
tolr = 1e-7  # Tolérance

# Application de la méthode du point fixe
resultat = pointfixe(g, x0, nmax, tolr)

# Affichage des résultats
print("Suite des approximations :", resultat)
=======
import numpy as np
from pointfixe import pointfixe  # Importation de la fonction pointfixe

# Définition des fonctions
def f(x):
    return (x + 1) * (x - 1)**2

def g(x):
    return x - f(x) / 5

# Paramètres
x0 = -1.5  # Point de départ pour r1 = -1
nmax = 50  # Nombre maximum d'itérations
tolr = 1e-7  # Tolérance

# Application de la méthode du point fixe
resultat = pointfixe(g, x0, nmax, tolr)

# Affichage des résultats
print("Suite des approximations :", resultat)
>>>>>>> 76be351553c23bc86535b0cd70878562fe5f4e66
print("Valeur finale trouvée :", resultat[-1])