from gtts import gTTS
import speech_recognition as sr
from mtranslate import translate
from playsound import playsound
import os
from englisttohindi.englisttohindi import EngtoHindi
from Preprocess import preprocess_text

def translate_to_eng(hindi):
	translation = translate(hindi)
	return translation

def Speak(audio):
    res_hindi(audio)

def takeCommand():
    command=sr.Recognizer()
    query = ''
    with sr.Microphone() as source:
        print("Listening..")
        command.pause_threshold = 0.5
        audio=command.listen(source)

        try:
            print("Recognizing...")
            query=command.recognize_google(audio, language='hi-IN')
            print(f"You said: {query}")

        except Exception as e:
              print(e)

        return query.lower()     

def res_hindi(text):
    translation = EngtoHindi(text)
    tts_hindi = gTTS(text=translation.convert, lang='hi')
    save_path = os.path.join('Audio','hindi.mp3')
    tts_hindi.save(save_path)
    playsound(save_path)
    os.remove(save_path)

def Give_Command():
    text = takeCommand()
    tts_eng = translate_to_eng(text)
    tts_eng = preprocess_text(tts_eng)
    print(tts_eng)
    
    return tts_eng
