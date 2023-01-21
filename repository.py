from color import Color

class BeaconRepository:

    def __init__(self):
        # TODO build mapping of color -> pins
        pass


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
        # TODO add GPIO logic
        print(f"LOG: Pulse {color} for {duration} ms")


    def clear(self):
        """
        Clear all GPIO pins
        """
        print("LOG: CLEAR")
