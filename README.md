# rgb-led-displays
A collection of RGB LED display scripts for special effects

## Python

### hallo_fire_magic.py
Halloween jack o lantern flame effect with other colours

To use:
`sudo python ./hallo_fire_magic.py -c`

To start on boot:

Run crontab for your user (eg: pi):
`sudo crontab -e -u pi`

Add a line like the following:
`@reboot sudo python ./hallo_fire_magic.py -c`
