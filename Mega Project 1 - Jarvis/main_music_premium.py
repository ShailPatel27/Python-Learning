import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from openai import OpenAI

# Spotify Authentication Setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="68f07b71b5514026b8a101603feba7bc", 
                                               client_secret="22a4045193d34706af589e981f439cee", 
                                               redirect_uri="http://localhost:8888/callback", 
                                               scope=["user-library-read", "user-read-playback-state", "user-modify-playback-state"]))

engine = pyttsx3.init()
newsapi_key = "134ab2ac0bce4992b81f6e0250136a9d"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    try:
        client = OpenAI(
            api_key = "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"
        )

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
                      {"role": "user", "content": command}]
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
        # Use Spotify API to search for the song
        result = sp.search(q=song, type="track", limit=1)
        track_url = result['tracks']['items'][0]['external_urls']['spotify']
        
        # Now play the song
        sp.start_playback(uris=[result['tracks']['items'][0]['uri']])
        speak(f"Playing {song} on Spotify")
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}")
        r.raise_for_status()

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
