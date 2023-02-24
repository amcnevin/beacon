from color import Color
import board
from digitalio import DigitalInOut, Direction

class BeaconRepository:

    pin_map = {}

    def __init__(self):
        # TODO build mapping of color -> pins
        self.pin_map[Color.BLUE] = [
            self.init_pin(board.GP0),
            self.init_pin(board.GP1),
            self.init_pin(board.GP2)]

        self.pin_map[Color.RED] = [
            self.init_pin(board.GP7),
            self.init_pin(board.GP8),
            self.init_pin(board.GP9)]

        self.pin_map[Color.GREEN] = [
            self.init_pin(board.GP13),
            self.init_pin(board.GP14),
            self.init_pin(board.GP15)]

        self.pin_map[Color.YELLOW] = [
            self.init_pin(board.GP17),
            self.init_pin(board.GP18),
            self.init_pin(board.GP19)]

        self.pin_map[Color.ORANGE] = [
            self.init_pin(board.GP20),
            self.init_pin(board.GP21),
            self.init_pin(board.GP22)]

        self.pin_map[Color.PURPLE] = [
            self.init_pin(board.GP28),
            self.init_pin(board.GP27),
            self.init_pin(board.GP26)]

    def init_pin(self, pin):
        dio = DigitalInOut(pin)
        dio.direction = Direction.OUTPUT
        return dio

    def toggle_color(self, color: Color):
        for pin in self.pin_map[color]:
            pin.value = not pin.value

    def clear(self):
        """
        Clear all GPIO pins
        """
        for pin_list in self.pin_map.values():
            for pin in pin_list:
                pin.value = False