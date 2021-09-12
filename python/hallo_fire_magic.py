#!/usr/bin/env python3
# Simon Ward 2021
# Halloween Jack o lantern Magic Fire RGB LED display
# Intented for Waveshare RGB LED hat on raspberry-pi zero
# Adapted from NeoPixel StrandTest port from https://github.com/rpi-ws281x/rpi-ws281x-python

import random, time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 32        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def colorPattern(strip, colors, wait_ms=50):
    """Set color from a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, random.choice(colors))
        strip.show()
        time.sleep(wait_ms / 1000.0)


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Color palette
    colorFireSet1 = [Color(255,0,0), Color(255,90,0), Color(255,154,0), Color(255,206,0), Color(255,232,8)]
    colorFireSet2 = [Color(190, 16, 19), Color(210, 48, 8), Color(228, 83, 35), Color(238, 119, 28), Color(246, 150, 14), Color(255, 205, 6)]
    colorFireSet3 = [Color(168, 6, 6), Color(187, 0, 9), Color(203, 12, 9), Color(216, 41, 28), Color(235, 58, 30)]
    colorFireSet4 = [Color(191, 2, 4), Color(235, 3, 6), Color(254, 149, 0), Color(247, 173, 17), Color(244, 232, 0), Color(217, 45, 2)]

    colorPurpleSet1 = [Color(188, 111, 241), Color(21, 0, 80), Color(63, 0, 113), Color(97, 0, 148)]
    colorPurpleSet2 = [Color(23, 0, 85), Color(62, 0, 255), Color(174, 0, 251), Color(181, 255, 217)]
    colorGreenSet1 = [Color(57, 255, 20), Color(10, 186, 181), Color(50, 205, 50), Color(57, 255, 20)]

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet3, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorPurpleSet2, 60)
            colorPattern(strip, colorFireSet1, 60)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet2, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorPurpleSet2, 60)
            colorPattern(strip, colorFireSet1, 60)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorPurpleSet2, 100)
            colorPattern(strip, colorFireSet1, 100)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet2, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 25)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorPurpleSet1, 100)
            colorPattern(strip, colorGreenSet1, 100)
            colorPattern(strip, colorPurpleSet2, 100)
            colorPattern(strip, colorGreenSet1, 100)
            colorPattern(strip, colorFireSet1, 100)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet1, 10)
            colorPattern(strip, colorFireSet4, 25)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
