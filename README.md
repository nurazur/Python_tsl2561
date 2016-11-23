# Python_tsl2561
A Python library for the Raspberry Pi and the Light sensor TSL2561.
Measures Luminosity in Lux.

The TSL2561 also has a Interrupt pin that is pulled LOW by the TSL2561 when light is below
or above a user defined threshold. Be sure to add a 10kOhm pull-up resistor
on the interrupt pin. The rule for the lower threshold is "if light is 
below or equal", so if it is totaly dark and 
the interrupt is armed, it would trigger immediately. So its better never ever
totally dark if you wait for light to raise above the lower threshold.
