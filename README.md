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

### Actions
| Action  | Desc                      | Args                    | 
|---------|---------------------------|-------------------------|
| pulse   | blinks a color            | color, pulses, duration |
| persist | enables a color           | color                   |
| cycle   | rotates among colors      | colors, duration        |
| morse   | emits color in morse code | color, phrase           |
| clear   | flushes off all colors    |                         |
| enable  | enables the service       |                         |
| disable | disables the service      |                         |
