import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
from playsound import playsound
from tkinter import Entry, Label
from tkinter import Button
from tkinter import Tk 
from tkinter import StringVar
from pytube import YouTube
from googletrans import Translator
import wikipedia as googleScrap
from pywikihow import search_wikihow
from Command import Give_Command as takeCommand
from Command import Speak

def TaskExe():

    Speak("Namaste")


    def WhatsApp():
        Speak("To whome")
        name=takeCommand()

        if 'sumit' or 'Sumit' in name:
            Speak("Ok Boss, What is the message?")
            msg=takeCommand()
            Speak("When should I send it?")
            hour=int(takeCommand())
            min=int(takeCommand())
            pywhatkit.sendwhatmsg("+9179000 90118",msg,hour,min,20)
            Speak("Message sent")

    def OpenApp():
        Speak("Ok Boss, Wait a second.")
        if 'open vs code' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'open blender' in query:
            os.startfile("C:\\Program Files\\Blender Foundation\\Blender 2.92\\blender.exe")

        elif 'open filomora' in query:
            os.startfile("C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe")

        elif 'open WhatsApp' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'open android studio' in query:
            os.startfile("E:\\Andriod Studio\\bin\\studio64.exe")

        elif 'open telegram' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

        elif 'open stream' in query:
            os.startfile("C:\\Users\\HP\\AppData\Local\\Programs\\LNV\\Stremio-4\\stremio.exe")
    
    def CloseApp():
        Speak("Ok boss")
        if 'close vs code' in query:
            os.system("TASKkILL /F /im Code.exe")

        elif 'close blender' in query:
            os.system("TASKKILL /F /im blender.exe")

        elif 'close filomora' in query:
            os.system("TASKKILL /F /im .exe")

        elif 'close WhatsApp' in query:
            os.system("TASKKILL /F /im WhatsApp.exe")

        elif 'close android studio' in query:
            os.system("TASKKILL /F /im studio64.exe")

        elif 'close telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'close straem' in query:
            os.system("TASKKILL /F /im stremio.exe")

    def YouTubeAuto():
        comm=takeCommand()
        if 'pause' in comm:
            keyboard.press('k')

        elif 'play' in comm:
            keyboard.press('space bar')

        elif 'rewind' in comm:
            keyboard.press('j')
        
        elif 'forward' in comm:
            keyboard.press('l')

        elif 'next  video' in comm:
            keyboard.press('N')

        elif 'previous video' in comm:
            keyboard.press('P')

        elif 'previous frame' in comm:
            keyboard.press(',')

        elif 'next frame' in comm:
            keyboard.press('.')

        elif 'decrease speed' in comm:
            keyboard.press('<')

        elif 'increase speed' in comm:
            keyboard.press('>')

        elif 'jump to 10 percent' in comm:
            keyboard.press('1')

        elif 'jump to 20 percent' in comm:
            keyboard.press('2')

        elif 'jump to 30 percent' in comm:
            keyboard.press('3')

        elif 'jump to 40 percent' in comm:
            keyboard.press('4')

        elif 'jump to 50 percent' in comm:
            keyboard.press('5')

        elif 'jump to 60 percent' in comm:
            keyboard.press('6')

        elif 'jump to 70 percent' in comm:
            keyboard.press('7')

        elif 'jump to 80 percent' in comm:
            keyboard.press('8')

        elif 'jump to 90 percent' in comm:
            keyboard.press('9')

        elif 'play from starting' in comm:
            keyboard.press('0')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'theater mode' in comm:
            keyboard.press('t')

        elif 'multiplayer mode' in comm:
            keyboard.press('i')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'captions' in comm:
            keyboard.press('c')

    def ChromeAuto():
        com=takeCommand()
        if 'open a new window' in com:
            keyboard.press_and_release('ctrl + n')

        elif 'open new incognito window' in com:
            keyboard.press_and_release('ctrl + shift + n')

        elif 'jump to new tab' in com:
            keyboard.press_and_release('ctrl + t')

        elif 'reopen closed tabs' in com:
            keyboard.press_and_release('strl + shift + t')

        elif 'jump to next tab' in com:
            keyboard.press_and_release('ctrl + page down')

        elif 'jump to previous' in com:
            keyboard.press_and_release('ctrl + page up')

        elif 'close this tab' in com:
            keyboard.press_and_release('ctrl + w')

        elif 'close current window' in com:
            keyboard.press_and_release('ctrl + shift + w')

        elif 'minimize the window' in com:
            keyboard.press_and_release('alt + space bar + n')

        elif 'select all' in com:
            keyboard.press_and_release('ctrl + a')

        elif 'copy the selected' in com:
            keyboard.press_and_release('ctrl + c')

    def Dict():
        Speak("Dictionary Activated")
        Speak("Whats the problem boss?")
        prob=takeCommand()

        if 'meaning' in prob:
            prob=prob.replace("friday what is tha meaning of","")
            result=Diction.meaning(prob)
            Speak(f"The meaning of {prob} is {result}")

        elif 'synonym' in prob:
            prob=prob.replace("friday what is tha synonym of","")
            result=Diction.synonym(prob)
            Speak(f"The synonym of {prob} is {result}")

        elif 'antonym' in prob:
            prob=prob.replace("friday what is tha antonym of","")
            result=Diction.antonym(prob)
            Speak(f"The antonym of {prob} is {result}")

        Speak("Exited dictionary")

    def TakeHindi():
        command=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            command.pause_threshold=1
            audio=command.listen(source)

        try:
            print("Recognizing...")
            query=command.recognize_google(audio,language='hi')
            print(f"You said: {query}")

        except:
            return "None"

        return query.lower()

    def Trans():
        Speak("Tell me the line")
        line=TakeHindi()
        translate=Translator()
        result=translate.translate(line)
        text=result.text
        Speak(text)

    def SpeedTest():
        from speedtest_cli import Speedtest
        Speak("Checking speed...")
        test=Speedtest()
        downloading=test.download()
        correctDown=int(downloading/800000)
        upload=test.upload()
        correctUp=int(upload/800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is {correctUp} mbps")

        elif 'downloading' in query:
            Speak(f"The downloading speed is {correctDown} mbps")

        else:
            Speak(f"The uploading speed is {correctUp} mbps and the downloading speed is {correctDown} mbps")

    while True:
        query=takeCommand()
        if 'hello' in query:
            Speak("Welcome")
            Speak("I am your personal AI assistant")
            Speak("How may I help you?")

        elif 'break' in query:
            Speak("Ok Boss")
            break

        elif 'youtube search' in query:
            Speak("What do you want to search")
            query = takeCommand()
            Speak("Ok Sir, This is what i found for your search!")
            web='https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)


        elif 'google search' in query:
            Speak("What do you want to search")
            query = takeCommand()
            Speak("Working on it Boss")
            pywhatkit.search(query)
            # ChromeAuto()


        elif 'play king' in query:
            Speak("Playing Boss")
            king='https://www.youtube.com/watch?v=9cclBKDC6fI&list=PLjzGKmjL1865VokzNfvMUEL0ualJcdrhs'
            webbrowser.open(king)
            

        elif 'wikipedia' in query:
            Speak("What do you want to search in Wikipedia")
            query = takeCommand()
            Speak("Searching Wikipedia")
            query=query.replace("friday","")
            query=query.replace("search","")
            query=query.replace("on wikipedia","")
            wiki=wikipedia.summary(query,2)
            Speak(f"According to wiki: {wiki}")
            # ChromeAuto()

        
        elif 'send message' in query:
            WhatsApp()

        
        elif 'screenshot' in query:
            Speak("OK boss, What should i name the file?")
            path=takeCommand()
            path1name=path+".jpeg"
            path1="E:\\Friday"+path1name
            kk=pyautogui.screenshot()
            kk.save(path1)
            os.startfile("E:\\")
            Speak("Here is your screenshot sir.")

        elif 'open vs code' in query:
            OpenApp()

        elif 'open blender' in query:
            OpenApp()

        elif 'open filomora' in query:
            OpenApp()

        elif 'open WhatsApp' in query:
            OpenApp()

        elif 'open android studio' in query:
            OpenApp()

        elif 'open telegram' in query:
            OpenApp()

        elif 'open stream' in query:
            OpenApp()

        elif 'close vs code' in query:
            CloseApp()

        elif 'close blender' in query:
            CloseApp()

        elif 'close filomora' in query:
            CloseApp()

        elif 'close WhatsApp' in query:
            CloseApp()

        elif 'close android studio' in query:
            CloseApp()

        elif 'close telegram' in query:
            CloseApp()

        elif 'close straem' in query:
            CloseApp()

        elif 'pause' in query:
            YouTubeAuto()

        elif 'play' in query:
            YouTubeAuto()

        elif 'rewind' in query:
            YouTubeAuto()
        
        elif 'forward' in query:
            YouTubeAuto()

        elif 'next  video' in query:
            YouTubeAuto()

        elif 'previous video' in query:
            YouTubeAuto()

        elif 'previous frame' in query:
            YouTubeAuto()

        elif 'next frame' in query:
            YouTubeAuto()

        elif 'decrease speed' in query:
            YouTubeAuto()

        elif 'increase speed' in query:
            YouTubeAuto()

        elif 'jump to 10 percent' in query:
            YouTubeAuto()

        elif 'jump to 20 percent' in query:
            YouTubeAuto()

        elif 'jump to 30 percent' in query:
            YouTubeAuto()

        elif 'jump to 40 percent' in query:
            YouTubeAuto()

        elif 'jump to 50 percent' in query:
            YouTubeAuto()

        elif 'jump to 60 percent' in query:
            YouTubeAuto()

        elif 'jump to 70 percent' in query:
            YouTubeAuto()

        elif 'jump to 80 percent' in query:
            YouTubeAuto()

        elif 'jump to 90 percent' in query:
            YouTubeAuto()

        elif 'play from starting' in query:
            YouTubeAuto()

        elif 'full screen' in query:
            YouTubeAuto()

        elif 'theater mode' in query:
            YouTubeAuto()

        elif 'multiplayer mode' in query:
            YouTubeAuto()

        elif 'mute' in query:
            YouTubeAuto()

        elif 'captions' in query:
            YouTubeAuto()

        elif 'open a new window' in query:
            ChromeAuto()

        elif 'open new incognito window' in query:
            ChromeAuto()

        elif 'jump to new tab' in query:
            ChromeAuto()

        elif 'reopen closed tabs' in query:
            ChromeAuto()

        elif 'jump to next tab' in query:
            ChromeAuto()

        elif 'jump to previous' in query:
            ChromeAuto()

        elif 'close this tab' in query:
            ChromeAuto()

        elif 'close current window' in query:
            ChromeAuto()

        elif 'minimize the window' in query:
            ChromeAuto()
        elif 'select all' in query:
            ChromeAuto()

        elif 'copy the selected' in query:
            ChromeAuto()


        elif 'joke' in query:
            get=pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("Ok Boss")
            jj=takeCommand()
            Speak(f"You said {jj}")

        elif 'show my location' in query:
            Speak("Ok boss, Wait a second")
            webbrowser.open('https://www.google.com/maps/@28.9879887,76.9950234,18.5z')

        elif 'dictionary' in query:
            Dict()
        
        elif 'set alarm' in query:
            Speak("Tell me the time")
            time=input("Enter the time: ")

            while True:
                TIme_Ac=datetime.datetime.now()
                now=TIme_Ac.strftime("%H:%M")

                if now==time:
                    Speak("Time to wake up boss")
                    playsound('iron man.mp3')
                    Speak("Alarm closed")

                elif now>time:
                    Speak("Alarm closed")
                    break

        elif 'download video' in query:
            root=Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube video downloader")
            Speak("Enter the link here!")
            Label(root,text="YouTube video downloader",font='arial 15 bold').pack()
            link=StringVar()
            Label(root,text="Paste the link here",font='arial 15 bold').place(x=160,y=60)
            Entry(root,width=70,textvariable=link).place(x=32,y=90)

            def VideoDownloader():
                url=YouTube(str(link.get()))
                video=url.streams.first()
                video.download()
                Label(root,text="Downloaded",font='arial 15').place(x=180,y=210)

            Button(root,text="Download",font='arial 15 bold',bg='violet',padx=2,command=VideoDownloader).place(x=180,y=150)
            root.mainloop()
            Speak("Video is bein downloaded")

        elif 'translate' in query:
            Trans()

        elif 'remember that' in query:
            remeberMSg=query.replace("remember that","")
            remeberMSg=remeberMSg.replace("friday","")
            Speak("You told me to remind that: "+remeberMSg)
            remeber=open('data.txt','w')
            remeber.write(remeberMSg)
            remeber.close()

        elif 'remind me' in query:
            remeber=open('data.txt','r')
            Speak("You told me to remember that: "+remeber.read())

        elif 'tell me summary' in query:
            query=query.replace("friday tell me summary of","")
            Speak("This is what i found on web")
            # pywhatkit.search(query)

            try:
                result=googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable data found")
                
        elif 'internet speed' in query:
            SpeedTest()

        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'how to' in query:
            Speak("Getting data from internet")
            op=query.replace("friday","")
            max_result=1
            how_to_func=search_wikihow(op,max_result)
            assert len(how_to_func)==1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'sleep' in query:
            Speak("OK boss")
            os.system('cmd /c "powercfg -hibernate off"')
            os.system('cmd /c "rundll32.exe powrprof.dll,SetSuspendState sleep"')


 

TaskExe()

