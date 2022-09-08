#!/usr/bin/python3

import random
import time
temperature = random.randint(1,30)
print(f'The temperature is being measured, please hold...')
time.sleep(2)
input('Measurement is complete, please press enter to continue...')
if temperature <= 20:
   print(f'The temperature is {temperature} degrees, chilly huh? Turning ON the termostat')
elif temperature > 20:
   print(f'The temperature is {temperature} degrees, thats warm enough. Turning OFF the termostat')
time.sleep(2)
print('***Shutting down***')
