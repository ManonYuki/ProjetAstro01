# Projet : Simulation de Systèmes Stellaires et Planétaires avec Python et Intelligence Artificielle

## Objectif
Réaliser une simulation numérique d'un système stellaire et planétaire en utilisant Python, en intégrant éventuellement des algorithmes d'intelligence artificielle pour analyser les données issues de la simulation.

---

## Phase 1 : Modélisation de la gravitation

### Objectifs
- Implémenter les lois de la gravitation de Newton.  
- Créer un modèle de simulation des interactions gravitationnelles entre plusieurs corps.  
- Se familiariser avec Jupyter Notebook pour tester et exécuter des segments de code interactifs.

### Outils et Compétences
- **Python, NumPy** : pour les calculs mathématiques (vecteurs, matrices, fonctions trigonométriques).  
- **Jupyter Notebook** : pour une approche interactive du développement, idéal pour tester des petites portions de code.  
- **Bases de la physique gravitationnelle** : comprendre la loi de Newton (F = G × M1 × M2 / r²) et les notions de force, vitesse, et accélération.

---

### Plan détaillé

#### 1. Préparation de l'environnement
- **Installation de Python et Jupyter Notebook** : Vérifier que vous avez Python 3.x et Jupyter. Vous pouvez utiliser Anaconda pour simplifier l’installation.  
- **Création d’un nouveau notebook** : Dans Jupyter, créez un nouveau notebook pour ce projet. Vous pourrez y organiser vos tests de code et vos calculs.  
- **CorpsCeleste\*\*\*\*** *Vecteurs position, vitesse, accélération* : comprendre comment relier la force (F) à l’accélération (a), via la deuxième loi de Newton (F = m × a).  
- **Choisir son système d’unités** : déterminer si vous utilisez le Système International (SI) ou des unités simplifiées (ex. masses réduites, distances en UA).

---

#### 2. Conception de la classe *CorpsCeleste*

- **Attributs** :  
  - `masse` : la masse du corps.  
  - `position` : un vecteur (x, y) ou (x, y, z) selon la 2D ou la 3D.  
  - `vitesse` : le vecteur vitesse du corps.  
  - `force` : le vecteur force subi par le corps (calculé à chaque itération).

- **Méthodes** :  
  - `mettre_a_jour_force()` : calcule la force nette subie par le corps (somme de toutes les forces gravitationnelles).  
  - `maj_position_et_vitesse()` : met à jour la position et la vitesse en fonction de la force (intégration temporelle).

- **Représentation** *(optionnel)* :  
  - Méthode `__str__` pour imprimer les infos du corps de manière lisible.

---

#### 3. Implémentation de la formule de la force gravitationnelle
- **Constante gravitationnelle (G)** : définir la valeur de G (6.67430e-11 en SI) ou ajuster selon le système d’unités.  
- **Calcul des forces** :  
  1. Pour chaque paire de corps (i, j), calculer le vecteur distance `r_vec = position_j – position_i`.  
  2. Calculer la distance `r = ||r_vec||`.  
  3. Calculer la force scalaire `F = G × (Mi × Mj) / (r²)`, puis la direction du vecteur force `r_vec / r`.  
  4. Appliquer la force en conséquence : corps i reçoit +F, corps j reçoit –F (loi de l’action et de la réaction). Généralement, on additionne simplement à la force existante.

---

#### 4. Intégration temporelle
- **Choix du pas de temps (`dt`)** :  
  - Trop grand → imprécis,  
  - Trop petit → demande plus de ressources.  
- **Schéma d’intégration (Euler ou Verlet)** :  
  - **Euler simple** :  
    ```txt
    v(t+dt) = v(t) + (F(t)/m) × dt
    p(t+dt) = p(t) + v(t) × dt
    ```
  - **Verlet ou Leapfrog** : plus précis pour les systèmes dynamiques.

---

#### 5. Expérimenter avec Jupyter Notebook
- **Essais progressifs** :  
  - Tester la force entre deux corps simples (par ex. 1 kg et 1 kg à 1 m) pour vérifier les valeurs.  
  - Vérifier que les vitesses se mettent correctement à jour.  
- **Visualiser la progression des calculs** : à chaque étape, afficher la position du corps pour voir s’il se rapproche ou s’éloigne comme prévu.  
- **Manipuler les variables** : changer la masse d’un corps ou sa distance initiale, relancer la cellule et observer l’impact.

---

#### 6. Validation des premiers résultats
- **Calculs analytiques** : pour un système à deux corps, on peut comparer les trajectoires (ex. orbite circulaire, orbite elliptique) à des formules classiques.  
- **Graphiques simples** : tracer la position de chaque corps en fonction du temps.  
- **Contrôle de la conservation de l’énergie** *(optionnel)* : calculer l’énergie totale (cinétique + potentielle) à chaque itération pour voir si elle reste à peu près constante.

---

### Conseils pratiques
- **Commencez par un système à deux corps** (étoile-planète) pour valider vos formules.  
- **Documentez** bien votre code et notez vos observations dans le notebook.  
- N’hésitez pas à faire des impressions (`print`) intermédiaires ou des tracés pour comprendre la dynamique.  
- Si vous avez quelques bases d’IA ou d’analyse de données, vous pouvez stocker chaque étape de la simulation (positions, vitesses) dans un **DataFrame Pandas** pour les analyser plus tard.
