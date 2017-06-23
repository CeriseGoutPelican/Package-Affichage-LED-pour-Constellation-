import time
import numpy as np
from PIL import ImageFont, ImageDraw, Image

from neopixel import *

""" VARIABLES GLOABLES DE CONFIGURATION
    ===================================
"""

# Configuration des LED
LED_COUNT      = 256      # Nombre de LED
LED_PIN        = 10       # Pin de connection : mettre le GPIO 10 pour SPI (/dev/spidev0.0)
LED_FREQ_HZ    = 800000   # Frequence du signal en hertz (defaut : 800khz)
LED_DMA        = 5        # Chaine DMA pour generer le signal (defaut : 5)
LED_BRIGHTNESS = 20       # Luminosite de 0 a 255
LED_INVERT     = False    # True pour inverser le signal
LED_CHANNEL    = 0        # Mettre 1 pour les GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Type de matrice et ordre des couleurs (defaut : ws.WS2811_STRIP_GRB)

""" LISTES DES FONTIONS UTILES AU PROGRAMME 
    =======================================
"""

def displayMatrix(start, matrix):
		
	offset = 8*start
		
	for i in range(0, len(matrix)):
		if matrix[i] > 0 and matrix[i] <= 255:
			matrix[i] = Color(200,200,200)
								
		strip.setPixelColor(i + offset, matrix[i])
			
def twitterLogo():
	
	logo = np.array([[Color( 87,172,238),Color(  0,  0,  0),Color(  0,  0,  0),Color(  0,  0,  0),Color(  0,  0,  0),Color( 87,172,238),Color(  0,  0,  0),Color(  0,  0,  0)],
	                 [Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0),Color(  0,  0,  0),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0)],
	                 [Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238)],
         	         [Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0)],
	                 [Color(  0,  0,  0),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0)],
	                 [Color(  0,  0,  0),Color(  0,  0,  0),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0),Color(  0,  0,  0)],
	                 [Color(  0,  0,  0),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0),Color(  0,  0,  0),Color(  0,  0,  0)],
	                 [Color( 87,172,238),Color( 87,172,238),Color( 87,172,238),Color(  0,  0,  0),Color(  0,  0,  0),Color(  0,  0,  0),Color(  0,  0,  0),Color(  0,  0,  0)]])
						
	return matrixToLine(logo)
	
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
	
def textToMatrix(text):
	image = Image.new("L", (22, 8), "black")
	draw = ImageDraw.Draw(image)
	tiny_font = ImageFont.truetype("fonts/TINY_FONT.ttf", 5)
	draw.text((0, 1), text, fill="white", font=tiny_font)
				
	return np.array(image)

""" PROGRAMME PRINCIPAL
    ===================
"""

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	
	displayMatrix(0, twitterLogo())
	displayMatrix(10, matrixToLine(textToMatrix("Cerise")))
	
	strip.show()
