# Package-Affichage-LED-pour-Constellation-
Ce paquet permet de gérer l’affichage de différents paquets constellation sur une seule matrice LED RGB 8x32. Le paquet gère l’affichage d’une icône RGB (8x8), d’un texte blanc avec défilement ou alors directement d’une matrice 8x32 RGB (pour un affichage personnalisé).

## Installation
### Liste des composants 
Pour utiliser ce paquet vous aurez besoin des trois composants suivants :
* Matrice LED RGB 8x32 : [Amazon](https://www.amazon.fr/gp/product/B01DC0IPVU/)
* Raspberry Pi 3 : [Amazon](https://www.amazon.fr/Raspberry-Pi-Carte-Mère-Model/dp/B01CD5VC92/)
* 3x câble de connexion F/F : [Amazon](https://www.amazon.fr/Philonext-Multicolore-M%C3%A2le-Femelle-Femelle-Femelle-Breadboard/dp/B072NSLB98)

_Note:_ il est également possible d'utiliser un Raspberry Pi Zero à la place du Raspberry Pi 3, moins coûteux mais aussi non testé à la création du paquet !

### Connexion de la matrice LED 
La matrice LED possède 8 connexions différentes.

| Matrice pin | Description                 | RPi Pin | RPi Fonction |
| ----------- | --------------------------- | ------- | ------------ |
| **5V**      | Alimentation +5V            | 2       | 5V0          |
| **GND**     | Terre                       | 6       | GND          |
| **DIN**     | Entrée données              | 19      | GIO 10       |
| 5V          | Alimentation supplémentaire | •       | •            |
| DIN         | Entrée données              | •       | •            |
| _5V_        | Sortie                      | •       | •            |
| _GND_       | Sortie                      | •       | •            |
| _DOUT_      | Sortie                      | •       | •            |

Les **pins en gras** sont obligatoires pour l'affichage. 
Les _pins en italiques_ permettent de relier la matrice LED à une autre en série et donc de transférer l'information simplement. Les deux pins centraux ne sont utiles que dans le cas où de nombreuses LED sont utilisées à pleine puissance.

_Note:_ Il n'est pas recommandé d'allumer toutes les LED de la matrice en blanc en même temps.

### Configuration
_En cours de rédaction..._
