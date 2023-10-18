from gtts import gTTS
from playsound import playsound
import os
from englisttohindi.englisttohindi import EngtoHindi
from main import TaskExe

def res_hindi(text,i):
    translation = EngtoHindi(text)
    tts_hindi = gTTS(text=translation.convert, lang='hi')
    save_path = os.path.join('Test',f'{i}.mp3')
    tts_hindi.save(save_path)
    playsound(save_path)
    # os.remove(save_path)

TaskExe()

# data = ['']
# for i,text in enumerate(data):
#     res_hindi(text,i)