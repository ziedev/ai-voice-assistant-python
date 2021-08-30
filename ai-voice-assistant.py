import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine = pyttsx3.init() 
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) # Choose the Gneder voice (Male or Female) 0 for male and 1 for female
newVoiceRate = 150
engine.setProperty("rate",newVoiceRate) # newVoiceRate is the speech speed
def speak(audio):
    engine.say(audio) # Speech 
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year) # get Current Year
    month = int(datetime.datetime.now().month) # get current month
    day = int(datetime.datetime.now().day) #get current day
    speak("the date is :")
    speak(day)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome Back Sir !")
    hour = datetime.datetime.now().hour #Get Current Hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif  hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif  hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Intellig Assistant at Your Service , How can I Help You ?")
def takeCommand():
    r = sr.Recognizer() #Initialize Recognizer
    with sr.Microphone() as source: # Make Microphone as Audio Source
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) # Get Speech from Mic
    try:
        print("Recongnizing ....")
        query = r.recognize_google(audio,language = "en=US") # Convert Speech to text (English Language)
    except Exception as e:
        print(e)
        speak("Say that again please ...")
        return "None"
    return query
def sendmail(to,content):
    # Configure Email Server
    server = smtplib.SMTP("smtp.gmail.com",587) # Your smtp server and PORT
    server.ehlo()
    server.starttls()
    server.login("mail@address.com","mailpassword") # Your Email address and password
    server.sendmail("mail@address.com",to,content)
    server.close()
def screenshot():
    img = pyautogui.screenshot() #Take ScreenShot
    imagename = "screennshot-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().year)+"-"+datetime.datetime.now().strftime("%I-%M-%S")+".png"
    img.save("C:/Scrren/"+imagename)
def cpu():
    usage = str(psutil.cpu_percent) #Get CPU usage Percent
    speak("CPU is at "+ usage+" %")
    battery = psutil.sensors_battery() #Get Battery Percent
    speak("battery is at "+str(battery.percent) +" %")
def jokes():
    speak(pyjokes.get_joke()) #Get Joke
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
            quit() #Exit Programm
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipeadia","")
            result = wikipedia.summary(query,sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should i say ?")
                content = takeCommand() #get email content from microphone input(converted to text)
                to = "zimaaloul@gmail.com"
                sendmail(to,content)
                speak("Email Sent Successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in web" in query or "search web" in query:
            speak("What should I search")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" #Your Browser exe file
            search = takeCommand().lower() #Get search query from Mic
            wb.get(chromepath).open_new_tab("https://www.google.com/search?q="+search.replace(" ","+"))
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdwn \s \t 1")
        elif "restart" in query:
            os.system("shutdwn \r \t 1")
        elif "play songs" in query:
            songsFolder = "C:/Users/zimaa/Desktop/Music" #Your Music Directory
            songs = os.listdir(songsFolder)
            os.startfile(os.path.join(songsFolder,songs[0]))
        elif "how are you" in query:
            speak("Fine Thank You , and what about You ?")
        elif "woman" in query:
            engine.setProperty("voice",voices[1].id)
            speak("Yes I m Heer , how can i help you ?")
        elif "remember that" in query:
            speak("What should i Remeber ?")
            data = takeCommand() #Remember Order
            speak("you said me to remember "+data)
            # Save your remember to data.txt
            f = open("data.txt", "a")
            f.write(data+"\n")
            f.close()
        elif "do you know anything" in query:
            #Read remember from data.txt
            file1 = open('data.txt', 'r')
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
            
            
        
            
                
