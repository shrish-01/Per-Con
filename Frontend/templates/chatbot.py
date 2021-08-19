from win32com.client import Dispatch
from win32com.client.makepy import main
import win32com.client as wincl

def speak(str):
    speaker_number = 1
    speak = wincl.Dispatch("SAPI.SpVoice")
    vcs = speak.GetVoices()
    SVSFlag = 11

    speak.Voice
    speak.SetVoice(vcs.Item(speaker_number))
    print(str)
    speak.Speak(str)

def speak2(str):
    speak= Dispatch("SAPI.SpVoice")
    print(str)
    speak.Speak(str)

speak("Hii I am Per-con your new friend!")
speak("what is your name???")
name=input()
speak("Nice to meet you "+name+ "!")
speak("how was your day? How are you feeling now?")
print("tired Sad Worried Angry Stressed")
feeling=(input()).lower()
speak2(feeling)
if (feeling== "tired"):
    speak("thank for beeing here even when you are low on energy")
    speak("life can be hectic.Everyone needs a break from time to time.")
    speak("But that is easier said than done,given all the things that one has to manage!")
    speak("I have some suggestions for you to help you feel energised and refreshed")
    print("Show me/may be later")
    command=input()
    speak2(command)
    if (command=="show me"):
        speak("Great!!take look on this.")
        speak("Do streching")
        speak("Listen some upbeat music to motivate")
        speak("Hydrate yourself")
        speak("try to move some steps" )
        speak("don't ignore it ok? trust me it will help a lot, just try once "+name)
else:
    speak("Sorry,try by entering tired now this feature not done yet") 






 
