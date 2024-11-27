# pip install setuptools
# pip install google_speech
# pip install google
# pip install speechrecognition 
# pip install webbrowser 
# pip install pyttsx3 
# pip install requests 
# pip install openai 

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

engine = pyttsx3.init()
newsapi_key = "134ab2ac0bce4992b81f6e0250136a9d"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    try:
        client = OpenAI(
            api_key = "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"
            # api_key = "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",
        )

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
                {"role": "user", "content": command}
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
    
def processCommand(c):
    print(c)
    
    if "open" in c.lower():
        site = c.lower().split(" ")[1]
        webbrowser.open(f"https://www.{site}.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        # command: play skyfall
        # split will seperate and put words into a list: ['play', 'skyfall']
        # we will get element of index 1 and it will search for that in the library
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}")
        r.raise_for_status()  # Raises an error for HTTP codes 4xx/5xx

        # Process JSON response
        data = r.json()
        articles = data.get("articles", [])
        
        count = 1
        for article in articles:
            print(article.get("title"))
            speak(article.get("title"))
            count += 1
            if count >= 4:
                break
            
    else:
        # Let OpenAI handle the request
        output = aiProcess(command)
        print(output)
        speak(output)
        

        
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    #Listening for the wake word
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
                # timeout means for how much time it will wait without getting an input
                # phase_time_limit means for how long will it take input
            
            word = r.recognize_google(audio)
            print(word)
            
            if("jarvis" in word.lower()):
                if(word.lower() == "jarvis"):
                    speak("Ya")                
                    #Listen for command Jarvis
                    with sr.Microphone() as source:
                        print("Jarvis Active!")
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio)    
                else:
                    command = word.split(" ", 1)[1]

                processCommand(command)
                
        except Exception as e:
            print(f"Error... {e}")