import speech_recognition as sr
import pyautogui as pg
import pyttsx3


audio = sr.Recognizer()
maquina = pyttsx3.init()

palavras = ['lucas', 'chamada', 'luciano', 'lucas, ta ai?',
            'lucas ta ai', 'lucas?', 'lucas coassi', 'lucas coati']

while True:
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            matchers = [comando]
            matching = [s for s in palavras if any(xs in s for xs in matchers)]
            if matching:
                print(comando)
                pg.write('!!!!!! PRESENTE !!!!!!')
                pg.press('enter')
                maquina.runAndWait()
    except Exception as e:
        print(e)
