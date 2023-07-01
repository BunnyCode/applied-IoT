# Issues

Getting to know how to work with the photoresistor.
It was not until finding a decent guide that I was able to understand how to use it.
Trying to find refference material for the photoresistor was a bit difficult.
..

Connecting the power the wrong way was a bit of a problem. And i feelt the smell of heated electronics. but the board was not damaged, cat warned me in time. (No seriusly, my cat warned me in time.)

Finding the correct pinout was a bit of an issue, but adafruit had a great guide on how to connect the sensor.
https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/pinouts
GND - power and logic ground
VIN - 3-5V DC (use the same power voltage as you would for I2C logic)
I2C SDA - there's a 10K pullup to VIN
I2C SCL - there's a 10K pullup to VIN

Photo resistor information

https://peppe8o.com/how-to-use-a-photoresistor-with-raspberry-pi-pico/

To get the Soil sensor working I had to install the adafruit_seesaw library. that was stripped from
circitpython. I had to install it manually. from here
https://github.com/mihai-dinculescu/micropython-adafruit-drivers/tree/master/seesaw

Some of the variales where from Python2 and had to be changed to Python3.
