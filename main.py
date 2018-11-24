# -*- coding: utf-8 -*-
import time
import os
import pygame
from tabulate import tabulate
os.system('clear')
pygame.init()
pygame.mixer.music.load("lose sound.mp3")

oxygen = 30
OC2 = 100
Fuel = 100
batery = 100

CBLUE = '\033[94m'
CRED = '\033[31m'
CEND = '\033[0m'
while 1:

	print(CBLUE + """
  /$$$$$$   /$$$$$$  /$$        /$$$$$$  /$$   /$$ /$$     /$$
 /$$__  $$ /$$__  $$| $$       /$$__  $$| $$  / $$|  $$   /$$/
| $$  \__/| $$  \ $$| $$      | $$  \ $$|  $$/ $$/ \  $$ /$$/ 
| $$ /$$$$| $$$$$$$$| $$      | $$$$$$$$ \  $$$$/   \  $$$$/  
| $$|_  $$| $$__  $$| $$      | $$__  $$  >$$  $$    \  $$/   
| $$  \ $$| $$  | $$| $$      | $$  | $$ /$$/\  $$    | $$    
|  $$$$$$/| $$  | $$| $$$$$$$$| $$  | $$| $$  \ $$    | $$    
 \______/ |__/  |__/|________/|__/  |__/|__/  |__/    |__/    
                                                              
                                                                            
	""" + CEND)
	print (CRED + tabulate([['oxygen', str(oxygen) + "%"], ['OC2', str(OC2) + "%"], ['Fuel', str(Fuel) + "%"], ['batery', str(batery) + "W"]],
	 headers=['Parametr', 'Value']) + CEND)
	if oxygen < 10:
		print("Critical level of oxygen!")
	if oxygen == 2:
		pygame.mixer.music.play()
		time.sleep(10)
		break
	oxygen -= 2
	OC2 -= 1
	Fuel -= 2
	batery -= 1
	time.sleep(60)
	os.system('clear')


