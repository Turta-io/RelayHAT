# Turta Relay HAT Helper for Raspbian
# Distributed under the terms of the MIT license.

import RPi.GPIO as GPIO

#Pins
relay1, relay2, relay3, relay4 = 21, 22, 23, 24

#Initialize
def Init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.setup(relay2, GPIO.OUT)
    GPIO.setup(relay3, GPIO.OUT)
    GPIO.setup(relay4, GPIO.OUT)
    GPIO.output(relay1, GPIO.LOW)
    GPIO.output(relay2, GPIO.LOW)
    GPIO.output(relay3, GPIO.LOW)
    GPIO.output(relay4, GPIO.LOW)
    return

#Relay Control
def SetRelay(ch, st):
    if (ch == 1):
        GPIO.output(relay1, GPIO.HIGH if st else GPIO.LOW)
    elif (ch == 2):
        GPIO.output(relay2, GPIO.HIGH if st else GPIO.LOW)
    elif (ch == 3):
        GPIO.output(relay3, GPIO.HIGH if st else GPIO.LOW)
    elif (ch == 4):
        GPIO.output(relay4, GPIO.HIGH if st else GPIO.LOW)
    return

#Relay Readout
def ReadRelayState(ch):
    if (ch == 1):
        return GPIO.input(relay1)
    elif (ch == 2):
        return GPIO.input(relay2)
    elif (ch == 3):
        return GPIO.input(relay3)
    elif (ch == 4):
        return GPIO.input(relay4)

#Release The Resources
def Dispose():
    GPIO.cleanup()
    return
