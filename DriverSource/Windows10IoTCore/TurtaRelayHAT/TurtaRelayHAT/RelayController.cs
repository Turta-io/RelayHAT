/* Turta® Relay HAT Helper for Windows® 10 IoT Core
 * Copyright © 2017 Turta
 * Distributed under the terms of the MIT license.
 */

using System;
using Windows.Devices.Gpio;

namespace TurtaRelayHAT
{
    public class RelayController : IDisposable
    {
        #region Globals

        // GPIO Device
        private static GpioPin relay1, relay2, relay3, relay4;

        #endregion

        #region Constructor

        /// <summary>
        /// Initiates the relays to turn on / off devices up to DC24V / AC240V 5A each.
        /// </summary>
        public RelayController()
        {
            // Initiate the GPIO Controller.
            GpioController gpioController = GpioController.GetDefault();

            // Configure the pins.
            relay1 = gpioController.OpenPin(21);
            relay2 = gpioController.OpenPin(22);
            relay3 = gpioController.OpenPin(23);
            relay4 = gpioController.OpenPin(24);

            relay1.Write(GpioPinValue.Low);
            relay2.Write(GpioPinValue.Low);
            relay3.Write(GpioPinValue.Low);
            relay4.Write(GpioPinValue.Low);

            relay1.SetDriveMode(GpioPinDriveMode.Output);
            relay2.SetDriveMode(GpioPinDriveMode.Output);
            relay3.SetDriveMode(GpioPinDriveMode.Output);
            relay4.SetDriveMode(GpioPinDriveMode.Output);
        }

        #endregion

        #region Relay Control

        /// <summary>
        /// Controls the relay state.
        /// </summary>
        /// <param name="ch">Relay channel. 1 to 4.</param>
        /// <param name="state">Relay state. True for enable, false for disable.</param>
        public void SetRelay(int ch, bool state)
        {
            switch (ch)
            {
                case 1:
                    relay1.Write(state ? GpioPinValue.High : GpioPinValue.Low);
                    break;

                case 2:
                    relay2.Write(state ? GpioPinValue.High : GpioPinValue.Low);
                    break;

                case 3:
                    relay3.Write(state ? GpioPinValue.High : GpioPinValue.Low);
                    break;

                case 4:
                    relay4.Write(state ? GpioPinValue.High : GpioPinValue.Low);
                    break;

                default:
                    break;
            }
        }

        #endregion

        #region Disposal

        /// <summary>
        /// Disables the relays and then cleans up the resources.
        /// </summary>
        public void Dispose()
        {
            relay1.Write(GpioPinValue.Low);
            relay2.Write(GpioPinValue.Low);
            relay3.Write(GpioPinValue.Low);
            relay4.Write(GpioPinValue.Low);

            relay1.Dispose();
            relay2.Dispose();
            relay3.Dispose();
            relay4.Dispose();
        }

        #endregion
    }
}
