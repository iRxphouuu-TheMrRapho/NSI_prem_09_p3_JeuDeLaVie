# Jeu de la vie

Ce projet est un Jeu de la vie créé par Gabriel et Raphaël et conçu initialement par Monsieur Pioche (https://github.com/jimpioche)

Ce projet est un Jeu de la vie dont les règles ont été revues par Gabriel et Raphaël. Le Jeu de la vie est au automate cellulaire imaginé par John Horton Conway en 1970. Malgré des règles qui paraissent simples au premier regard, il est "Turing-complet". C'est un jeu de de simulation au sens mathématiques. Le jeu de la vie peut être qualifié de jeu à zéro joueur car il ne nécessite aucune intervention lors de son déroulement. Il s'agit d'un automate cellulaire, un modèle où chaque état conduit mécaniquement à l'état suivant à partir de règles préétablies.

Le principe est simple, lorsque le joueur lance le jeu, il peut dessiner ce qu'il souhaite dans la grille où importer un "schematic" pré-existant. Lorsque le joueur est satisafait de sa création, il n'a plus qu'à lancer le jeu en appuyant sur le bouton "Play", ce qui lance le jeu de la vie. A partir de là, il peut obsever l'évolution de sa création initiale. Il peut mettre le jeu sur pause, revenir en arrière ou en avant, et lorsque le jeu est en pause, ajouter ou supprmer des cellules, et le tout, à sa guise. A la fin de la simulation, l'utilisateur peut voir deux choses différentes : Les cellules se sont toutes stabilisées et plus aucune évolution interne au jeu n'est possible (sans que le joueur ne rajoute d'autres cellules), ou toutes les cellules sont mortes, et il n'y en a donc plus sur la grille, et dans ce cas là, à moins d'une intervention de l'utilisateur, il n'y a plus d'évolution possible.

Tout le code de base a été imaginé par Monsieur Pioche. Des fonctions ou des modifications des règles du jeu de la vie on été rajoutées par la suite

## Répartition des Taches

La répartition des tâches pour le projet est la suivante : 
```
La recherche et l'établissement du cachier des charges : Gabriel et Raphaël
Différentes règles du jeu de la vie : Raphaël
Ajout du menu déroulant de sélection des règles de vie : Raphaël et M. Pioche
Ajout de couleurs aléatoires : Raphaël
Ajout du chargement de gif par le jeu de la vie : Gabriel
...
...
```

## Etapes de Réalisations

Dans un premier temps, nous nous sommes familiarisés avec le jeu de la vie. Sans modifier les règles de vies ou de mort, nous avons appris à générer des figures à des endroits précis en lançant le jeu. Cette familiarisation nous a permis de mieux comprendre comment le jeu, ainsi que le code fonctionnaient, et nous avons donc pu établir un cahier des charges.

Ce cachier des charges a évoulué tout au long du projet, selon notre avancement, et ce qui était possible de faire ou ne pas faire avec les moyens mis à notre disposition et le temps accordé au projet.
Ainsi le cahier des charges comportes deux grandes parties : une partie "ajouts" et une partie "modifications".
```
Dans la partie ajout nous avions pour ambition d'ajouter plusieurs choses : 
différentes couleurs pour les cellules vivantes 
(fait),
Un fonction permettant de déplacer le schématic une fois importer via des touches 
(flèches directionnelles par exemple) (idée abandonnée),
pouvoir exporter le contenu de la grille en .png (photo) et .mp4 (vidéo) (idées abandonnées).
Association d'une cellule et d'une note de musique. Lorsqu'une cellule vient de naître, cette dernière 
émet un son. 
Tout les sons sont enregistrés puis tout est convertit chronologiquement dans un fichier mp3.
Ajout d'une durée de vie limitée pour chaque cellule (en cours)
Ajout de différentes règles du jeu de la vie. (en cours)
Ajout de différents "mode de jeu" (abandonné)
Prise en compte par le jeu de la vie de gifs (fait)
```

Lors de la réalisation du projet nous avons tout fait de façon désordée en avançant à l'aveuglette dans ce que nous faisions. 


## Fonctionnement de l'interface graphique
Voici les différetes fonctions de l'interface graphique :
```
Bouton Play : lance le jeu 
Bouton Pause : coupe le jeu
Flèches allant vers la gauche ou la droite : permet de load la scène précédente / suivante.
Couper : Coupe la sélection
Coller : Colle la sélection
Copier : Copie la sélection
Reset : Nettoie toute la grille pour la remettre à un état immaculée (sans cellule)
Quitter : Quitte le jeu
Menu déroulant le plus à gauche : load un schematic
Bouton + : save le schematic
Menu déroulant plus à droite sur la même ligne : permet de choisir une règle du jeu de la vie. 
Grille (à l'arrêt) : clique gauche place une cellule; flèches directionnelles : à la manière du snake, 
crée une ligne de cellules vivantes. Sélectionner (clique gauche en laissant appuyer puis en bougeant le curseur) : 
crée une grosse zone de cellules vivates. Toutes ces actions précédentes peuvent aussi servir à faire le contraire 
(tuer la cellule)
```

## Fonctions notables

Il existe différentes fonctions essetielles au bon fonctionnement du projet qui sont dans les différents fichiers python :

jdlv_my_tools
```
apply_game_of_life_rules : règles du jeu de la vie : condition
de vie ou de mort des différentes cellules. Ces règles sont reprises
et modifiées dans les fonction R0_rules, R1_rules, R2_rules...
manage_rules : permet de choisir une règles de vie R0, R1, R2 et de 
l'appliquer à la place de l'apply_game_of_life_rules
apply_rules : applique les règles de vie
``` 
jdlv_main
```
Permet de lancer le JEU DE LA VIE !!!! ^^
``` 
Jdlv_Vue_fromUI et jdlv_ui 
```
Liaisons entre les boutons du controleur et les fonctions
``` 
jdlv_controleur
```
La création de différents boutons et menus déroulants
```
jdlv_data
```
La forme de la grille les couleurs, le nombre de cases
```
jdlv_outils 
```
La couleur aléatoire et d'autres choses
```
## Installation
Le projet requière Python en version 3.10.2
Le projet requiere les différentes librairies suivantes : 
```
os (avec listdir)
sys
time
threading
PyQt5 (avec QtCOre, QtWidgets, QtGui)
PyQt5.QtCore (avec QObject, QThread, pyqtSignal, QCoreApplication, QRunnable, QThreadPool)
PyQt5.QtGui (QIcon, QPixmap)
random
json
os.path (avec isfile, join)
```
Après avoir executé le fichier nommé ``app.py``, suivez les instructions et cliquer sur le lien affiché sur la console.
