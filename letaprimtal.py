#!/usr/bin/python3

#leta primtal

numbersToTest = int(input('How many numbers would you like to test?: '))

#yttre loop - prova samtliga tal upp till numbersToTest
for i in range(1,numbersToTest+1):
   #inre loop - prova om talet i ar jamt delbart med nagot annat tal an '1' och 'i'
   #isf ar det ej ett primtal.
   provenNotPrime = False
   for k in range(2,i):
      if i % k == 0:
         print(f'{i} is not a prime number')
         provenNotPrime = True
         break
   if provenNotPrime == False:
      print(f'                                 *** {i} is a Prime number! ***')
