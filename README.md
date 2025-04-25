# Tri Automatique d'Objets par Couleur

Ce projet réalise un tri automatique d'objets (par exemple, des fruits) dans une vidéo en fonction de leur couleur dominante. Il permet d'identifier et de classer trois types de fruits selon leur teinte : 

- **Rouge** : Tomate
- **Orange** : Orange
- **Vert** : Citron vert

## Fonctionnement

1. **Zone d'Intérêt (ROI)** : Une zone d'intérêt est définie dans chaque image de la vidéo.
2. **Conversion en HSV** : L’image dans la ROI est convertie en espace HSV pour faciliter l’analyse des couleurs.
3. **Histogramme des Teintes** : Un histogramme des teintes est calculé pour détecter la couleur dominante dans la zone.
4. **Masques HSV** : Des masques HSV sont utilisés pour renforcer la précision de la détection (ex : pour la détection du vert).
5. **Affichage** : Le nom de la couleur (et donc du fruit détecté) est affiché sur la vidéo avec une boîte englobante.

## Utilisation

Ce système peut être utilisé dans des applications de tri industriel, robotique ou d'agriculture automatisée.

### Prérequis

- Python 
- OpenCV
- NumPy

