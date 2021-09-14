#!/usr/bin/env python3
# Halloween Jack o lantern Magic Fire RGB LED display
# Supposed to look like a realistic flame inside a jack o lantern with occasional shifts to green and purple magic
# Intended for Waveshare RGB LED hat on raspberry-pi zero
# Simon Ward 2021
# Adapted from NeoPixel StrandTest port from https://github.com/rpi-ws281x/rpi-ws281x-python

import argparse, random, time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 32  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 1        # GPIO pin connected to the pixels (1 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 1  # DMA channel to use for generating signal (try 1)
LED_BRIGHTNESS = 60  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

DEF_WAIT = 3

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe a color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 100.0)


def colorPattern(strip, colors, wait_ms=50):
    """Set a color randomly chosen from a list of colors across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, random.choice(colors))
        strip.show()
        time.sleep(wait_ms / 100.0)


# Main program logic follows:
if __name__ == "__main__":
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--clear", action="store_true", help="clear the display on exit"
    )
    args = parser.parse_args()

    # Color palette
    colorFireSet1 = [
        Color(255, 0, 0),
        Color(255, 90, 0),
        Color(255, 154, 0),
        Color(255, 206, 0),
        Color(255, 232, 8),
    ]

    colorFireSet2 = [
        Color(168, 6, 6),
        Color(187, 0, 9),
        Color(203, 12, 9),
        Color(216, 41, 28),
        Color(235, 58, 30),
    ]

    colorPurpleSet1 = [
        Color(188, 111, 241),
        Color(21, 0, 80),
        Color(63, 0, 113),
        Color(97, 0, 148),
    ]
    colorPurpleSet2 = [
        Color(23, 0, 85),
        Color(62, 0, 255),
        Color(174, 0, 251),
        Color(181, 255, 217),
    ]
    colorPurpleSet3 = [
        Color(71, 4, 108),
        Color(115, 30, 157),
        Color(160, 65, 197),
        Color(205, 109, 243),
    ]
    colorGreenSet1 = [
        Color(57, 255, 20),
        Color(1, 186, 181),
        Color(50, 205, 50),
        Color(57, 255, 20),
    ]
    colorGreenPurple1 = [
        Color(57, 255, 20),
        Color(1, 186, 181),
        Color(50, 205, 50),
        Color(57, 255, 20),
        Color(71, 4, 108),
        Color(115, 30, 157),
        Color(160, 65, 197),
        Color(205, 109, 243),
    ]

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL,
    )
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print("Press Ctrl-C to quit.")
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    # Build the performance script (Add functions and params as tuples to list)
    scriptFinal = []
    scriptMainFlame = []
    scriptTranFlameGreen = []
    scriptTranFlamePurple = []
    scriptTranGreenPurple = []
    scriptGreen = []
    scriptPurple = []

    for i in range(random.randint(30, 50)):
        scriptMainFlame.append((colorPattern, strip, colorFireSet1, DEF_WAIT))
    for i in range(10):
        scriptMainFlame.append((colorPattern, strip, colorFireSet2, DEF_WAIT))
    random.shuffle(scriptMainFlame)
    scriptFinal.extend(scriptMainFlame)

    for i in range(20):
        scriptPurple.append((colorPattern, strip, colorPurpleSet1, DEF_WAIT))
        scriptPurple.append((colorPattern, strip, colorPurpleSet3, DEF_WAIT))
    for i in range(10):
        scriptPurple.append((colorPattern, strip, colorPurpleSet2, DEF_WAIT))
    random.shuffle(scriptPurple)
    scriptFinal.extend(scriptPurple)

    for i in range(20):
        scriptTranGreenPurple.append((colorPattern, strip, colorGreenPurple1, DEF_WAIT))
    random.shuffle(scriptTranGreenPurple)
    scriptFinal.extend(scriptTranGreenPurple)

    for i in range(20):
        scriptGreen.append((colorPattern, strip, colorGreenSet1, DEF_WAIT))
    random.shuffle(scriptGreen)
    scriptFinal.extend(scriptGreen)

    # Run the performance
    try:
        while True:
            for e in scriptFinal:
                e[0](*e[1:])

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 1)
