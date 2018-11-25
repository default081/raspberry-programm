# -*- coding: utf-8 -*-
import time
from pymouse import PyMouse
import os
from tabulate import tabulate
os.system('clear')
m = PyMouse()
m.move(600,600)

oxygen = 60
OC2 = 20
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
	print (CRED + tabulate([['oxygen', str(oxygen) + "%", '100%'], ['CO2', str(OC2) + "%", '20%'], ['Fuel', str(Fuel) + "%", '100%'], ['batery', str(batery) + "W", '100%']],
	 headers=['Parameter', 'Value', 'Status']) + CEND)
	if oxygen < 10:
		print(CRED + "\n \nCritical level of oxygen!" +  CEND)
	if oxygen == 2:
		print(CRED + "\n \nYou Are Dead!" +  CEND)
		time.sleep(20)
		break
		
	oxygen -= 1
	OC2 += 1
	m.click(600,600)
	time.sleep(60)
	os.system('clear')
