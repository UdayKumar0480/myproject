import pygame 

from pygame.locals import *
import os
import random
import pygame.mixer

L = []

for file in os.listdir(r"C:\Users\Uday Kumar Gandluri\Desktop\My_Python_Personal\Songs"):
	if file.endswith('.mp3'):
		L.append(file)

S = random.randint(0, len(L))

pygame.mixer.init()
filename = random.choice(L)
pygame.mixer.music.set_volume(0.50)

pygame.mixer.music.load(filename)

pygame.mixer.music.play(S)