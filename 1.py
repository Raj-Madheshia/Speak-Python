import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx3
from tkinter import *
import threading
from symbol import symbol
from buildfunc import func
from sentence import sentenceHandler

# This function is for Speaking Audio
def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()
    
# This function for Recording Audio
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

# This is App class
# this is is build for multithreading behaviour of System
# This is Imporant to run tkinter and backend both at the same time

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
        
    def print(self, data):
        if data != "":
            self.text.insert(END, data)
    
    def run(self):
        
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.textContainer = Frame(self.root, borderwidth=1, relief="sunken")
        self.text = Text(self.textContainer, width=80, height=80, wrap="none", borderwidth=0, font=('consolas', '12'))
        self.textVsb = Scrollbar(self.textContainer, orient="vertical", command=self.text.yview)
        self.textHsb = Scrollbar(self.textContainer, orient="horizontal", command=self.text.xview)
        self.text.configure(yscrollcommand=self.textVsb.set, xscrollcommand=self.textHsb.set)
        self.text.grid(row=0, column=0, sticky="nsew")
        self.textVsb.grid(row=0, column=1, sticky="ns")
        self.textHsb.grid(row=1, column=0, sticky="ew")
        self.textContainer.grid_rowconfigure(0, weight=1)
        self.textContainer.grid_columnconfigure(0, weight=1)
        self.textContainer.pack(side="top", fill="both", expand=True)
        self.root.mainloop()


app = App()
print('Now we can continue running code while mainloop runs!')

    
# initialization
time.sleep(2)
speak("Hi Raj, what can I do for you?")
while 1:
    data = recordAudio()
    if data == "":
        print("Nothing")
    elif "symbol" in data.lower():
        data = symbol(data)
    elif "define function" in data.lower():
        data = func(data)
    else:
        data = sentenceHandler(data)
    app.print(data)

