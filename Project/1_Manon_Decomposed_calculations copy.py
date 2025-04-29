import math
import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
MTerre = 5.97219e24
MLune = 7.3477e22

positionT = [0,0,0]
positionL = [3.844e8, 0, 0]

# Distance
dx = positionL[0] - positionT[0]
dy = positionL[1] - positionT[1]
dz = positionL[2] - positionT[2]

# l'intervalle de temps au bout de laquelle on calcule la nouvelle position
dT = 600.0

# calcul de la distance entre les deux astres avec le théorème de Pythagore 3 dimensions
d = math.sqrt(dx*dx + dy*dy + dz*dz)

# print("La distance est de :", d) = 
print(f"La distance est de : {d}")

F = G * MTerre * MLune / d**2
print(f"La force est de : {F} N") 


# accélération Lune
aL = F/MLune
print(f"L'accélération de la Lune est de : {aL} m.s^-2")

# accélération Terre
aT = F/MTerre
print(f"L'accélération de la Terre est de : {aT} m.s^-2")


# différence de vitesse qu'on rajoute à chaque fois
vL += aL*dT 
vT += aT*dT
# += = rajoute à la valeur d'avant

# Mise à jour des positions (Euler)

