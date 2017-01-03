from WEMOListener import WEMOListener

lightsOn = ["lights on", "light on", "on the lights", "on the light"]
lightsOff = ["lights off", "light off",
             "off the lights", "off the light"]
lightsToggle = ["lights", "light"]
LightSwitch = WEMOListener()


class TextInputHandler(object):

    def __init__(self):
        self.text = ""
        return

        # helper method to improve readability
    def commandIs(self, arrayToCheck):
        for trigger in arrayToCheck:
            if trigger in self.text:
                return True
        return False

    # determines which command to be run
    # TODO map keys to functions to improve future scalability
    def getCommand(self, text):
        self.text = text
        # Check if the command is to turn on lights
        if self.commandIs(lightsOn):
            return "lightsOn"
        # check to see if command is to turn off lights
        if self.commandIs(lightsOff):
            return "lightsOff"
        # check to see if command is to toggle lights
        if self.commandIs(lightsToggle):
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

    # function that gets and runs the apropriate function based on given text
    # input
    def process(self, text):
        self.runCommand(self.getCommand(text))
