# Turta Relay HAT Library for Raspbian
# Distributed under the terms of the MIT license.

# Python Driver for Relays
# Version 1.02
# Updated: February 16th, 2018

# Visit https://docs.turta.io for ducumentation.

import RPi.GPIO as GPIO

class RelayHAT:
    """Relay HAT"""

    #Variables
    is_initialized = False

    #Pins
    relay1, relay2, relay3, relay4 = 21, 22, 23, 24

    #Initialize
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay1, GPIO.OUT)
        GPIO.setup(self.relay2, GPIO.OUT)
        GPIO.setup(self.relay3, GPIO.OUT)
        GPIO.setup(self.relay4, GPIO.OUT)
        GPIO.output(self.relay1, GPIO.LOW)
        GPIO.output(self.relay2, GPIO.LOW)
        GPIO.output(self.relay3, GPIO.LOW)
        GPIO.output(self.relay4, GPIO.LOW)
        self.is_initialized = True
        return

    #Relay Control
    def set_relay(self, ch, st):
        """Controls the relay.
        :param ch: Relay channel. 1 to 4.
        :param st: Relay state. True or False."""

        if (ch == 1):
            GPIO.output(self.relay1, GPIO.HIGH if st else GPIO.LOW)
        elif (ch == 2):
            GPIO.output(self.relay2, GPIO.HIGH if st else GPIO.LOW)
        elif (ch == 3):
            GPIO.output(self.relay3, GPIO.HIGH if st else GPIO.LOW)
        elif (ch == 4):
            GPIO.output(self.relay4, GPIO.HIGH if st else GPIO.LOW)
        return

    #Relay Readout
    def read_relay_state(self, ch):
        """Reads the relay state.
        :param ch: Relay channel. 1 to 4."""
        if (ch == 1):
            return GPIO.input(self.relay1)
        elif (ch == 2):
            return GPIO.input(self.relay2)
        elif (ch == 3):
            return GPIO.input(self.relay3)
        elif (ch == 4):
            return GPIO.input(self.relay4)

    #Disposal
    def __del__(self):
        """Releases the resources."""
        if self.is_initialized:
            GPIO.output(self.relay1, GPIO.LOW)
            GPIO.output(self.relay2, GPIO.LOW)
            GPIO.output(self.relay3, GPIO.LOW)
            GPIO.output(self.relay4, GPIO.LOW)
            GPIO.cleanup()
            del self.is_initialized
        return
