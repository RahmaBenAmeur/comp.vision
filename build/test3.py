"""
Ce programme réalise un tri automatique d'objets (ex: fruits) dans une vidéo en fonction de leur couleur dominante.
Dans cet exemple, il permet d'identifier et de classer trois types de fruits selon leur teinte :
- Rouge : Tomate
- Orange : Orange
- Vert : Citron vert

Fonctionnement :
1. Une zone d'intérêt (ROI) est définie dans chaque image de la vidéo.
2. L’image dans la ROI est convertie en espace HSV pour faciliter l’analyse des couleurs.
3. Un histogramme des teintes est calculé pour détecter la couleur dominante dans la zone.
4. Des masques HSV sont également utilisés pour renforcer la précision (ex: pour la détection du vert).
5. Le nom de la couleur (et donc du fruit détecté) est affiché sur la vidéo avec une boîte englobante.

Ce système peut être utilisé dans des applications de tri industriel, robotique ou d'agriculture automatisée.
"""


import cv2
import numpy as np

# Ouvrir la vidéo
cap = cv2.VideoCapture('video3.mp4')


# Définir le codec et créer un objet VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec pour le format de sortie
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (800, 500))  # 30 FPS, taille 800x500

# Définir la taille de la fenêtre d'affichage
resize_width = 800  
resize_height = 500  

# Définir la zone d'intérêt (ROI)
x, y, w, h = int(resize_width / 22), int(resize_height / 1.35), 80, 80  



while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Extraire la ROI
    roi = frame[y:y+h, x:x+w]

    # Convertir l'image de BGR à HSV
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Calculer l'histogramme pour le canal HSV
    hist_hue = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])  # Histogramme pour la teinte (H)

    # Trouver la teinte dominante
    dominant_hue = np.argmax(hist_hue)  # Trouver la teinte dominante

    # Définir des seuils pour classer la couleur
    if (dominant_hue >= 0 and dominant_hue <= 10) or (dominant_hue >= 160 and dominant_hue <= 180):  
        color = "Red"
    elif dominant_hue >= 11 and dominant_hue <= 25:  
        color = "Orange"
    elif dominant_hue >= 40 and dominant_hue <= 80:  
        color = "Green"
    else:
        color = ""
        
    # Utiliser des masques de couleur pour une détection plus précise
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv_roi, lower_green, upper_green)

    # Vérifier si le masque vert a des pixels
    if np.sum(mask_green) > 0:
        color = "Green"
        
    # Afficher la couleur dominante sur l'image
    cv2.putText(frame, f"Color: {color}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # Afficher la vidéo avec la ROI
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Redimensionner l'image pour l'affichage
    resized_frame = cv2.resize(frame, (resize_width, resize_height))

    out.write(resized_frame)

    # Afficher la vidéo redimensionnée
    cv2.imshow('Video', resized_frame)

    # Condition de sortie
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()