import math

# Constantes
G = 6.67430e-11            # Constante gravitationnelle
M_TERRE = 5.97219e24       # Masse de la Terre (kg)
M_LUNE = 7.3477e22         # Masse de la Lune (kg)

# Positions initiales (1D)
x_terre = 0.0
x_lune = 3.844e8  # ~384 400 km

# Vitesses initiales (1D)
v_terre = 0.0
v_lune = 0.0

# Paramètres temporels
t = 0.0
dt = 60.0      # 60 s (1 minute)
T_MAX = 3600.0 # exemple : 1 heure total

while t <= T_MAX:
    # 1) Calcul de la distance Terre-Lune
    dx = x_lune - x_terre
    r = abs(dx)

    # 2) Calcul de la force gravitationnelle
    #    F = G * (m1 * m2) / r^2
    #    On évite la division par zéro
    if r == 0.0:
        F = 0.0
    else:
        F = G * M_TERRE * M_LUNE / (r*r)

    # 3) Gérer le sens de la force (si la Lune est à droite de la Terre, la force sur la Lune est dirigée vers la Terre, donc négative en x)
    #    dx > 0 => la Lune est à droite, la Lune subit une force vers la gauche.
    if dx > 0:
        force_lune = -F
    else:
        force_lune = F

    # Par action-réaction, la Terre subit la force opposée
    force_terre = -force_lune

    # 4) Calcul des accélérations a = F / m
    a_lune = force_lune / M_LUNE
    a_terre = force_terre / M_TERRE

    # 5) Mise à jour des vitesses (Euler)
    v_lune = v_lune + a_lune * dt
    v_terre = v_terre + a_terre * dt

    # 6) Mise à jour des positions (Euler)
    x_lune = x_lune + v_lune * dt
    x_terre = x_terre + v_terre * dt

    # 7) Affichage (optionnel)
    print(f"t={t:.0f}s  r={r:.2e}m  v_lune={v_lune:.3e}m/s  x_lune={x_lune:.3e}m")

    # 8) Avancer le temps
    t += dt
