from pipes import quote
import subprocess
from  playsound import playsound
import eel
import os
import sqlite3
import pyautogui
from engine.config import ASSISTANCE_NAME, system_apps, web_apps, contacts
#from engine import config
from engine.command import *
import pywhatkit as kit
import re

import webbrowser
from engine.helper import extact_yt_term  , remove_words,get_api_key
import pvporcupine
import pyaudio
import struct 
import time

import google.generativeai as genai


#playing assistance sound function
@eel.expose
def playAssistancesound():
    music_dir = 'www/assets/audio/start_sound.mp3'
    playsound(music_dir)



def openCommand(query):
    con = sqlite3.connect("config.db")
    cursor = con.cursor()
    query = query.replace(ASSISTANCE_NAME, "")
    query = query.replace("open", "")
    query=query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT app_path FROM system_apps WHERE app_name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT web_path FROM webpages WHERE web_name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except Exception as e:
            speak("some thing went wrong:" )

       

    

def PlayYoutube(query):
    search_term=extact_yt_term(query)
    search_term=str(search_term)
    speak("playing"+search_term+'on youtube')
    kit.playonyt(search_term)


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j by automaticcaly with pyautogui
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# find contacts
# find contacts
def findContact(query):
    con = sqlite3.connect("config.db")
    cursor = con.cursor()
    words_to_remove = [ASSISTANCE_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT number FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        con.commit()
        if results:
            con.close()
            print(results[0][0])
            mobile_number_str = str(results[0][0])

            if not mobile_number_str.startswith('+91'):
                mobile_number_str = '+91' + mobile_number_str

            return mobile_number_str, query
        else:
            speak('please mention contact name or add contact in settings')
            con.close()
            return 0,0        
    except Exception as e:
        print(e)
        return 0, 0

#whatsapp message
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 6
        message = ''
        jarvis_message = "calling to "+name

    elif flag== 'videocall':
        target_tab = 5
        message = ''
        jarvis_message = "staring video call with "+name
    else:
        return


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)


# to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(136, 2220)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1397)
    speak("message send successfully to "+name)

# chat bot 
def chatBot(query):
    api_key=get_api_key()

    api_key=str(api_key)
    genai.configure(api_key=api_key)




    model = genai.GenerativeModel("models/gemini-2.5-flash")
    user_input = query.lower()

    

    try:
        response = model.generate_content(user_input)
        response_text = response.text
        eel.DisplayMessage(response_text)
        print(response_text)
        speak( response_text)

    except Exception as e:
        speak(e)
