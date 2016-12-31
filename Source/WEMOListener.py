from ouimeaux.environment import Environment


class WEMOListener(object):

    def __init__(self):
        # Creates a server
        self.env = Environment()
        self.env.start()
        # may need to increase for slower networks
        self.env.discover(seconds=2)

    def toggle(self):
        switch = self.env.get_switch('Athena toggle')
        if switch.get_state():
            switch.off()
        else:
            switch.on()
        return
