from machine import Pin
import neopixel
import time

# Configuración del pin y cantidad de LEDs
PIN = 8  # Pin donde está conectado el WS2812B
NUMPIXELS = 1  # Número de LEDs (ajusta si tienes más de uno)

# Inicializa el objeto NeoPixel
np = neopixel.NeoPixel(Pin(PIN), NUMPIXELS)

def show_color(r, g, b):
    np[0] = (r, g, b)
    np.write()

while True:
    # Cambiar colores en el espectro RGB
    for i in range(255):
        show_color(i, 255 - i, 0)  # Cambia gradualmente de rojo a verde
        time.sleep_ms(5)

    for i in range(255):
        show_color(255 - i, 0, i)  # Cambia de verde a azul
        time.sleep_ms(5)

    for i in range(255):
        show_color(0, i, 255 - i)  # Cambia de azul a rojo
        time.sleep_ms(5)
