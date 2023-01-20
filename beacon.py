from color import Color
from action import BeaconAction, PulseAction, PersistAction, ClearAction, EnableAction, DisableAction


class Beacon:

    def __init__(self):
        print("Beacon initialized")
        self.enabled = True

    def process_action(self, action: BeaconAction):
        """
        process the BeaconAction by routing the class type to the appropriate method
        TODO: look into alternatives for overloading or multipledispatch for circuitpython
        """
        type_val = type(action)

        if type_val == PulseAction:
            self.pulse(action)
        elif type_val == PersistAction:
            self.persist(action)
        elif type_val == ClearAction:
            self.clear(action)
        elif type_val == EnableAction:
            self.enable(action)
        elif type_val == DisableAction:
            self.disable(action)
        else:
            ValueError("Action not recognized")


    def pulse(self, pulse_action: PulseAction):
        """
        Pulse the LEDs with the provided color and number of pulses
        """
        if self.enabled:
            print("Pulse Action")

    def persist(self, persist_action: PersistAction):
        """
        Turn on the LEDs with the provided color and leave them on
        """
        if self.enabled:
            print("Persist Action")

    def clear(self, clear_action: ClearAction):
        """
        Clear any state of the LEDs
        """
        if self.enabled:
            print("Clear Action")

    def enable(self, enable_action: EnableAction):
        """
        Enable the Beacon and respond to other Actions
        """
        self.enabled = True
        print("Enable Action")

    def disable(self, disable_action: DisableAction):
        """
        Disable the Beacon and ignore any other Actions
        """
        self.enabled = False
        print("Disable Action")