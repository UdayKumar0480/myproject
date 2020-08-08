
from playsound import playsound
playsound("D:\mp3\FreakOut.mp3")
#adb logcat -v threadtime > logs.log

'''
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('D:\FreakOut.mp3')
mixer.music.play()


import vlc
p = vlc.MediaPlayer("D:\FreakOut.mp3")
p.play()



import os
import random 
path="D:\mp3"
files=os.listdir(path)
d=random.choice(files)
os.startfile(d)
'''