# DXF_plotter

Projet d'un traceur de DXF à main levé intuitif et facile d'utilisation basé sur le principe d'un bras SCARA muni de capteurs de position angulaire dans chaque articulation.

# Inspiration

Le projet est inspiré du concept de l'entreprise *Arcdroid* qui propose une machine de découpe plasma sous forme de bras robotique avec une fonction de traçage "à la main" de la pièce à découper.

L'idée est donc d'essayer de reproduire cette fonction de reproduction de pièce pour pouvoir ensuite la découper avec la machine de notre choix. Le tout en gardant le prix de production le plus réduit possible.

# Cahier des charges provisoire

La machine devra disposer des fonctionnalités suivantes :

### Tracé 
#### Obligatoire :
- Visualisation en direct de la forme tracée
- Possibilité de créer plusieurs courbes
- Possibilité de régler la hauteur du palpeur

#### Optionnel :
- Pilotage uniquement via l'interface de la machine : pas de contrôle depuis l'ordinateur
- Alimentation via port USB uniquement *(Si impossible, utiliser un chargeur de téléphone 5V)*
 
### Post-traitement 
#### Obligatoire :
- IHM claire et intuitive
- Fermeture automatique des courbes
- Lissage des courbes :
  
  - Lissage *main levée* : enlève simplement le bruit de mesure
  - Lissage *pièce mécanique* : lisse de manière à créer des lignes droites, des cercles et des arcs de cercle

- Algorithme de détection d'angle droit pour les pièces mécaniques : lorsqu'un angle après lissage est suffisamment proche de 90°, la courbe est modifiée pour créer un angle droit.
- Export en DXF *polyline*

#### Optionnel :

- Possibilité de déplacer des points à la main via un *offset* ou directement en renseignant les coordonées
- Mesure de distance entre deux points
- Export en DXF *splines*

