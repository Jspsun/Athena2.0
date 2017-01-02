from WEMOListener import WEMOListener

lightsOn = ["lights on", "light on", "on the lights", "on the light"]
lightsOff = ["lights off", "light off",
             "off the lights", "off the light"]
lightsToggle = ["lights", "light"]
LightSwitch = WEMOListener()


class TextInputHandler(object):

    def __init__(self):
        return

    # TODO BUILD HELPER METHOD TO IMPROVE READABILITY
    # determines which command to be run
    def getCommand(self, text):

        # Check if the command is to turn on lights
        for trigger in lightsOn:
            if trigger in text:
                return "lightsOn"
        # check to see if command is to turn off lights
        for trigger in lightsOff:
            if trigger in text:
                return "lightsOff"
        # check to see if command is to toggle lights
        for trigger in lightsToggle:
            if trigger in text:
                return "lightsToggle"
        return None

    # runs commands
    def runCommand(self, command):

        if command == "lightsOn":
            LightSwitch.lightsOn()
        elif command == "lightsOff":
            LightSwitch.lightsOff()
        elif command == "lightsToggle":
            LightSwitch.toggle()

    def process(self, text):
        self.runCommand(self.getCommand(text))
