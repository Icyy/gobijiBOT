import pyttsx3
import speech_recognition as sr
import webbrowser
from googlesearch import *

# print(voices)

# engine.say("I find Om the dopest, flyest, O.G.-pimp-hustler-gangster-player-hardcore-motherfucker living today. To be honest, I am totally and completely on his dick")

# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def order():
#     r = sr.Recognizer()
#     with sr.Microphone as source:
#         print("bolo please")
#         r.pause_threshold=1
#         sound = r.listen(source)
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(sound, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:    
#         print("Say that again please...")  
#         return "None"
#     return query


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("bolo..")
        r.pause_threshold = 1
        awaz = r.listen(source)

    try:
        print("sun liya maine.")
        stmt = r.recognize_google(awaz, language= 'en-IN')
        print("you said ->  {0}".format(stmt))    

    except Exception as e:
        print("please say that again")
        speak("dude i'm not that smart yet, please say that again but, a litter slower, hah that's what she said")
        return "bhai thik se bol le thoda"
    return stmt

if __name__ == "__main__":
    # while True:
    
        # inp1 = input("press 'R' to go again and 'Q' to stop")
        #if inp1 == 'r':
        while True:
            # speak("Om is the flyest")
            phrase = takecmd().lower()
            comp = ["what can you do", "what all things can you do", "why do i use you", "can you do something", "do something"]
            who = ["tell me something about the person who made you", "who is om", "who made you", "who made you bruh"]
            sear = ["search google for","search for", "google"]
            youtube = ["search youtube", "play", "youtube"]
            name = ["who are you", "what is your name", "I dont know who you are"]
            for p in who:
                if p == phrase:
                    speak("Citrus Monkey Butts created me, he is the dopest flyest, O-G.-pimp-hustler-gangster-player-hardcore-motherfucker, living today. To be honest, I am totally and completely on his dick")

            for k in comp:
                if k == phrase:
                    speak("currently I can't do shit, I'm under construction")
            for g in sear:
                if g in phrase:
                    sword  ="for"
                    # length = len(phrase.split())
                    # print(length)
                    searstmt = phrase.partition(sword)[2]
                    # print(searstmt)
                    cp = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                    for q in search(searstmt, tld="co.in", num = 1, stop = 1, pause = 2):
                        readstmt = "searching for" + searstmt
                        print(readstmt)
                        webbrowser.open("https://google.com/search?q={0}" .format(searstmt), new=2)
                        speak(readstmt)

            for y in youtube:
                if y in phrase:
                    wrd = "play"
                    sstmt = phrase.partition(wrd)[2]
                    rstmt = "searching for" + sstmt + "on youtube"
                    print(rstmt)
                    webbrowser.open("https://www.youtube.com/results?search_query={0}".format(sstmt), new=2)
                    speak(rstmt)

            for m in name:
                if m in phrase:
                    speak("Hi! my name is Gobiji and please show some respect and add, 'ji', everytime you call me")        

        # elif inp1 == 'q':
        #     break
        
        
        # # inp = input("press q to stop")
        # # if inp == "q":
        # #     break
            if phrase == 'quit':
                break
        # #     break
        # # speak(phrase)