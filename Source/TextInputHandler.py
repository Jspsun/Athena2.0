from WEMOListener import WEMOListener

lights = ["lights", "light"]
LightSwitch = WEMOListener()


class TextInputHandler(object):

    def __init__(self):
        return

        # determines which command to be run
    def getCommand(self, text):
        inputArray = text.split()

        # Check if the command is to open lights
        for trigger in lights:
            if trigger in inputArray:
                return "lights"
        return None

    # runs commands
    def runCommand(self, command):
        if command == "lights":
            LightSwitch.toggle()

    def process(self, text):
        self.runCommand(self.getCommand(text))
