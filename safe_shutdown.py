#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import RPi.GPIO as GPIO
import time
import os
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
logging.debug('Setting GPIO27 / PIN13 to INPUT PULLUP')
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP) # PIN13 / YEL / SW-COM

# Turn delay relay on
logging.debug('Setting GPIO22 / PIN15 to OUTPUT HIGH')
GPIO.setup(22, GPIO.OUT) # PIN15 / WHT / CH1
GPIO.output(22, GPIO.HIGH)

# # Our function on what to do when the button is pressed
def Shutdown(channel):
    logger.debug('Detected falling edge on GPIO27 / PIN13')
    logger.info('Safely shutting down the system')
    os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(27, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

# Now wait!
while 1:
    # print('PIN13/GPIO27: {}'.format(GPIO.input(27)))
    # if not GPIO.input(27):
    #
    #     print('Safely shutdown')

    time.sleep(0.1)
