# beacon
Beacon using Raspberry Pi Pico W and Adafruit's CircuitPython HTTP Server 


## Goal
I'd like to have some visual indicator of 'Events' that occur within my surroundings. Like the sump pump firing off or wifi cutting out.

This web server that routes actions to interact with the pico's GPIO pins. The intent is to have node-red or some other flow tool interact with this API

This will be paired with a 3d printed crystal that I'm butchering with a Dremel tool for now...
https://www.thingiverse.com/thing:61172



### Examples:
pulse the beacon 10 times with a second delay with the Green LEDs
```
curl -XPOST http://localhost/beacon -d '{ "action": "pulse", "color": "BLUE", "args": { "pulses" : 10, "delay": 1000 } }'
 ```
 
persist the beacon with the RED LEDs to indicate outage
```
curl -XPOST http://localhost/beacon -d '{ "action": "persist", "color": "RED", "args": {} }'
```
