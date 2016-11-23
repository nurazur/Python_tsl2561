# Python_tsl2561
A Python library for the Raspberry Pi and the Light sensor TSL2561.
Measures Luminosity in Lux.
The TSL2561 also has a Interrupt pin that goes LOW when light is below
or above a user defined threshold. The rule for the lower
threshold is "if light is below or equal", so if it is totaly dark and 
the interrupt is armed, it would trigger immediately. 
