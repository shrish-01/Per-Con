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

if (feeling== "sad"):
    speak("Sadness is very difficult emotion to deal with. It makes you us loss trust in ourself an in those around us. ")
    speak("Sometimes, sadness can get overwhelming and make us feel like We are trapped alone all alone in darkness. ")
    speak("I am here for you. Let me suggest a few things that might help you right now. ")
    print("Show me/may be later")
    command=input()
    speak2(command)
    if (command=="show me"):
        speak("Great!!take look on this.")       
        speak("Do mindful walking")
        speak("Do positive selftalk")
        speak("Listen some upbeat music to motivate")
        speak("do meditation")
        speak("don't ignore it ok? trust me it will help a lot, just try once "+name)

if (feeling== "Worried"):
    speak("I'm sorry you are feeling worried. I appreciate you telling me this about yourself.  ")
    speak("Life can be overwhelming and out of control sometime.  ")
    speak("I am here for you. And I happen to know also activities that can help you worry a little less would you like to try them out? ")
    print("Show me/may be later")
    command=input()
    speak2(command)
    if (command=="show me"):
        speak("Great!!take look on this.")
        speak("Do mindful walking")
        speak("Say some statements out loud to feel calmer")
        speak("use your imagination to takle your worry.")
        speak("do meditation")
        speak("don't ignore it ok? trust me it will help a lot, just try once "+name)

if (feeling== "Angry"):
    speak("Thanks for sharing this with me. I am sure it was not easy to acknowledge your anger.  ")
    speak("Anger can be corrosive and bitter. It can harm your relationship with others and yourself! ")
    speak("Anger can also be very difficult to manage at times. After all nobody likes to lose their cool. ")
    speak("Don't worry, I'm here for you. Let me suggest a few things that can cool you off ")
    print("Show me/may be later")
    command=input()
    speak2(command)
    if (command=="show me"):
        speak("Great!!take look on this.")
        speak("Counting backwards")
        speak("Thinking aloud")
        speak("Scribble down all anger on paper")
        speak("Do meditation,simple exercises")
        speak("don't ignore it ok? trust me it will help a lot, just try once "+name)

if (feeling== "Stressed"):
    speak("I am sorry to hear you're stressed!")
    speak("Life is full of challenges and stressors,and sometimes,it all gets a little too much.")
    speak("Stress can make us feel nervous ,unfocussed,forgetful and easily frustrated.")
    speak("Don't worry, I'm here for you. Let me suggest a few things that can help you")
    print("Show me/may be later")
    command=input()
    speak2(command)
    if (command=="show me"):
        speak("Great!!take look on this.")
        speak("Breath deeply")
        speak("Beat stree by paying attention to your body.")
        speak("Scribble down all anger on paper")
        speak("Do meditation,simple exercises")
        speak("don't ignore it ok? trust me it will help a lot, just try once "+name)




else:
    speak("Sorry,try by entering some other this feature not done yet") 






 
