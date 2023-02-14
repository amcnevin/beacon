from repository import BeaconRepository
from color import Color
from time import sleep

DOT = "."
DASH = "-"
WS = " "
SPEED = 0.3

def get_alphabet():
    """
    build the alphabet
    :return:
    """
    return {
        "A": [DOT, DASH],
        "B": [DASH, DOT, DOT],
        "C": [DASH, DOT, DASH, DOT],
        "D": [DASH, DOT, DOT],
        "E": [DOT],
        "F": [DOT, DOT, DASH, DOT],
        "G": [DASH, DASH, DOT],
        "H": [DOT, DOT, DOT, DOT],
        "I": [DOT, DOT],
        "J": [DOT, DASH, DASH, DASH],
        "K": [DASH, DOT, DASH],
        "L": [DOT, DASH, DOT, DOT],
        "M": [DASH, DASH],
        "N": [DASH, DOT],
        "O": [DASH, DASH, DASH],
        "P": [DOT, DASH, DASH, DOT],
        "Q": [DASH, DASH, DOT, DASH],
        "R": [DOT, DASH, DOT],
        "S": [DOT, DOT, DOT],
        "T": [DASH],
        "U": [DOT, DOT, DASH],
        "V": [DOT, DOT, DOT, DASH],
        "W": [DOT, DASH, DASH],
        "X": [DASH, DOT, DOT, DASH],
        "Y": [DASH, DOT, DASH, DASH],
        "Z": [DASH, DASH, DOT, DOT],
        "0": [DASH, DASH, DASH, DASH, DASH],
        "1": [DOT, DASH, DASH, DASH, DASH],
        "2": [DOT, DOT, DASH, DASH, DASH],
        "3": [DOT, DOT, DOT, DASH, DASH],
        "4": [DOT, DOT, DOT, DOT, DASH],
        "5": [DOT, DOT, DOT, DOT, DOT],
        "6": [DASH, DOT, DOT, DOT, DOT],
        "7": [DASH, DASH, DOT, DOT, DOT],
        "8": [DASH, DASH, DASH, DOT, DOT],
        "9": [DASH, DASH, DASH, DASH, DOT],
        "&": [DOT, DASH, DOT, DOT, DOT],
        "'": [DOT, DASH, DASH, DASH, DASH, DOT],
        "@": [DOT, DASH, DASH, DOT, DASH, DOT],
        ")": [DASH, DOT, DASH, DASH, DOT, DASH],
        "(": [DASH, DOT, DASH, DASH, DOT],
        ":": [DASH, DASH, DASH, DOT, DOT, DOT],
        ",": [DASH, DASH, DOT, DOT, DASH, DASH],
        "=": [DASH, DOT, DOT, DOT, DASH],
        "!": [DASH, DOT, DASH, DOT, DASH, DASH],
        ".": [DOT, DASH, DOT, DASH, DOT, DASH],
        "-": [DASH, DOT, DOT, DOT, DOT, DASH],
        "+": [DOT, DASH, DOT, DASH, DOT],
        "?": [DOT, DOT, DASH, DASH, DOT, DOT],
        "/": [DASH, DOT, DOT, DASH, DOT],
    }

class Morse:

    alpha = {}
    repository = None

    def __init__(self, repository: BeaconRepository):
        self.repository = repository
        self.alpha = get_alphabet()

    def convert_char(self, input_char: str, alpha: dict):
        return alpha.get(input_char.upper(), WS)

    def morse_code(self, color: Color, phrase: str):
        morse = []
        for char in phrase:
            morse.extend(self.convert_char(char, self.alpha))
        print(morse)

        for code in morse:
            if code == WS:
                self.emit_whitespace()
            elif code == DOT:
                self.emit_dot(color)
            elif code == DASH:
                self.emit_dash(color)
            self.repository.clear()
            sleep(3*SPEED)

    def emit_whitespace(self):
        self.repository.clear()
        sleep(7*SPEED)

    def emit_dot(self, color: Color):
        self.repository.toggle_color(color)
        sleep(SPEED)
        self.repository.toggle_color(color)
        sleep(SPEED)

    def emit_dash(self, color: Color):
        self.repository.toggle_color(color)
        sleep(4*SPEED)