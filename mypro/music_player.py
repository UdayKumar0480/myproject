'''
from pygame import mixer
import os
mixer.init()
#clips = os.listdir(r"C:\Users\Uday Kumar Gandluri\Desktop\My_Python_Personal\Songs")
song_list = []
for file in os.listdir(r"C:\Users\Uday Kumar Gandluri\Desktop\My_Python_Personal\Songs"):
	if file.endswith('.mp3'):
		song_list.append(file)
#mixer.music.load("Ala Vaikunthapurramuloo.mp3")
#mixer.music.load("Ay Pilla.mp3")
#mixer.music.load("ButtaBomma.mp3")
#mixer.music.load("Dhak Dhak Dhak.mp3")
#mixer.music.load("Emai Pothane.mp3")
#mixer.music.load("Faded.mp3")
#mixer.music.load("Gundegilli.mp3")
mixer.music.load(song_list[0])
mixer.music.set_volume(20.0)
mixer.music.play()
while True:
	print("press 'p' to pause 'r' to resume")
	print("press 'e' to exit the program")
	print("press 'n' to play next song")
	query = input(">>>")
	if query == "p":
		mixer.music.pause()
	elif query == "r":
		mixer.music.unpause()
	elif query == "e":
		mixer.music.exit()
	elif query == "n":
		mixer.music.exit()
		break
'''

	
import pygame 

from pygame.locals import *

import random

import pygame.mixer

L = []

for file in os.listdir(r"C:\Users\Uday Kumar Gandluri\Desktop\My_Python_Personal\Songs"):
	if file.endswith('.mp3'):
		L.append(file)

S = random.randint(0, len(L))

pygame.mixer.init()

pygame.mixer.music.set_volume(0.50)

pygame.mixer.music.load(L[0])

pygame.mixer.music.play(S)