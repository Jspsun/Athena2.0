
from VoiceInputHandler import VoiceInputHandler
from TextInputHandler import TextInputHandler


def main():

    VoiceInput = VoiceInputHandler()
    CommandHandler = TextInputHandler()

    while True:
        text = VoiceInput.getInput()
        print "Text:", text
        CommandHandler.process(text)

if __name__ == '__main__':
    main()
