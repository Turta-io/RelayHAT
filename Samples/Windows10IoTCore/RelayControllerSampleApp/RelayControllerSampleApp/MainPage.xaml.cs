using Windows.UI.Xaml.Controls;
using System.Threading;
using TurtaRelayHAT;

namespace RelayControllerSampleApp
{
    public sealed partial class MainPage : Page
    {
        // Relay Controller
        static RelayController relayController;

        // Relay Timer
        Timer relayTimer;

        // Counter
        static int counter = 0;

        public MainPage()
        {
            this.InitializeComponent();

            // Initialize controller and timer
            Initialize();
        }

        private void Initialize()
        {
            // Initialize Relay Controller
            relayController = new RelayController();

            // Configure timer to 2000ms delayed start and 1000ms interval
            relayTimer = new Timer(new TimerCallback(RelayTimerTick), null, 2000, 1000);
        }

        private static void RelayTimerTick(object state)
        {
            switch (counter)
            {
                case 0:
                    relayController.SetRelay(1, true); // Turn relay 1 on
                    break;

                case 1:
                    relayController.SetRelay(2, true); // Turn relay 2 on
                    break;

                case 2:
                    relayController.SetRelay(3, true); // Turn relay 3 on
                    break;

                case 3:
                    relayController.SetRelay(4, true); // Turn relay 4 on
                    break;

                case 4:
                    relayController.SetRelay(1, false); // Turn relay 1 off
                    break;

                case 5:
                    relayController.SetRelay(2, false); // Turn relay 2 off
                    break;

                case 6:
                    relayController.SetRelay(3, false); // Turn relay 3 off
                    break;

                case 7:
                    relayController.SetRelay(4, false); // Turn relay 4 off
                    break;

                default:
                    break;
            }

            // Increase the counter
            counter++;

            // Reset the counter if overflowed
            if (counter > 7) counter = 0;
        }
    }
}