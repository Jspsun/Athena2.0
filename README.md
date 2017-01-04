#Athena Voice Bot
A "home-brewed" assistant with natural language processing, smartHome integration and talk-back functionality. There are some things that Amazon Echo and Google Home wont let me do so I decided to build my own system.

As a note: this project is very much still in progress. I will try to update the readme as I go but just in this case, my priority is to have everything roughly implemented and will only roughly document. Once everything is ready to deploy, I will be releasing full documentation. Until then, I will only have small notes on the readme as well as my own notes on the side.

##TODO
###General
- [x] Voice Recognition
  - [x] Set up Google Speech to text API (and Keys)
  - [ ] Build in RPC bidirectional Streaming

- [x] Talk-back Functionality
  - [ ] Improve quality of talk-back

###Modules
  - [x] LightSwitch Control
  - [ ] WealthSimple Display
  - [ ] Clock
  - [ ] Weather

###Further IOT Functionality
- [ ] build to recieve requests and send communications to clients (ie, asking bot to play a spotify playlist, starts the music on home computer)
- [ ] build communication via an app (Send commands to central bot via smartphone)

##Dependancies
- https://github.com/Uberi/speech_recognition
- pyAudio
- wemo api (ouimeaux)
- PocketSphinx(use $ brew install cmu-pocketsphinx)
- Google Clouds (speech to text)
- Houndify API

##Things I did externally
- Changed the speech_recognition library to include: recognizer_instance.pause_threshold = 0.1
- Changed my speech output voice in my mac system preferences
