import config
import speech_recognition as sr


class VoiceInputHandler(object):

    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            # listen for 1 second to calibrate the energy threshold for ambient
            # noise levels
            self.r.adjust_for_ambient_noise(source)

    def getVoice(self):
        with sr.Microphone() as source:
            # TODO remove
            print("Say something: ")
            audio = self.r.listen(source)
        return audio

    def getText(self, audio):
        # Toggles use of speech to text api
        # 1 for houd, 2 for google and 3 for sphinx
        api = 3
        text = ""

        if api == 1:
            try:
                text = self.r.recognize_houndify(
                    audio,  client_id=config.HOUNDIFY_CLIENT_ID, client_key=config.HOUNDIFY_CLIENT_KEY)
            except sr.UnknownValueError:
                print("Houndify could not understand audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Houndify service; {0}".format(e))

        elif api == 2:
            try:
                text = self.r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Engine could not process the speech")
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(e))

        else:
            try:
                text = self.r.recognize_sphinx(audio)
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

        return text

    def getInput(self):
        return self.getText(self.getVoice())
