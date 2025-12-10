import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize
import db

def start():
    eel.init('www')

        
    flag= recoganize.AuthenticateFace()
        
    if flag==1:
        playAssistancesound()
        os.system('start msedge.exe --app="http://localhost:8000/index.html"')
        eel.start('index.html', mode=None, host='localhost', block=True)
