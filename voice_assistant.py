import os

import google.cloud.speech

# Set the path to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"Your API KEY DIRECTORY"

import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time


def sptext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            data = r.recognize_google_cloud(audio,language="hi-in")
            print(data)
            return data1
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Sorry! Voice not recognized.")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(x)
    engine.runAndWait()


# speechtx("Recording in progress.")
# sptext()

if __name__ == "__main__":
    if "Hey Alex" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "Your name" in data1:
                name = "My name is Alex."
                speechtx(name)
            elif "Old are you" in data1:
                age = "I am two years old"
                speechtx(age)
            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif 'Youtube' in data1:
                webbrowser.open('https://www.youtube.com/')
            elif 'ChatGPT' in data1:
                webbrowser.open('https://chatgpt.com/?oai-dm=1')
            elif 'Google' in data1:
                webbrowser.open('https://www.google.com/')
            elif 'Hi Anime' in data1:
                webbrowser.open('https://hianime.to/home')
            elif 'CUIMS' in data1:
                webbrowser.open('https://students.cuchd.in/')
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="all")
                print(joke_1)
                speechtx(joke_1)
            elif "exit" in data1:
                speechtx("Thank You")
                break
            time.sleep(7)
            # elif 'open wallpaper' in data1:
            #     add = r"Directory of the file/folder"
            #     listwallpaper = os.listdir(add)
            #     print(listwallpaper)
            #     os.startfile(os.path.join(add,listwallpaper[0]))
    else:
        print("Okay!")
#     assert os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is not None, \
#         "Set the GOOGLE_APPLICATION_CREDENTIALS environment variable"
