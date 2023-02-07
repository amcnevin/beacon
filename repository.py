from color import Color
import board
from digitalio import DigitalInOut, Direction
from time import sleep

class BeaconRepository:

    pin_map = {}

    def __init__(self):
        # TODO build mapping of color -> pins
        self.pin_map[Color.BLUE] = [
            self.init_pin(board.GP0),
            self.init_pin(board.GP1),
            self.init_pin(board.GP2)]

    def init_pin(self, pin):
        dio = DigitalInOut(pin)
        dio.direction = Direction.OUTPUT
        return dio

    def persist(self, color: Color):
        """
        Persist High on all pins mapped to color
        """

        # TODO add GPIO logic
        print(f"LOG: Persisting {color}")

    def pulse(self, color: Color, duration: int):
        """
        Pulse High on all pins mapped to color
        """
        for pin in self.pin_map[color]:
            pin.value = True
        sleep(duration)
        for pin in self.pin_map[color]:
            pin.value = False

        # TODO add GPIO logic
        print(f"LOG: Pulse {color} for {duration} ms")

    def clear(self):
        """
        Clear all GPIO pins
        """
        # TODO iterate over all values in pin map
        print("LOG: CLEAR")