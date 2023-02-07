# beacon
Beacon using Raspberry Pi Pico W and Adafruit's CircuitPython HTTP Server 


## Goal
I'd like to have some visual indicator of 'Events' that occur within my surroundings. Like the sump pump firing off or wifi cutting out.

This web server that routes actions to interact with the pico's GPIO pins. The intent is to have node-red or some other flow tool interact with this API

This will be paired with a 3d printed crystal that I'm butchering with a Dremel tool for now...
https://www.thingiverse.com/thing:61172

### install

```
circup install adafruit-circuitpython-httppserver
```

### Examples:
pulse the beacon 10 times with a second delay with the Green LEDs
```
curl -XPOST http://localhost/beacon -d '{ "action": "pulse", "color": "BLUE", "pulses" : 10, "duration": 1000 }'
 ```
 
persist the beacon with the RED LEDs to indicate outage
```
curl -XPOST http://localhost/beacon -d '{ "action": "persist", "color": "RED" }'
```

clear the beacon
```
curl -XPOST http://localhost/beacon -d '{ "action": "clear" }'
```

disable the beacon
```
curl -XPOST http://localhost/beacon -d '{ "action": "disable" }'
```

enable the beacon
```
curl -XPOST http://localhost/beacon -d '{ "action": "enable" }'
```
