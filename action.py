from color import Color


class ActionFactory:
    @staticmethod
    def build(input: dict) -> BeaconAction :
        action = input.get("action", None)
        try:
            color = getattr(Color, input.get("color", "WHITE"))
        except AttributeError as ae:
            raise ValueError("Color not recognized")

        args = input.get("args", {})

        if action == "pulse":
            return PulseAction(color, args)
        elif action == "persist":
            return PersistAction(color, args)
        elif action == "clear":
            return ClearAction()
        elif action == "enable":
            return EnableAction()
        elif action == "disable":
            return DisableAction()
        else:
            raise ValueError("Action not recognized")

class BeaconAction:
    def __init__(self, color: Color, args: dict):
        self.color = color
        self.args = args


class PulseAction(BeaconAction):
    def __init__(self, color: Color, args: dict):
        super().__init__(color, args)


class PersistAction(BeaconAction):
    def __init__(self, color: Color, args: dict):
        super().__init__(color, args)


class ClearAction(BeaconAction):
    def __init__(self):
        super().__init__(None, {})


class EnableAction(BeaconAction):
    def __init__(self):
        super().__init__(None, {})


class DisableAction(BeaconAction):
    def __init__(self):
        super().__init__(None, {})
