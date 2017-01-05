# Athena Voice Bot
A "home-brewed" assistant with natural language processing, smartHome integration and talk-back functionality. There are some things that Amazon Echo and Google Home wont let me do so I decided to build my own system.

As a note: this project is very much still in progress. I will try to update the readme as I go but just in this case, my priority is to have everything roughly implemented and will only roughly document. Once everything is ready to deploy, I will be releasing full documentation. Until then, I will only have small notes on the readme as well as my own notes on the side.

*Based on a past personal [project: Athena 1.0](https://github.com/Jspsun/AthenaVoiceAssistant)*   
This overhaul of the bot uses far better contextual and natural langauge processing.


## Update:
I'm working on my latest commit for conversational interaction using NLP and salience values. Need to iron out a few bugs so I don't commit broken code first!

## Dependancies
- https://github.com/Uberi/speech_recognition
- pyAudio
- wemo api (ouimeaux)
- PocketSphinx(use $ brew install cmu-pocketsphinx)
- Google Clouds (speech to text)
- Houndify API

## Things I did externally
- Changed the speech_recognition library to include: recognizer_instance.pause_threshold = 0.1
- Changed my speech output voice in my mac system preferences
