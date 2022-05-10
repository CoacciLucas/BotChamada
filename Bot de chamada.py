import speech_recognition as sr
import pyttsx3
import pyautogui as pg


audio = sr.Recognizer()
maquina = pyttsx3.init()

try:
    with sr.Microphone() as source:
        print('Ouvindo..')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'tina' in comando:
            print(comando)
            pg.write('!!!!!! PRESENTE !!!!!!')
            pg.press('enter')
            maquina.runAndWait()
except Exception as e:
    print(e)
