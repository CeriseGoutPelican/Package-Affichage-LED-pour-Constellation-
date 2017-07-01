import Constellation
import time
import numpy as np
from PIL import ImageFont, ImageDraw, Image

from neopixel import *

""" LISTES DES FONTIONS UTILES AU PROGRAMME 
    =======================================

    Ces fonctions utilisent la bibliothèque Adafruit rpi_ws281x
    https://github.com/jgarff/rpi_ws281x

    La génération de police d'écriture utilise PILLOW
    https://github.com/python-pillow/Pillow
"""

""" FONCTION : displayMatrix
	========================
	Permet d'afficher une matrice en allumant les LED une a une
	
	PARAMETRES :
	============
	offset : numero de la colonne de depart
	matrix : matrice ligne 1D contenant les informations de toutes les LED a afficher une a une
"""
def displayMatrix(offset, matrix):
	
	if(offset % 2 != 0):
		matrix = oddColumn(matrix)

	offset = 8*offset

	for i in range(0, len(matrix)):
		if matrix[i] > 0 and matrix[i] <= 255:
			matrix[i] = Color(200,200,200)

		strip.setPixelColor(i + offset, matrix[i])
		
	strip.show()
		
""" FONCTION : scroll
    =================
    Permet de faire defiler une matrice trop grande pour etre affichee sur la matrice LED 

    /!\ Ne fonctionne pas correctement avec Constellation sur le Raspeberry Pi3, sans doute à cause
    de l'alimentation directement sur le pin 5V. Des modifications seront apportées plus tard.
    
    PARAMETRES:  
    ===========
    offset : numero de la colonne de depart 
    matrix : matrice ligne 1D contenant les informations de toutes les LED a afficher une a une
    speed  : temps d'actualisation entre chaque deplacement de lettre
"""
def scroll(offset, matrix, speed = 0.5):	
	
	odd = False
	while True:
		
		# Les colonnes impaires posent probleme, on inverse les colonnes
		if odd == True:
			matrixBuffer = oddColumn(matrix)
			odd = False
		else:
			matrixBuffer = matrix
			odd = True
		
		displayMatrix(offset, matrixBuffer)
					
		matrix += matrix[:8]
		del matrix[:8]

		time.sleep(speed)
	
""" FONCTION : matrixToLine
    =======================
    Permet de transformer une matrice 2D possedant les coordonnees (x,y) en une liste contenant toutes les donnees de LED adressables de 1 a 256  
    
    PARAMETRES:  
    ===========
    matrix : matrice ligne 2D possedant les coordonnees (x,y) d'un texte/image
"""
def matrixToLine(matrix):
	# Passage d'une matrice 2D a une ligne en trois etapes
	# 1. Transpotion
	matrix = matrix.transpose()
	# 2. Renverse les lignes impaires (anciennement colonnes)
	for i in range(0, len(matrix - 1)):
		if i % 2 != 0:
			matrix[i] = matrix[i][::-1]
	# 3. Passage ligne
	matrix = matrix.flatten()
		
	return matrix.tolist()
	
""" FONCTION : displayText
    ======================
    Permet de generer une matrice N/B de la taille du texte demmande a l'aide de PILLOW 
    
    PARAMETRES:  
    ===========
    offset : numero de la colonne de depart
    text   : texte a generer
    font   : nom de la police d'ecriture a mettre dans le dossier fonts/NAME_FONT.ttf
    icone  : (bool) s'il y a une icone 8x8 presente 
"""
def displayText(offset, text, font = "SMALL", icone = True, speed = 0.3):
	# Definition du texte et de sa taille :
	font = ImageFont.truetype("fonts/"+font+"_FONT.ttf", 7)
	wText, hText = font.getsize(text)
	# Creation d'une image de la taille du texte
	image = Image.new("L", (wText, 8), "black")
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), text, fill="white", font=font)
	# Retourne une matrice bitmap si le text est petit / sinon fait defiler le text
	maxLED = 2200 if icone else 3200	

	if wText < maxLED:
		return displayMatrix(offset, matrixToLine(np.array(image)))
	else:
		return scroll(offset, matrixToLine(np.array(image)), speed)

""" FONCTION : pngToMatrix
    ======================
    Permet de transformer une image au format png en une matrice 2D
	
	PARAMETRES :
	============
	icone : chemin de l'image png 8x8 a recuperer
"""
def pngToMatrix(icone):
	icone = Image.open("img/"+icone+".png")
	data = np.array(icone)

	matrix = np.zeros((data.shape[0],data.shape[1]), dtype=int)	
	for i,v in enumerate(data):
		for y, v2 in enumerate(v):
			matrix[i][y] = int(Color(v2[0], v2[1], v2[2]))

	return matrixToLine(matrix)
	
""" FONCTION : oddColumn
    ====================
    Retourne une matrice commencant sur une colonne impaire
    
    PARAMETRES :
    ============
    matrix : matrice d'entree 1D
"""
def oddColumn(matrix):
    matrix = np.reshape(matrix, (-1,8))
    for i in range(0, len(matrix - 1)):
        matrix[i] = matrix[i][::-1]
    matrix = matrix.flatten()
    matrix = matrix.tolist()

    return matrix

