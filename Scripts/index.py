import Constellation
import time
from neopixel import *
exec(compile(source=open('ledlib.py').read(), filename='ledlib.py', mode='exec')) # N'est pas appelé avec un import à cause du global strip du OnStart

# Configuration des LED
LED_COUNT      = 256      # Nombre de LED
LED_PIN        = 21       # Pin de connection : mettre le pin 12 BCM 18) pour PWM
LED_FREQ_HZ    = 800000   # Frequence du signal en hertz (defaut : 800khz)
LED_DMA        = 5        # Chaine DMA pour generer le signal (defaut : 5)
LED_BRIGHTNESS = 15       # Luminosite de 0 a 255
LED_INVERT     = False    # True pour inverser le signal
LED_CHANNEL    = 0        # Mettre 1 pour les GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB # Type de matrice et ordre des couleurs (defaut : ws.WS2811_STRIP_GRB)

""" FONCTION : DisplayContent
    =========================
    Récupère un message callback Constellation et met à jour directement l'affichage LED à l'aide de la bibliothèque ledlib.py
    
    PARAMETRES
    ==========
    icon : nom de l'icone au format .jpg 8x8 à afficher à gauche de la matrice. L'image doit être placée dans le dossier ./img avec "Copy if Newer"
    text : texte à afficher à droite de l'icone
    Non encore implanté 
    time : à utiliser pour afficher l'affichage comme une notification push pendant le temps spécifié (en secondes) / Mettre None sinon
    matrix : matrice 8x32 avec des truples RGB pour un affichage 100% personnalisé. Prioritaire sur 'icon' et 'text'.
"""
@Constellation.MessageCallback()
def DisplayContent(data):
    "Permet d'afficher quelque chose sur la matrice LED (icon/text/time [option]/matrix [option])"
    
    displayMatrix(0, pngToMatrix(str(data.icon)))
    displayText(9, str(data.text) + "          ", font="SMALL", speed=0.1) # Les espaces sont utilisés pour vider tout le texte de la matrice, sinon superposition

def OnStart():
    global strip
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

    Constellation.WriteInfo("Démarrage du packet AffichageLED...")

Constellation.Start(OnStart)