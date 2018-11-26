# -*- coding: utf-8 -*-
import time
from pymouse import PyMouse
import os
from tabulate import tabulate
os.system('clear')
m = PyMouse()
m.move(600,600)

oxygen = 60
pressure = 59
humidity = 42 #static
temperatute = 21 #static
OC2 = 0
Fuel = 47 #static
batery = 72 #static
voltageSP = 80 #static

pressureStatus = "Norm"
CO2status = "Norm"


CBLUE = '\033[94m'
CRED = '\033[31m'
CGREEN = '\033[92m'
CEND = '\033[0m'
while 1:


	if(pressure <= 49):
		pressureStatus = "Abnormally"
	if(OC2 >= 5):
		CO2status = "Abnormally"


	print (CGREEN + tabulate([['Pressure', str(pressure) + ' kPa', pressureStatus], ['Temperatute', str(temperatute) + ' C', "Norm"], ['Humidity', str(humidity) + ' %', "Norm"], ['oxygen', str(oxygen) + " %", "Abnormally"], ['CO2', str(OC2) + " %", CO2status], ['Voltage of solar panel', str(voltageSP) + " V", "Norm"], ['Batery voltage', str(batery) + " V", "Norm"], ['Fuel', str(Fuel) + " %", "Norm"]],
	 headers=['Parameter', 'Value', 'Status']) + CEND)

	print(CRED + "\n \nAttention! L'impermeabilite de la navette est cassee!" +  CEND)

	if oxygen <= 10:
		print(CRED + "\n \nNiveau critique d'oxygène" +  CEND)

	if oxygen == 0:
		time.sleep(20)
		break

	pressure -= 0.5
	oxygen -= 1
	OC2 += 0.5
	m.click(600,600)
	time.sleep(0.2)
	# time.sleep(60)
	os.system('clear')

	# print (CGREEN + tabulate([['Pressure', str(pressure) + ' kPa', "Norm"], ['Temperatute', str(temperatute) + ' C', "Norm"], ['Humidity', str(humidity) + ' %', "Norm"], ['oxygen', str(oxygen) + " %", "Abnormally"], ['CO2', str(OC2) + " %", "Norm"], ['Voltage of solar panel', str(voltageSP) + " V", "Norm"], ['Batery voltage', str(batery) + " V", "Norm"], ['Fuel', str(Fuel) + " %", "Norm"]],
	 # headers=['Parameter', 'Value', 'Status']) + CEND)
