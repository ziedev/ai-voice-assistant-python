import pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes



# pipwin install pyaudio

engine = pyttsx3.init()
#voices = engine.getProperty("voices")
#engine.setProperty("voice",voices[1].id)
#newVoiceRate = 1500
#engine.setProperty("rate",newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

#speak("this is friday")
#time()
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the date is :")
    speak(day)
    speak(month)
    speak(year)
#date()
def wishme():
    speak("Welcome Back Sir !")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif  hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif  hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Entellig Assistant at Your Service , How can I Help You ?")
#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing ....")
        query = r.recognize_google(audio,language = "en=US")
    except Exception as e:
        print(e)
        speak("Say that again please ...")
        return "None"
    return query
def sendmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("mail@address.com","mailpassword")
    server.sendmail("mail@address.com",to,content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    imagename = "screennshot-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().year)+"-"+datetime.datetime.now().strftime("%I-%M-%S")+".png"
    img.save("C:/Scrren/"+imagename)

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU is at "+ usage+" %")
    battery = psutil.sensors_battery()
    speak("battery is at "+str(battery.percent) +" %")
def jokes():
    speak(pyjokes.get_joke())
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("GoodBye")
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipeadia","")
            result = wikipedia.summary(query,sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should i say ?")
                content = takeCommand()
                to = "zimaaloul@gmail.com"
                sendmail(to,content)
                speak("Email Sent Successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in web" in query or "search web" in query:
            speak("What should I search")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            print(search)
            wb.get(chromepath).open_new_tab("https://www.google.com/search?q="+search.replace(" ","+"))
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdwn \s \t 1")
        elif "restart" in query:
            os.system("shutdwn \r \t 1")
        elif "play songs" in query:
            songsFolder = "C:/Users/zimaa/Desktop/Music"
            songs = os.listdir(songsFolder)
            os.startfile(os.path.join(songsFolder,songs[0]))
        elif "remember that" in query:
            speak("What should i Remeber ?")
            data = takeCommand()
            speak("you said me to remember "+data)
            f = open("data.txt", "a")
            f.write(data+"\n")
            f.close()
        elif "do you know anything" in query:
            file1 = open('data.txt', 'a')
            Lines = file1.readlines()
            count = 0
            speak("You said me to remember that ")
            for line in Lines:
                count += 1
                speak(line)
            if count == 0:
                speak("Sorry i don't have any note")
            file1.close()
        elif "screenshot" in query:
            screenshot()
            speak("Done. Screenshot Taken")
        elif "cpu" in query or "battery" in query:
            cpu()
        elif "joke" in query:
            jokes()
            
            
        
            
                
