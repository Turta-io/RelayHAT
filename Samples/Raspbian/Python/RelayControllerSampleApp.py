import time
import RelayController

#Initialize
RelayController.Init()

try:
    while 1:
        #Toggle relay 1
        RelayController.SetRelay(1, not RelayController.ReadRelayState(1))
        time.sleep(5.0)

        #Toggle relay 2
        RelayController.SetRelay(2, not RelayController.ReadRelayState(2))
        time.sleep(5.0)

        #Toggle relay 3
        RelayController.SetRelay(3, not RelayController.ReadRelayState(3))
        time.sleep(5.0)

        #Turn relay 4 on
        RelayController.SetRelay(4, True)
        time.sleep(5.0)

        #Turn relay 4 off
        RelayController.SetRelay(4, False)
        time.sleep(5.0)

except KeyboardInterrupt:
    RelayController.Dispose()
