from ouimeaux.environment import Environment
import VoiceOutput


class WEMOListener(object):

    def __init__(self):
        # Creates a server
        self.env = Environment()
        self.env.start()
        # may need to increase for slower networks
        self.env.discover(seconds=2)

    def toggle(self):
        try:
            switch = self.env.get_switch('Athena toggle')
        except:
            VoiceOutput.Say("Sorry I can't seem to contact your WEMO switch.")
            return
        if switch.get_state():
            self.lightsOff()
        else:
            self.lightsOn()
        return

    def lightsOn(self):
        try:
            switch = self.env.get_switch('Athena toggle')
        except:
            VoiceOutput.Say("Sorry I can't seem to contact your WEMO switch.")
            return
        if not switch.get_state():
            switch.on()
            VoiceOutput.Say("Lights turned on")
        else:
            VoiceOutput.Say("Lights are already on")

    def lightsOff(self):
        try:
            switch = self.env.get_switch('Athena toggle')
        except:
            VoiceOutput.Say("Sorry I can't seem to contact your WEMO switch.")
            return
        if switch.get_state():
            switch.off()
            VoiceOutput.Say("Lights turned off")
        else:
            VoiceOutput.Say("Lights are already off")
