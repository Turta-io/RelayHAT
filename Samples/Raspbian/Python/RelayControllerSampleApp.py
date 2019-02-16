import time
from turta_relayhat import Turta_RelayHAT
#Install Relay HAT library with "pip install turta-relayhat"

#Initialize
rc = Turta_RelayHAT.RelayHAT()

try:
    while 1:
        #Toggle relay 1
        rc.set_relay(1, not rc.read_relay_state(1))
        print("Relay 1 state: " + ("On" if rc.read_relay_state(1) else "Off"))
        time.sleep(2.0)

        #Toggle relay 2
        rc.set_relay(2, not rc.read_relay_state(2))
        print("Relay 2 state: " + ("On" if rc.read_relay_state(2) else "Off"))
        time.sleep(2.0)

        #Toggle relay 3
        rc.set_relay(3, not rc.read_relay_state(3))
        print("Relay 3 state: " + ("On" if rc.read_relay_state(3) else "Off"))
        time.sleep(2.0)

        #Toggle relay 4
        rc.set_relay(4, not rc.read_relay_state(4))
        print("Relay 4 state: " + ("On" if rc.read_relay_state(4) else "Off"))
        time.sleep(2.0)

except KeyboardInterrupt:
    print('Bye.')