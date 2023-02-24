from color import Color
from repository import BeaconRepository
from time import sleep
from morse_code import Morse


def get_color(args: dict) -> Color :
    """
    map the color from arguments
    raise a ValueError if we cannot map
    """
    try:
        return getattr(Color, args["color"])
    except AttributeError as ae:
        raise ValueError("color not recognized")


def get_colors(args: dict) -> list:
    try:
        return getattr(list, args["colors"])
    except AttributeError as ae:
        raise ValueError("colors not recognized")


class BeaconService:

    def __init__(self, repository: BeaconRepository):
        self.persisted = False
        self.enabled = True
        self.repository = repository

    def process_action(self, action: dict):
        """
        map the input action args to the appropriate function
        """
        action_type = action.get("action")

        if action_type == "pulse":
            self.pulse(action)
        elif action_type == "persist":
            self.persist(action)
        elif action_type == "cycle":
            self.cycle(action)
        elif action_type == "morse":
            self.morse(action)
        elif action_type == "clear":
            self.clear()
        elif action_type == "enable":
            self.enable()
        elif action_type == "disable":
            self.disable()
        else:
            ValueError("action not recognized")

    def pulse(self, args: dict):
        """
        pulse the beacon with the provided args
        """
        if self.can_action():
            color = get_color(args)
            pulses = int(args.get("pulses", 1))
            duration = int(args.get("duration", 1))
            for i in range(pulses):
                self.repository.toggle_color(color)
                sleep(duration)
                self.repository.toggle_color(color)
                sleep(duration)

    def persist(self, args: dict):
        """
        persist the beacon with the provided args
        """
        if self.can_action():
            color = get_color(args)
            self.repository.clear()
            self.repository.toggle_color(color)
            self.persisted = True

    def cycle(self, args: dict):
        """
        cycle through a list of colors
        """
        if self.can_action():
            colors = args.get("colors", [])
            duration = int(args.get("duration", 1))
            print("CYCLE")
            print(colors)
            for color in colors:
                color = getattr(Color, color)
                self.repository.toggle_color(color)
                sleep(duration)
                self.repository.toggle_color(color)

    def morse(self, args: dict):
        if self.can_action():
            color = get_color(args)
            phrase = args.get("phrase", "LOL")
            morse = Morse(self.repository)
            morse.morse_code(color, phrase)

    def clear(self):
        """
        Clear the beacon
        """
        if self.is_enabled():
            self.persisted = False
            self.repository.clear()


    def enable(self):
        """
        Enable the beacon
        """
        self.enabled = True
        self.persisted = False

    def disable(self):
        """
        Disable the beacon
        """
        self.clear()
        self.enabled = False

    def can_action(self) -> bool:
        """
        determine if were in an actionable state
        """
        return (self.enabled and not self.persisted)

    def is_enabled(self) -> bool:
        """
        is the beacon enabled?!?
        """
        return self.enabled

