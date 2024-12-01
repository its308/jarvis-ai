import webbrowser
import speech_recognition as sr
import os
import datetime
import requests



def say(text):
    os.system(f'say "{text}"')

newsapi="f0946a34f0424000a00e4e93e071de86"
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"



if __name__ == '__main__':
    print("pycharm")
    say("hello Madam, i am jarvis A.I.")
    while True:
        print("Listening...")
        query=takeCommand()
        sites=[["youtube","https://youtube.com"],["google","https://google.com"],["whatsapp","https://whatsapp.com"],["wikipedia","https://wikipedia.com"]]
        for site in sites:
            if (f"open {site[0]}").lower() in query.lower():
               say(f"Opening {site[0]} madam..")
               webbrowser.open(site[1])
        if("Play Music").lower() in query.lower():
            musicPath="/Users/itishachoudhary/Downloads/vinee-heights-126947.mp3"
            os.system(f"open {musicPath}")
        elif ("the time").lower() in query.lower():
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Mam, the time is {strfTime}")
        elif ("open camera").lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
        elif ("news").lower() in query.lower():
            r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=f0946a34f0424000a00e4e93e071de86")
            # Checking if the request was successful
            if r.status_code == 200:
                data = r.json()  # Parse the response as JSON
                articles = data.get("articles", [])

                # Loop through the articles and print the headlines
                for article in articles:
                    say(article.get("title"))
                 #otherwise let chatgpt handle the request
        else:
            say("Failed to fetch the headlines")







